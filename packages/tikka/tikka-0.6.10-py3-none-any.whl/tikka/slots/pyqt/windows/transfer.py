# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import logging
import sys
from typing import Optional

from PyQt5.QtCore import QMutex
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QCompleter, QDialog, QWidget
from substrateinterface import Keypair
from substrateinterface.utils.ss58 import is_valid_ss58_address

from tikka.domains.application import Application
from tikka.domains.entities.account import Account
from tikka.domains.entities.constants import AMOUNT_UNIT_KEY, DATA_PATH
from tikka.interfaces.adapters.repository.preferences import SELECTED_UNIT
from tikka.slots.pyqt.entities.constants import ICON_LOADER
from tikka.slots.pyqt.entities.worker import AsyncQWorker
from tikka.slots.pyqt.resources.gui.windows.transfer_rc import Ui_TransferDialog


class TransferWindow(QDialog, Ui_TransferDialog):
    """
    TransferWindow class
    """

    def __init__(
        self,
        application: Application,
        account: Account,
        mutex: QMutex,
        parent: Optional[QWidget] = None,
    ):
        """
        Init transfer window

        :param application: Application instance
        :param account: Account instance
        :param mutex: QMutex instance
        :param parent: QWidget instance
        """
        super().__init__(parent=parent)
        self.setupUi(self)

        # only open if account is unlocked
        if application.wallets.is_unlocked(account.address) is False:
            raise ValueError("TransferWindow: sender account is locked")

        self.application = application
        self.account = account
        self.mutex = mutex
        self._ = self.application.translator.gettext

        # substrate error message for gettext extraction
        self._("Transfer/payment would kill account")
        self._("Balance too low to send value")

        # init unit from preference or default
        unit_preference = self.application.preferences_repository.get(SELECTED_UNIT)
        if unit_preference is not None:
            self.unit = unit_preference
        else:
            self.unit = AMOUNT_UNIT_KEY

        self.init_units()

        self.recipient_account: Optional[Account] = None
        self.amount_value = 0
        self.fees = None
        self.transfer_success: Optional[bool] = None

        self.senderAddressValueLabel.setText(account.address)
        self.feesButton.setDisabled(True)
        self.sendButton.setDisabled(True)

        # animated loading icon
        self.loader_movie = QMovie(ICON_LOADER)
        self.loader_movie.start()
        self.loaderIconLabel.setMovie(self.loader_movie)
        self.loaderIconLabel.hide()

        # recipient autocomplete (dirty version)
        # todo: create a model to fetch only a filtered list from database on edit
        self.account_address_by_name = {
            account.name: account.address
            for account in self.application.accounts.get_list()
        }
        account_wordlist = list(self.account_address_by_name.keys()) + list(
            self.account_address_by_name.values()
        )
        completer = QCompleter(account_wordlist)
        self.recipientNameOrAddressLineEdit.setCompleter(completer)

        self._update_ui()

        # events
        self.recipientNameOrAddressLineEdit.textChanged.connect(
            self._on_recipient_address_line_edit_changed
        )
        self.amountDoubleSpinBox.valueChanged.connect(
            self._on_amount_double_spin_box_changed
        )
        self.amountUnitComboBox.activated.connect(self._on_unit_changed)
        self.feesButton.clicked.connect(self._on_fees_button_clicked)
        self.sendButton.clicked.connect(self._on_send_button_clicked)
        self.buttonBox.button(self.buttonBox.Close).clicked.connect(self.close)

        ##############################
        # ASYNC METHODS
        ##############################
        # fetch recipient balance
        self.fetch_recipient_balance_from_network_async_qworker = AsyncQWorker(
            self.fetch_recipient_balance_from_network, self.mutex
        )
        self.fetch_recipient_balance_from_network_async_qworker.finished.connect(
            self._on_finished_fetch_recipient_balance_from_network
        )
        # fetch sender balance
        self.fetch_sender_balance_from_network_async_qworker = AsyncQWorker(
            self.fetch_sender_balance_from_network, self.mutex
        )
        self.fetch_sender_balance_from_network_async_qworker.finished.connect(
            self._on_finished_fetch_sender_balance_from_network
        )

        # fetch fees from network
        self.fetch_fees_from_network_async_qworker = AsyncQWorker(
            self.fetch_fees_from_network, self.mutex
        )
        self.fetch_fees_from_network_async_qworker.finished.connect(
            self._on_finished_fetch_fees_from_network
        )
        # send transfer to network
        self.send_tranfer_to_network_async_qworker = AsyncQWorker(
            self.send_transfer_to_network, self.mutex
        )
        self.send_tranfer_to_network_async_qworker.finished.connect(
            self._on_finished_send_transfer_to_network
        )

    def _on_unit_changed(self):
        """
        Triggered when unit combo box is changed

        :return:
        """
        self.unit = self.amountUnitComboBox.currentData()
        self._update_ui()

    def _on_amount_double_spin_box_changed(self):
        """
        Triggered when the amount spin box is changed

        :return:
        """
        self.amount_value = self.amountDoubleSpinBox.value()
        if self.recipient_account is not None and self.amount_value > 0:
            self.feesButton.setDisabled(False)
            self.sendButton.setDisabled(False)

    def fetch_recipient_balance_from_network(self):
        """
        Fetch last account data from the network

        :return:
        """
        self.loaderIconLabel.show()
        self.application.accounts.fetch_balance_from_network(self.recipient_account)

    def _on_finished_fetch_recipient_balance_from_network(self):
        """
        Triggered when async request fetch_from_network is finished

        :return:
        """
        self.loaderIconLabel.hide()
        self._update_ui()

    def fetch_sender_balance_from_network(self):
        """
        Fetch last sender account data from the network

        :return:
        """
        self.loaderIconLabel.show()
        self.application.accounts.fetch_balance_from_network(self.account)

    def _on_finished_fetch_sender_balance_from_network(self):
        """
        Triggered when async request fetch_from_network is finished

        :return:
        """
        self.loaderIconLabel.hide()
        self._update_ui()

    def _on_recipient_address_line_edit_changed(self):
        """
        Triggered when text in the recipient address field is changed

        :return:
        """
        address_or_name = self.recipientNameOrAddressLineEdit.text().strip()

        try:
            address_is_valid = is_valid_ss58_address(address_or_name)
        except IndexError:
            address_is_valid = False

        if not address_is_valid:
            # if entry is a known account name...
            if address_or_name in self.account_address_by_name:
                # display address under the name
                self.recipientNameOrAddressValueLabel.setText(
                    self.account_address_by_name[address_or_name]
                )
                self._get_recipient_account(
                    self.account_address_by_name[address_or_name]
                )
                if self.recipient_account is not None and self.amount_value > 0:
                    self.feesButton.setDisabled(False)
                    self.sendButton.setDisabled(False)
            else:
                self.recipientBalanceValueLabel.setText(self._("Invalid!"))
                self.recipientBalanceValueLabel.setToolTip(
                    self._("Invalid address! Please check it again.")
                )
                self.recipient_account = None
                self.feesButton.setDisabled(True)
                self.sendButton.setDisabled(True)
        else:
            # display name under the address
            for key, value in self.account_address_by_name.items():
                if value == address_or_name:
                    self.recipientNameOrAddressValueLabel.setText(key)
            self._get_recipient_account(address_or_name)
            if self.recipient_account is not None and self.amount_value > 0:
                self.feesButton.setDisabled(False)
                self.sendButton.setDisabled(False)

    def _get_recipient_account(self, address: str) -> None:
        """
        Get recipient account

        :return:
        """
        self.recipient_account = None
        try:
            Keypair(
                ss58_address=address,
                ss58_format=self.application.currencies.get_current().ss58_format,
            )
        except ValueError as exception:
            logging.exception(exception)
            self.recipientBalanceValueLabel.setText(self._("Invalid!"))
            self.recipientBalanceValueLabel.setToolTip(
                self._("Invalid address! Please check it again.")
            )
            self.recipient_account = None
            return None

        # search in local account list
        for account in self.application.accounts.get_list():
            if account.address == address:
                self.recipient_account = account
                self._update_ui()
                return None

        # create account and fetch balance
        self.recipient_account = Account(address)
        self.fetch_recipient_balance_from_network_async_qworker.start()

        return None

    def _update_ui(self):
        """
        Update UI

        :return:
        """
        amount = self.application.amounts.get_amount(self.unit)
        self.senderBalanceValueLabel.setText(
            self.locale().toCurrencyString(
                amount.value(self.account.balance), amount.symbol()
            )
        )
        if self.fees is not None:
            self.feesValueLabel.setText(
                self.locale().toCurrencyString(amount.value(self.fees), amount.symbol())
            )
        else:
            self.feesValueLabel.setText("")

        if self.recipientNameOrAddressLineEdit.text().strip() != "":
            if self.recipient_account.balance is None:
                self.recipientBalanceValueLabel.setText(self._("Unknown!"))
                self.recipientBalanceValueLabel.setToolTip(
                    self._(
                        "Account balance unknown! Send only one unit and make sure the owner can get it"
                    )
                )
            else:
                self.recipientBalanceValueLabel.setText(
                    self.locale().toCurrencyString(
                        amount.value(self.recipient_account.balance), amount.symbol()
                    )
                )
                self.recipientBalanceValueLabel.setToolTip("")

    def init_units(self) -> None:
        """
        Init units combobox for transfer amount

        :return:
        """
        self.amountUnitComboBox.clear()

        for key, amount in self.application.amounts.register.items():
            self.amountUnitComboBox.addItem(amount.name(), userData=key)
        self.amountUnitComboBox.setCurrentIndex(
            self.amountUnitComboBox.findData(self.unit)
        )

    def _on_fees_button_clicked(self):
        """
        Triggered when user click on Fees button

        :return:
        """
        self.feesButton.setDisabled(True)
        self.loaderIconLabel.show()

        self.fetch_fees_from_network_async_qworker.start()

    def fetch_fees_from_network(self):
        """
        Fetch fees amount from network

        :return:
        """
        amount = self.application.amounts.get_amount(self.unit)
        # get value as blockchain units
        blockchain_value = amount.blockchain_value(self.amountDoubleSpinBox.value())
        self.fees = self.application.transfers.fees(
            self.account, self.recipient_account.address, blockchain_value
        )

    def _on_finished_fetch_fees_from_network(self):
        """
        Triggered when async request fetch_from_network is finished

        :return:
        """
        self.loaderIconLabel.hide()
        self.feesButton.setDisabled(False)
        self._update_ui()

    def _on_send_button_clicked(self):
        """
        Triggered when user click on Send button

        :return:
        """
        self.sendButton.setDisabled(True)
        self.loaderIconLabel.show()

        self.send_tranfer_to_network_async_qworker.start()

    def send_transfer_to_network(self):
        """
        Send transfer to network

        :return:
        """
        self.sendStatusLabel.setText("")
        # get value as blockchain units
        amount = self.application.amounts.get_amount(self.unit)
        blockchain_value = amount.blockchain_value(self.amountDoubleSpinBox.value())
        extrinsic_receipt = self.application.transfers.send(
            self.account, self.recipient_account.address, blockchain_value
        )
        if extrinsic_receipt is None:
            self.transfer_success = False
            self.sendStatusLabel.setStyleSheet("color: red;")
            self.sendStatusLabel.setText(
                self._("Transfer failed. Please check logs to understand why")
            )
        elif extrinsic_receipt.is_success is False:
            self.transfer_success = False
            self.sendStatusLabel.setStyleSheet("color: red;")
            self.sendStatusLabel.setText(
                self._(extrinsic_receipt.error_message["docs"][0])
            )
        else:
            self.transfer_success = True
            self.sendStatusLabel.setStyleSheet("color: green;")
            self.sendStatusLabel.setText(self._("Transfer done"))

    def _on_finished_send_transfer_to_network(self):
        """
        Triggered when async request send_transfer_to_network is finished

        :return:
        """
        self.loaderIconLabel.hide()
        self.sendButton.setDisabled(False)
        self.fetch_sender_balance_from_network_async_qworker.start()
        self.fetch_recipient_balance_from_network_async_qworker.start()


if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    application_ = Application(DATA_PATH)
    account_ = application_.accounts.get_by_address(
        "5E6taVoL7eW8qpPKjDcf3GjyvFkkMB8EHkkqZksiWeViEkSP"
    )
    if account_ is not None:
        application_.accounts.delete(account_)
    application_.accounts.create_new_root_account(
        "album cute glance oppose hub fury strategy health dust rebuild trophy magic",
        "en",
        "test account",
        "aaaaaa",
    )
    account_ = application_.accounts.get_by_address(
        "5E6taVoL7eW8qpPKjDcf3GjyvFkkMB8EHkkqZksiWeViEkSP"
    )
    if account_ is not None:
        account_.balance = 0
        TransferWindow(application_, account_, QMutex()).exec_()

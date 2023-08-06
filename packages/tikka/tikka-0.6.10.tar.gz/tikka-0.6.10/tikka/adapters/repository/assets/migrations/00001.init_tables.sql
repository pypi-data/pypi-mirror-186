create table if not exists currency(
    code_name varchar(255) unique primary key not null,
    name varchar(255),
    ss58_format integer,
    token_decimals integer default null,
    token_symbol varchar(255) default null,
    universal_dividend integer default null,
    monetary_mass integer default null,
    members_count integer default null
);

create table nodes (
        url varchar(255) primary key not null,
        peer_id varchar(255) default null,
        block integer default null,
        software varchar(255) default null,
        software_version varchar(255) default null
);

create table if not exists accounts(
        address varchar(255) unique primary key not null,
        name varchar(255),
        crypto_type integer default null,
        balance integer default null,
        identity_index integer,
        path varchar(255) default null,
        root varchar(255) default null,
        file_import integer default 0,
        category_id varchar(36) default null,
        FOREIGN KEY (root) REFERENCES accounts (address),
        FOREIGN KEY (category_id) REFERENCES categories (id)
);

create table if not exists wallets(
        address varchar(255) unique primary key not null,
        crypto_type integer,
        encrypted_private_key varchar(65535),
        encryption_nonce varchar(255),
        encryption_mac_tag varchar(255)
);

create table if not exists identities(
        index_ integer unique primary key not null,
        removable_on integer,
        next_creatable_on integer,
        status varchar(255)
);

create table if not exists tabs(
        id varchar(255) unique primary key not null,
        panel_class varchar(255) not null
);

create table if not exists preferences(
        key_ varchar(255) unique primary key not null,
        value_ varchar(65535)
);

create table if not exists categories(
        id varchar(36) unique primary key not null,
        name varchar(255),
        expanded integer default 1,
        parent_id varchar(36) default null,
        FOREIGN KEY (parent_id) REFERENCES categories (id)
);

create table if not exists passwords(
    root varchar(255) unique primary key not null,
    encrypted_password varchar(255),
    encryption_nonce varchar(255),
    encryption_mac_tag varchar(255)
);

-- PREFERENCES FIELDS
INSERT INTO preferences (key_, value_) VALUES ("selected_tab_page", NULL);
INSERT INTO preferences (key_, value_) VALUES ("wallet_load_default_directory", null);
INSERT INTO preferences (key_, value_) VALUES ("wallet_save_default_directory", null);
INSERT INTO preferences (key_, value_) VALUES ("current_entry_point_url", null);
INSERT INTO preferences (key_, value_) VALUES ("selected_unit", "unit");
INSERT INTO preferences (key_, value_) VALUES ("table_sort_column", null);
INSERT INTO preferences (key_, value_) VALUES ("table_sort_order", "ASC");
INSERT INTO preferences (key_, value_) VALUES ("table_category_filter", null);
INSERT INTO preferences (key_, value_) VALUES ("table_wallet_filter", null);

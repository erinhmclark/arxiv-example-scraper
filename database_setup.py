import mysql.connector
from settings import (MYSQL_DB_NAME, MYSQL_HOST,
                      MYSQL_USER, MYSQL_PASSWORD,
                      API_RESPONSE, AUTHORS_TABLE_NAME,
                      CATEGORIES_TABLE_NAME, LINKS)

CONN = mysql.connector.connect(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DB_NAME
)

CURSOR = CONN.cursor()


create_main_table_query = f"""
CREATE TABLE IF NOT EXISTS {API_RESPONSE} (
    entry_id VARCHAR(255) NOT NULL PRIMARY KEY,
    article_link VARCHAR(255),
    updated TIMESTAMP,
    published TIMESTAMP,
    title TEXT,
    summary TEXT,
    comment TEXT,
    journal_ref TEXT,
    doi VARCHAR(255),
    primary_category VARCHAR(255),
    pdf_url VARCHAR(255),
    raw_json JSON
);
"""
CURSOR.execute(create_main_table_query)

create_authors_table_query = f"""
CREATE TABLE IF NOT EXISTS {AUTHORS_TABLE_NAME} (
    entry_id VARCHAR(255),
    author VARCHAR(255),
    PRIMARY KEY (entry_id, author),
    FOREIGN KEY (entry_id) REFERENCES {API_RESPONSE}(entry_id)
);
"""
CURSOR.execute(create_authors_table_query)


create_categories_table_query = f"""
CREATE TABLE IF NOT EXISTS {CATEGORIES_TABLE_NAME} (
    entry_id VARCHAR(255),
    category VARCHAR(255),
    PRIMARY KEY (entry_id, category),
    FOREIGN KEY (entry_id) REFERENCES {API_RESPONSE}(entry_id)
);
"""
CURSOR.execute(create_categories_table_query)


create_links_table_query = f"""
CREATE TABLE IF NOT EXISTS {LINKS} (
    entry_id VARCHAR(255),
    link VARCHAR(255),
    content_type VARCHAR(255),
    title VARCHAR(255),
    rel VARCHAR(255),
    PRIMARY KEY (entry_id, link),
    FOREIGN KEY (entry_id) REFERENCES {API_RESPONSE}(entry_id));
"""
CURSOR.execute(create_links_table_query)


CONN.commit()
CONN.close()

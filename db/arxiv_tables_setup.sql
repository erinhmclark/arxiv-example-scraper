
CREATE TABLE IF NOT EXISTS arxiv_api (
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


CREATE TABLE IF NOT EXISTS arxiv_authors (
    entry_id VARCHAR(255),
    author VARCHAR(255),
    PRIMARY KEY (entry_id, author),
    FOREIGN KEY (entry_id) REFERENCES arxiv_api(entry_id)
);


CREATE TABLE IF NOT EXISTS arxiv_categories (
    entry_id VARCHAR(255),
    category VARCHAR(255),
    PRIMARY KEY (entry_id, category),
    FOREIGN KEY (entry_id) REFERENCES arxiv_api(entry_id)
);


CREATE TABLE IF NOT EXISTS arxiv_links (
    entry_id VARCHAR(255),
    link VARCHAR(255),
    content_type VARCHAR(255),
    title VARCHAR(255),
    rel VARCHAR(255),
    PRIMARY KEY (entry_id, link),
    FOREIGN KEY (entry_id) REFERENCES arxiv_api(entry_id)
    );


"""
Collect data from the ArXiv API using the package: https://pypi.org/project/arxiv/.
This script performs a simple extraction which inserts the response fields into a MySQL database.
"""
import json
from typing import Generator
import mysql.connector
import arxiv
from arxiv import Result
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from settings import MYSQL_DB_NAME, API_RESPONSE, SEARCH_QUERY, SEARCH_LIMIT, MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD


def establish_connection(user: str, password: str, host: str, db: str) -> MySQLConnection:
    """Establishes a MySQL connection and returns the connection object."""
    return mysql.connector.connect(user=user, password=password, host=host, database=db)


def get_cursor(connection: MySQLConnection) -> MySQLCursor:
    """Returns a cursor object using the connection object."""
    return connection.cursor()


def search_arxiv(search_query: str, limit: int = 15) -> Generator[Result, None, None]:
    """Performs a search on the ArXiv API and returns the results."""
    search = arxiv.Search(query=search_query, max_results=limit)
    return search.results()


def clean_result(result: Result) -> dict:
    """Cleans up the result object and returns it as a dictionary."""
    result_dict = vars(result)
    result_dict['article_link'] = result_dict['entry_id']
    result_dict['entry_id'] = result_dict['entry_id'].split('/')[-1]
    result_dict['_raw'] = json.dumps(result_dict['_raw'])
    return result_dict


def insert_into_db(cursor: MySQLCursor, result: dict) -> None:
    """Inserts the given result into the database using the provided cursor."""
    insert_query = f"""
    INSERT INTO {API_RESPONSE} (entry_id, article_link, updated, published, title, summary, comment, 
                                journal_ref, doi, primary_category, pdf_url, raw_json)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    article_link = VALUES(article_link),
    updated = VALUES(updated),
    published = VALUES(published),
    title = VALUES(title),
    summary = VALUES(summary),
    comment = VALUES(comment),
    journal_ref = VALUES(journal_ref),
    doi = VALUES(doi),
    primary_category = VALUES(primary_category),
    pdf_url = VALUES(pdf_url),
    raw_json = VALUES(raw_json)
    """
    cursor.execute(insert_query, (
        result['entry_id'], result['article_link'], result['updated'], result['published'], result['title'],
        result['summary'], result['comment'], result['journal_ref'], result['doi'], result['primary_category'],
        result['pdf_url'], result['_raw']))

    for author in result['authors']:
        cursor.execute("INSERT INTO arxiv_authors (entry_id, author) VALUES (%s, %s)",
                       (result['entry_id'], author.name))

    for category in result['categories']:
        cursor.execute("INSERT INTO arxiv_categories (entry_id, category) VALUES (%s, %s)",
                       (result['entry_id'], category))

    for link in result['links']:
        cursor.execute("INSERT INTO arxiv_links (entry_id, link, content_type, title, rel) VALUES (%s, %s, %s, %s, %s)",
                       (result['entry_id'], link.href, link.content_type, link.title, link.rel))


def main() -> None:
    """Main function to search ArXiv API, clean results and insert into the database."""
    connection = establish_connection(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB_NAME)
    cursor = get_cursor(connection)
    results = search_arxiv(SEARCH_QUERY, limit=SEARCH_LIMIT)
    results_list = [clean_result(result) for result in results]

    for result in results_list:
        insert_into_db(cursor, result)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()

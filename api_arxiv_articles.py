"""Collect data from the ArXiv API using the package: https://pypi.org/project/arxiv/.
   Simple extraction which inserts the response fields into a SQLite database.
"""
import sqlite_utils
import arxiv
from settings import DB_NAME, API_TABLE_NAME, SEARCH_QUERY, SEARCH_LIMIT


db = sqlite_utils.Database(DB_NAME)
table = db[API_TABLE_NAME]


def search_arxiv(search_query: str, limit: int = 15):
    """Search the ArXiv API and return the results.
    """
    search = arxiv.Search(
        query=search_query,
        max_results=limit
    )
    return search.results()


def main():
    results = search_arxiv(SEARCH_QUERY, limit=SEARCH_LIMIT)
    results_list = [result.__dict__ for result in results]
    table.upsert_all(results_list, pk='entry_id')


if __name__ == '__main__':
    main()

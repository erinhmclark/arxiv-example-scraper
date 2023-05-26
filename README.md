# arxiv-example-scraper

This repository contains a Python script for extracting data from the ArXiv API and storing the response in a MySQL database. 
The script uses the Python package [arxiv](https://pypi.org/project/arxiv/) to interact with the arXiv API.

## Installation

This project used a [Poetry](https://python-poetry.org/) environment to store the dependencies.
Follow the documentation to install this if needed, and the use the following command to install the environment:

``` bash
cd arxiv-example-scraper
poetry init
```

## Usage

Set up a MySQL database and create a .env file with the credentials added to the variables given in the .env.template file.

Run the database setup script:

```
python database_setup.py
```

Modify any options that you want to in the file `settings.py`. 
For example change the variable `SEARCH_QUERY` to search for another string.

Run the main script:
```
python api_arxiv_articles.py
```


## Extensions

- Create a Docker image for the scraper
- Run this on a remote server
- Schedule this to run at regular time intervals
- Add an alert system such as email or slack
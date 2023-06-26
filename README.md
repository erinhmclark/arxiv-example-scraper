# arxiv-example-scraper

This repository contains a Python script for extracting data from the ArXiv API and storing the response in a MySQL database. 
The script uses the Python package [arxiv](https://pypi.org/project/arxiv/) to interact with the arXiv API.


# Installation

## Python MySQL Scraper with Docker Compose

This is a Python application designed to scrape data and insert it into a MySQL database. 
Docker Compose is used to orchestrate the application and database containers.


### Setup

1. Clone this repository.

    ```
    gh repo clone erinhmclark/arxiv-example-scraper
    ```

2. Navigate to the repository directory.

    ```
    cd repo
    ```

3. Set the required environment variables for the MySQL database in the `.env` file:

    ```
    MYSQL_ROOT_PASSWORD=yourpassword
    MYSQL_ARXIV_USER=youruser
    MYSQL_ARXIV_PASSWORD=yourpassword
    ```

## Running the Application Docker Compose

### Requirements

- Docker
- Docker Compose

First, start up the database service:

```shell
docker-compose up --build -d
```


## Querying the MySQL Database

Once the MySQL container is up and running, you can use the `mysql` command-line client to interact with your database. First, you'll need to get the ID of the running MySQL container:

```shell
docker ps
```

Then, you can use the `docker exec` command to start a `mysql` client session:

```shell
docker exec -it <CONTAINER_ID> mysql -u <username> -p
```
Or using the database name:
```shell
docker exec -it db mysql -u <username> -p
```

Replace `<username>` with the MySQL user name. Enter the password when prompted.

## Debugging

If you're encountering issues with the Docker images not updating with your changes, you can force Docker Compose to rebuild the images:

```shell
docker-compose up --build --no-cache
```


## Cleanup

To stop and remove the containers, networks, and volumes defined in your `docker-compose.yml` file, run the `down` command:

```shell
docker-compose down
```

Add the -v option to also delete your volumes:
```shell
docker-compose down -v
```

## Local Installation

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

- Create scrapers and run benchmarks to compare efficiency
  - Using the requests module
  - Using automation such as Selenium
  - Using ScraPy
- Dockerize the process
  - Dockerfile for MySQL database, modify database_setup python file to SQL file to be 
  - Docker compose file to connect script and database containers
- Schedule trigger for scraper

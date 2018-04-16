# Top40 Scraper
For a given month/year range, create a list of all songs that have appeared on Billboard's Hot 100 for that time range, sorted by the number of weeks each song appeared on the list. Results are written to the file output.txt

## How to use:

1. Install Python3 and VirtualEnv
2. Run the following code

## Setup code
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the app
```
python3 main.py [start_year] [start_month] [end_year] [end_month]
```
Leaving any argument blank will default to the current year/month

## Running tests
```
python3 tests.py
```

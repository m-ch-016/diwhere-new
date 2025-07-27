# DIWhere

## Introduction

DIWhere is a search engine for comparing products and pricing from the UKs leading DIY suppliers.

## Setup

```
flask db init && flask db migrate && flask db upgrade
```

## Todo

- turn webscraping and retrieval into a script
- script should write to a CSV file all of the products that are found

1. run script
2. note the current time
3. for each retrieved product, save that time as its retrieval time

- id, name, link, image, source, retrievalTime
- each product is a row in a CSV file generated from the webscraping


## Authors

Muhammed Chaudhary, Ibrahim Qasim



# DevToScraper

[Dev.to](https://dev.to/) Blog Scraper

## Introduction

DevToScraper is a Python tool designed with Scrapy library to scrape blog content from the [dev.to](https://dev.to/) platform. It provides
an easy way to extract blog posts and their metadata for analysis, archiving, or other purposes.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Reza-Nonva/DevToScrapper.git
```

2. Navigate to the project directory and install the required dependencies:
```bash
cd DevToScrapper/
pip3 install -r requirements.txt
```
## Usage
run this commands to start spider
```bash
cd devto/
scrapy crawl devto_spider
```
## Tips
1. you can set depth of crawling in devto_spider.py ``` max_depth = 5 (default)```

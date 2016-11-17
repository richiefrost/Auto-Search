#!/bin/bash
echo "Starting data read"
echo $(($(date +'%s * 1000 + %-N / 1000000')))
scrapy crawl auto_search -t jsonlines -o data-withlog.json
echo $(($(date +'%s * 1000 + %-N / 1000000')))
echo "Data read finished"
#!/usr/bin/env bash

cat name.txt | while read line
do
   instagram-scraper $line -u mingmingyang2 -p yang6757383575
done

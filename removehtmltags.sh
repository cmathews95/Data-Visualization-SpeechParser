#!/bin/bash
#Use this script to remove html tags, but not add space.
sed 's/<[^>]*>//g'

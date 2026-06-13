#!/bin/sh

pycacheDirs=$(find .. -maxdepth 4 -name "__pycache__" -type d)

echo $pycacheDirs
rm -r $pycacheDirs
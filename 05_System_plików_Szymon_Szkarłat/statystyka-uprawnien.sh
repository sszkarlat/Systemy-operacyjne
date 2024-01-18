#!/bin/bash

ls -la | grep "^-" | cut -d" " -f1 | sort | uniq -c | sort -rn | awk '{print $1, $2}'


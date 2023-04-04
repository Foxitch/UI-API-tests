#!/bin/bash

echo "API tests started"

result=$(python3 pytest "$1" --tb=no --alluredir=allure-results | grep -o "FAILED\|ERROR" | wc -l)

if [ "$result" -eq 0 ]
then
    echo "Tests finished without errors"
else
    echo "Tests finished with $result errors"
fi

echo "API tests finished"
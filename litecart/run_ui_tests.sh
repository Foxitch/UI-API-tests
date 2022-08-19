#!/bin/sh

echo "tests started"

result=`python3.10 pytest $1 --tb=no --alluredir=allure-results | grep -o "FAILED\|ERROR" | wc -l`

if [ $result -eq 0 ]
then
    curl -d "text=Tests finished without errors"
else
    curl -d "text=Tests finished with $result errors"
fi
echo "tests finished"
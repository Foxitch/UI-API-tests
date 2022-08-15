#!/bin/sh

oauth_slack_token=`printenv SLACK_TOKEN`
proto=`printenv PROTO`
hostname=`printenv HOSTNAME`
username=`printenv USERNAME`
password=`printenv PASSWORD`

date=`date '+%Y:%m:%d:%H:%M:%S'`

reports_dir="reports"

if ! [ -d ./$reports_dir/ ]; then
mkdir $reports_dir
fi

echo "tests started"

result=`python3.10 pytest $1/tests --proto=$proto --url=$hostname --username=$username\
 --password=$password --tb=no --allure-dir=reports/report_$date.html\
 --self-contained-html | grep -o "FAILED\|ERROR" | wc -l`

if [ $result -eq 0 ]
then
    curl -d "text=Tests finished without errors" -d "channel=#pipeline-aipix-control-center" -H "Authorization: Bearer $oauth_slack_token" -X POST https://slack.com/api/chat.postMessage
else
    curl -d "text=Tests finished with $result errors" -d "channel=#pipeline-aipix-control-center" -H "Authorization: Bearer $oauth_slack_token" -X POST https://slack.com/api/chat.postMessage
fi
echo "tests finished"
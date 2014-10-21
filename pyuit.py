#!/usr/bin/env python

from Controllers import RunUITests
import sys, json
import time

# Run tests using firefox or phantomjs
run_using_browser = "firefox"
retries = 0
max_retries_if_phantomjs_fails = 4
sleep_before_retrying = 3 # seconds
# Read rules as json from stdin and run UITests
data = sys.stdin.read()

while(True):
    try:
        # Get rules from stdin in json format on server
        rules = json.loads(data)
        test = RunUITests(rules)
        test.run_ui_tests(run_using_browser)
        break       
    except Exception, e:
        # If phantomjs crashes it throws an exception containing string "ghostdriver" we retry
        if str(e).lower().find("ghostdriver") >= 0 and (retries <= max_retries_if_phantomjs_fails):
            time.sleep(sleep_before_retrying)
            retries += 1
            continue
        raise e
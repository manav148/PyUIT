from Controllers import RunUITests
import sys, json
import time

retries = 0
max_retries_if_ghost_driver_fails = 4
# Read data once since its reading from stdin
data = sys.stdin.read()
while(True):
	try:
		# Get rules from stdin in json format on server
		rules = json.loads(data)
		test = RunUITests(rules)
		test.run_ui_tests("phantomjs")

		# Get rules from test file if running locally
		
		break		
	except Exception, e:
		# If ghost driver initializing is the reason for the script failure restart
		if str(e).lower().find("ghostdriver") >= 0 and (retries <= max_retries_if_ghost_driver_fails):
			time.sleep(3)
			retries += 1
			continue
		raise e
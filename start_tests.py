from Controllers import RunUITests
import sys, json
import time

retries = 0
max_retries_if_ghost_driver_fails = 4
# Read rules as json from stdin and run UITests
data = sys.stdin.read()
while(True):
	try:
		# Get rules from stdin in json format on server
		rules = json.loads(data)
		test = RunUITests(rules)
		# Run tests using phantomjs 
		test.run_ui_tests("phantomjs")
		# Run tests using firefox browser
		# test.run_ui_tests("firefox")
		break		
	except Exception, e:
		# If ghost driver initializing is the reason for the script failure restart
		if str(e).lower().find("ghostdriver") >= 0 and (retries <= max_retries_if_ghost_driver_fails):
			time.sleep(3)
			retries += 1
			continue
		raise e
PyUIT
=====

A UI Test Framework using Python, Selenium and Phantomjs/FireFox driver.(Alpha)

Requirements:

<b>Selenium:</b> ```pip install selenium``` 


<b>Phantomjs:</b> http://phantomjs.org/download.html (<i>Recommended if we can't afford GUI on the server.</i>)

<b>Firefox:</b> https://www.mozilla.org/en-US/firefox/new/ (<i>Recommended if we can afford GUI on the server.</i>)

<b>Usage:</b> ```cat SampleRules/rules.json | python pyuit.py```

Where rules.json is an input json file which governs UITests<br>
(Checkout SampleRules/rules.json)
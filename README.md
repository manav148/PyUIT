PyUIT
=====

A UI Test Framework using Python, Selenium and Phantomjs/FireFox driver.(Alpha)

Requirements:

<b>Selenium:</b> ```pip install selenium``` 


<b>Phantomjs:</b> http://phantomjs.org/download.html (<i>Install only if we don't have GUI installed on server.</i>)

<b>Firefox:</b> https://www.mozilla.org/en-US/firefox/new/ (<i>Install if we have GUI installed on server.</i>)

<b>Usage:</b> ```cat SampleRules/rules.json | python pyuit.py```

Where rules.json is an input json file which governs UITests<br>
(Checkout SampleRules/rules.json)
### selenium-shortcuts
Shortcut functions for Python selenium

Installation:
`pip install selenium-shortcuts`

Usage:
```
from selenium_shortcuts import setup_shortcuts

helper = setup_shortcuts(browser='uc') # Start a browser on port 9222 or reconnect to existing browser on port 9222 with undetected-chromedriver
driver, find, finds, click, text, send, get, check = helper.driver, helper.find, helper.finds, helper.click, helper.text, helper.send, helper.get, helper.check

info = text('#info')
print(info)

click('#submit')

info = find('#info')
print(info.text)
info.click()

items = finds('.items')
for item in items:
	print(item.text)

info, classes = find('#info', attribute='class')
print(classes)
```

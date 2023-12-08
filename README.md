# playwright-cicd-demo
Playwright/Pytest/Python integration with CI/CI using git actions

Goals:
- [x] create simple website check test
- [x] create data structure to hold test data
- [x] manage page locators and functions using page object model
- [x] add a test fixture to turn on trace logging
- [x] integrate with ci/cd using git actions
- [x] run tests on push to master

## Requirements 
- Python 3.12
- pip
- playwright
- pytest
- pytest-playwright plugin

## Setup
- Install Python3.x and pip 
- Virtual Env Setup
  - `python3.x -m venv venv`
  - `source venv/bin/activate`
  - `deactivate` to exit
- Upgrade pip
  - `pip install --upgrade pip`
- Install playwright
  - `pip install playwright` 
- Install Chromium
- `playwright install chromium`
- Install pytest
  - `pip install pytest`
- Install pytest-playwright
  - `pip install pytest-playwright`




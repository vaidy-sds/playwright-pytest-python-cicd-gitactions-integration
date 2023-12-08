# playwright-cicd-demo
Playwright/Pytest/Python integration with CI/CI using git actions

Goals:
- [x] create simple website check test
- [x] create data structure to hold test data
- [x] manage page locators and functions using page object model
- [x] add a test fixture to turn on trace logging
- [x] integrate with ci/cd using git actions
- [x] run tests on push to master

## Setup
- Install Python3.x and pip 
- Setup virtual environment
  - `python3.12 -m venv venv`'
  - `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install pytest`
- `pip install pytest-playwright`
- `playwright install`

## Run Tests
- `python -m pytest tests`



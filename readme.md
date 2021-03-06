# Wetheria
A Flask Application to fetch weather information from External API

## Project Folders Structure
```
├───requirements
│       base.txt
│       develop.txt
│       production.txt
│
├───weather
│   │   constants.py
│   │   resources.py
│   │   utils.py
│   │
│   ├───tests
│   │   │   constants.py
│   │   │   test_resources.py
│   │   │   test_utils.py
│   │   │
│   │   └───__init__.py
│   └───__init__.py
├───wetheria
│   │   app.py
│   │   extensions.py
│   │   handlers.py
│   │   middlewares.py
│   │   settings.py
│   │   settings_local_example.py
│   │
│   └───__init__.py
```

## System Configuration

###  For local configuration

1. Create virtual environment.

2. Install Python library requirements (pip install -r requirements/devel.txt).

3. Configure settings_local.py; 

   1. Copy template "settings_local_example.py" to create a file named "settings_local.py".
   2. If you want to update the API Key used on the third party API, please do it over settings_local.py file.

4. Run the command "flask run" in order to make available flask service

5. Enjoy it!

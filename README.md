# Notes

- I choose command line option from newrelic. Its easy and straight forward.
- There are multiple routes in the app. test3 and test4 should throw errors.


### Steps:
    - Get the license key from newrelic interface

    - Generate newrelic config
        - newrelic-admin generate-config <your-key-goes-here> newrelic.ini

    - Run python program
        - NEW_RELIC_CONFIG_FILE=newlic.ini newrelic-admin run-python run_app.py

    - Click "Listen to my application"


from flask import Flask, request
from src.switcher import MonitorSwitcher

# Initialise the MonitorSwitcher object
ms = MonitorSwitcher()

# Create the Flask app
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    # Get the integer parameter from the request
    num = int(request.form['num'])

    # Return the result and process the request
    if num == 0:
        result = 'Switching show only to next monitor...'
        ms.switch(num)
    elif num in {1, 2}:
        result = f'Switching to show only on monitor {num}...'
        ms.switch(num)
    else:
        result = 'Invalid number! Number should be 0, 1 or 2.'
    return result

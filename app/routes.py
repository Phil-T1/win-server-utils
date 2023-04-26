from flask import Flask, request, abort
from src.switcher import MonitorSwitcher

# Initialise the MonitorSwitcher object
ms = MonitorSwitcher()

# Create the Flask app
app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_request():
    '''Endpoint routes the request to the correct function.'''
    try:
        # Get the integer parameter from the request
        mon_id = int(request.json['mon_id'])

        # Return the result and process the request
        if mon_id == 0:
            result = 'Switching show only to next monitor...'
            ms.switch(mon_id)
        elif mon_id in {1, 2}:
            result = f'Switching to show only on monitor {mon_id}...'
            ms.switch(mon_id)
        # If the monitor ID is invalid, return a 404 error
        else:
            abort(404, description='Invalid monitor ID.')

    # Return a 404 error if the request is invalid
    except KeyError:
        abort(404, description='Error!')

    # Return the result
    return result
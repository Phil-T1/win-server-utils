from flask import Flask, request, abort
from src.switcher import MonitorSwitcher

# Initialise the MonitorSwitcher object
ms = MonitorSwitcher()

# Create the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def process_request():
    '''Endpoint routes the request to the correct function.'''

    # Get the integer parameter from the request
    mon_id = request.args.get('id')

    # ID number not passed then return a 200 response (ping check)
    if mon_id is None:
        return ('Okay', 200)
    
    try:
        # Else onvert the ID to an integer and process
        mon_id = int(mon_id)

        # Return the result and process the request
        if mon_id == 0:
            response = ('Switching show only to next monitor...', 200)
            ms.switch(mon_id)
        elif mon_id in {1, 2}:
            response = (f'Switching to show only on monitor {mon_id}...', 200)
            ms.switch(mon_id)
        # If the monitor ID is invalid, return a 404 error
        else:
            response= ('Invalid ID.', 403)
    except Exception:
        # Return a 404 error if the request is invalid
        response = ('Request error!', 404)
    finally:
        # Return response
        return response

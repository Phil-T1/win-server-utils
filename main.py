from app.routes import app as flask_app

# Launch the Flask app
if __name__ == '__main__':
    flask_app.run(debug=False, host='0.0.0.0', port=6999)

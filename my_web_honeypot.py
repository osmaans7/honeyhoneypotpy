# Libraries
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for

# Logging Format
logging_format = logging.Formatter('%(asctime)s %(message)s')

# HTTP Logger
http_logger = logging.getLogger('HTTP Logger')
http_logger.setLevel(logging.INFO)
http_handler = RotatingFileHandler('http_audits.log', maxBytes=2000, backupCount=5)
http_handler.setFormatter(logging_format)
http_logger.addHandler(http_handler)

# Baseline honeypot

def my_web_honeypot(input_username="admin", input_password="password"):
    
    app = Flask(__name__)

    @app.route('/')

    def index():
        return render_template('wp-admin.html')
    
    @app.route('/wp-admin-login', methods=['POST'])

    def login():
        username = request.form['username']
        password = request.form['password']

        ip_address = request.remote_addr

        http_logger.info(f'Client with IP Address: {ip_address} entered\n Username: {username}, Password: {password}')

        if username == input_username and password == input_password:
            return 'OHMYGOD!'
        else:
            return "Invalid username or password. Please Try Again."
        
    return app

def run_my_web_honeypot(port=5000, input_username="admin", input_password="password"):
    run_my_web_honeypot_app = my_web_honeypot(input_username, input_password)
    run_my_web_honeypot_app.run(debug=True, port=port, host="0.0.0.0")

    return run_my_web_honeypot_app

from flask import Flask
import urllib.parse
import os
from dotenv import load_dotenv
import logging
from models.proverbs import db
from api.v1.endpoints import proverbs_blueprint

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the Database credentials from the environment variable.
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
print("password: ", db_password)
db_host = os.getenv('DB_HOST')
print("db_host: ", db_host)
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Configure the Flask logger
handler = logging.FileHandler('app.log')  # Create a file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s\n')
handler.setFormatter(formatter)  # Assign the formatter to the handler
app.logger.addHandler(handler)  # Add the handler to the Flask logger
app.logger.setLevel(logging.DEBUG)


# URL-encode the password
encoded_password = urllib.parse.quote_plus(db_password)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_username}:{encoded_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Register API blueprints
app.register_blueprint(proverbs_blueprint)

# Create all tables based on the defined models
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
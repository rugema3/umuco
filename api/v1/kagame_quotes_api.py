from flask import Blueprint, request, jsonify
from models.umurage import db, KagameQuote
from flask import current_app as app

kagame_blueprint = Blueprint('kagame_quote', __name__)

"""
@kagame_blueprint.route('/api/v1/insert_quote', methods=['POST'])
def insert_quote():
    Insert a new quote.

    This endpoint allows the insertion of a new quote by providing the 
    quote in the request body.

    Request JSON Parameters:
    - quote: The text of the quote (required)
    
    Returns:
    - 201 Created: If the quote is created successfully.
    - 400 Bad Request: If the request body is missing required parameters or contains invalid data.
    - 500 Internal Server Error: If an unexpected error occurs during proverb creation.
    
    # Parse request data
    data = request.json
    quote = data.get('quote')
   
    # Validate request data
    if not quote:
        return jsonify({'error': 'Quote text is required'}), 400

    # Create a new proverb object
    new_quote = KagameQuote(quote=quote)

    # Insert the proverb into the database
    try:
        new_quote.insert()
        return jsonify({'message': 'quote created successfully', 'quote': new_quote.serialize()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
""" 

@kagame_blueprint.route('/api/v1/get_kagame_quotes', methods=['GET'])
def get_quotes():
    """
    Retrieves all quotes and returns them as a JSON response.

    Returns:
          JSON response:
          - On success: Contains a list of serialized Kagame quotes (200 OK).
          - On data retrieval error: Error message indicating "No quotes found" (404 Not Found).
          - On other errors: Generic error message (500 Internal Server Error).
    """

    try:
        # Query the database to retrieve all proverbs
        quotes = KagameQuote.query.all()

        app.logger.info("Quotes queried successfully.")

        if not quotes:
            # Handle empty quote list (potential 404)
            return jsonify({'error': 'No quotes found'}), 404

        try:
            # Serialize the quotes into JSON format with detailed error handling
            serialized_quotes = [quote.serialize() for quote in quotes]
            app.logger.info("Serialization successful.")
            return jsonify(serialized_quotes), 200

        except Exception as e:
            # Log detailed serialization error information
            app.logger.error("Serialization failed: %s (%s)", e, type(e))
            message = f"OOPS!! Serialization failed"
            return jsonify({'error': message}), 500

    except Exception as e:
        # Log generic data retrieval error information
        app.logger.error("Failed to retrieve Kagame quotes: %s (%s)", e, type(e))
        return jsonify({'error': 'Internal server error'}), 500


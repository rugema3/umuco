from flask import Blueprint, request, jsonify
from models.proverbs import Proverb, db

proverbs_blueprint = Blueprint('proverbs', __name__)

@proverbs_blueprint.route('/api/v1/insert_proverbs', methods=['POST'])
def insert_proverb():
    """
    Insert a new proverb.

    This endpoint allows the insertion of a new proverb by providing the 
    proverb text, category, translation, and explanation in the request body.

    Request JSON Parameters:
    - proverb: The text of the proverb (required)
    - category: The category of the proverb
    - translation: The English translation of the proverb
    - explanation: An explanation or interpretation of the proverb

    Returns:
    - 201 Created: If the proverb is created successfully.
    - 400 Bad Request: If the request body is missing required parameters or contains invalid data.
    - 500 Internal Server Error: If an unexpected error occurs during proverb creation.
    """
    # Parse request data
    data = request.json
    proverb = data.get('proverb')
    category = data.get('category')
    translation = data.get('translation')
    explanation = data.get('explanation')

    # Validate request data
    if not proverb:
        return jsonify({'error': 'Proverb text is required'}), 400

    # Create a new proverb object
    new_proverb = Proverb(proverb=proverb, category=category, translation=translation, explanation=explanation)

    # Insert the proverb into the database
    try:
        new_proverb.insert()
        return jsonify({'message': 'Proverb created successfully', 'proverb': new_proverb.serialize()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@proverbs_blueprint.route('/api/v1/get_proverbs', methods=['GET'])
def get_proverbs():
    """
    Retrieve all proverbs from the database.

    Returns:
    - JSON response containing all proverbs.
    """
    # Query the database to retrieve all proverbs
    proverbs = Proverb.query.all()

    # Serialize the proverbs into JSON format
    serialized_proverbs = [proverb.serialize() for proverb in proverbs]

    # Return the JSON response
    return jsonify(serialized_proverbs), 200
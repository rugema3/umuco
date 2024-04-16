from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proverb(db.Model):
    """
    Represents a proverb in the database.

    Attributes:
    - id: The unique identifier of the proverb.
    - proverb: The text of the proverb.
    - category: The category of the proverb.
    - translation: The English translation of the proverb.
    - explanation: An explanation or interpretation of the proverb.
    """

    id = db.Column(db.Integer, primary_key=True)
    proverb = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    translation = db.Column(db.Text)
    explanation = db.Column(db.Text)
    
    def insert(self):
        """
        Insert the proverb into the database.

        This method adds the current instance of the proverb to the db session
        and commits the session to save the changes.
        """
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        """
        Serialize the Proverb object into a dictionary representation.

        Returns:
            dict: A dictionary containing the serialized representation of the Proverb object.
        """
        return {
            'id': self.id,
            'proverb': self.proverb,
            'category': self.category,
            'translation': self.translation,
            'explanation': self.explanation
        }
    
class KagameQuote(db.Model):
    """
    Represents a quote by President Kagame in the database.

    Attributes:
    - id: The unique identifier of the quote.
    - quote: The text of the quote attributed to President Kagame.
    """

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.Text, nullable=False)

    def serialize(self):
        """
        Serialize the KagameQuote object into a dictionary representation.

        Returns:
            dict: A dictionary containing the serialized representation of the
                    KagameQuote object.
        """
        return {
            'id': self.id,
            'quote': self.quote
        }
    def insert(self):
        """
        Insert a quote into the database.

        This method adds the current instance of the KagameQuote to the db 
        session and commits the session to save the changes.
        """
        db.session.add(self)
        db.session.commit()

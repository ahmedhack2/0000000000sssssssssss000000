from .extensions import db

class bot_conversion(db.Model):
    massage = db.Column(db.String(50) , unique = True)
    response = db.Column(db.String(50) , unique = True)

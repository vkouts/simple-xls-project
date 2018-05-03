from app import db
from datetime import datetime


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), nullable=True)
    profile = db.Column(db.String(512), nullable=True)
    photo = db.Column(db.String(512), nullable=True)

    def __repr__(self):
        return '<Record {}>'.format(self.name) 
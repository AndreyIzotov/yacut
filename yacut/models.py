from datetime import datetime

from flask import url_for

from yacut import db
from .constants import FIELD_NAMES


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def from_dict(self, data):
        for field_db, field_inp in FIELD_NAMES.items():
            if field_inp in data:
                setattr(self, field_db, data[field_inp])

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('index_view', _external=True) + self.short
        )

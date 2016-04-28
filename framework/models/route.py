"""Key (parent) => value (path) for directing URLs."""

from ..extensions import db
from .template import Template


class Route(db.Model):
    """TODO."""

    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False)
    parent = db.Column(db.Integer, nullable=False)

    @property
    def child(self):
        """TODO."""

        return Template.query.filter_by(parent=self.id).first()

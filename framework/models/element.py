"""HTML-tag with hierarchy and inheritance."""

from ..extensions import db


class Element(db.Model):
    __tablename__ = 'elements'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(255), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    template = db.Column(db.Integer, nullable=False)
    parent = db.Column(db.Integer, nullable=True)

    @property
    def children(self):
        return Element.query.filter_by(parent=self.id).all()

    @property
    def attribute_dict(self):
        d = {}
        attributes = Attribute.query.filter_by(parent=self.id).all()
        for attribute in attributes:
            d[attribute.key] = attribute.value
        return d

    def __repr__(self):
        return '<{}>'.format(self.tag)
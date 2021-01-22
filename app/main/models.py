from app import db


class Animal(db.Model):
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    feeds = db.relationship('Feed', backref='animal', lazy=True)


class Brand(db.Model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Feed(db.Model):
    __tablename__ = "feeds"
    sku = db.Column(db.String(12), unique=True, nullable=False, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=True)
    name = db.Column(db.String, nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)

    description = db.Column(db.TEXT, nullable=False)
    image_url = db.Column(db.String(240), nullable=False)
    purchase_link = db.Column(db.String(240), nullable=False)
    price_range = db.Column(db.String(240), nullable=False)

    min_weight = db.Column(db.Integer, nullable=False)
    max_weight = db.Column(db.Integer, nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    max_age = db.Column(db.Integer, nullable=False)

    allergies = db.Column(db.String(240))
    health_issues = db.Column(db.String(240))

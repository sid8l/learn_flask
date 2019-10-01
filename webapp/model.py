from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False, unique=True)
    published = db.Columnt(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)

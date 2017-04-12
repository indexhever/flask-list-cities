from app import db

class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String(50), unique=True)

    def __init__(self, cityname=None):
        self.cityname = cityname

    def __repr__(self):
        return '<City %r>' % (self.cityname)

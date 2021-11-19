from app import db
from sqlalchemy.dialects.postgresql import JSON


class NetworkDevices(db.Model):
    __tablename__ = 'NetworkDevices'

    id = db.Column(db.Integer, primary_key=True)
    mac_address = db.Column(db.String())
    status_all = db.Column(db.String())
    ip_address = db.Column(db.String())

    def __init__(self, mac_address, status_all, ip_address):
        self.mac_address = mac_address
        self.status_all = status_all
        self.ip_address = ip_address

    def __repr__(self):
        return '<id {}>'.format(self.id)
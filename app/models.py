from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import uuid


class BasicColumn(db.Model):
    __abstract__ = True

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)


class User(BasicColumn):
    __tablename__ = 'users'

    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def compare_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Contact(BasicColumn):
    __tablename__ = 'contacts'

    name = db.Column(db.String(35), nullable=False)
    cellphone = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name, cellphone) -> None:
        self.name = name
        self.cellphone = cellphone

    def __repr__(self):
        return f'<Contact {self.name}>'

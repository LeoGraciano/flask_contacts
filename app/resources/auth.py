from datetime import datetime, timedelta
import json
from app.utils.convert import JSONEncoder
from flask import current_app
from flask_restful import Resource, marshal
import jwt

from app import db, request
from app.models import User
from app.schemas import user_fields


class Login(Resource):
    def post(self):
        payload = request.only(['email', 'password'])
        email = payload['email']
        password = payload['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.compare_password(password):
            return {'message': 'Usuário não existe'}, 404

        data = {
            "id": user.id,
            "exp": datetime.now() + timedelta(hours=1)
        }

        token = jwt.encode(data, current_app.config['SECRET_KEY'])

        return {'access_token': token}


class Register(Resource):
    def post(self):
        payload = request.only(['email', 'password'])

        email = payload['email']
        password = payload['password']

        user = User(email, password)

        db.session.add(user)
        db.session.commit()

        return marshal(user, user_fields, 'user')

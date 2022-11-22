from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models import User


def jwt_required(f):
    def decorator(*args, **kwargs):
        token = None

        if "authorization" in request.headers:
            token = request.headers.get("authorization")

        if not token:
            return {'error': "Você não tem permissão para acessar essa rota"}, 401

        if not "Bearer" in token:
            return {'error': "Token é inválido"}, 401

        try:
            token_pure = token.replace("Bearer ", "")
            decode = jwt.decode(
                token_pure, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(decode['id'])
        except Exception as e:
            return {'error': "Token invalido"}, 403

        return f(current_user=current_user, *args, **kwargs)

    return decorator

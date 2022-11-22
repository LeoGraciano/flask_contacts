from flask_restful import fields

contact_fields = {
    "id": fields.String,
    "name": fields.String,
    "cellphone": fields.String,
}


user_fields = {
    "id": fields.String,
    "email": fields.String,
    # "password": fields.String,
}

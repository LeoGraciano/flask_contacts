from flask_restful import Resource, marshal
from app.decorator import jwt_required

from app.models import Contact
from app import request, db
from app.schemas import contact_fields


class Contacts(Resource):
    @jwt_required
    def get(self, current_user):
        contacts = Contact.query.all()
        return marshal(contacts, contact_fields, 'contacts')

    @jwt_required
    def post(self, current_user):
        payload = request.only(['name', 'cellphone'])

        name = payload['name']
        cellphone = payload['cellphone']

        contact = Contact(name=name, cellphone=cellphone)
        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_fields, 'contact')

    @jwt_required
    def put(self, current_user):
        payload = request.only(['id', 'name', 'cellphone'])
        _id = payload['id']
        name = payload['name']
        cellphone = payload['cellphone']

        contact = Contact.query.get(_id)
        if not contact:
            return {'message': "Contato não existe"}, 404

        contact.name = name
        contact.cellphone = cellphone

        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_fields, 'contact')

    @jwt_required
    def delete(self, current_user):
        payload = request.only(['id'])
        _id = payload['id']
        contact = Contact.query.get(_id)

        if contact is None:
            return {'message': "Contato não existe"}, 404

        db.session.delete(contact)
        db.session.commit()

        return marshal(contact, contact_fields, 'contact')

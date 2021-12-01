import uuid
from db.models import Type
from db.base import db_session

class TypeService:
    
    
    @staticmethod
    def find():
        return Type.query.all()


    @staticmethod
    def get(id):
        return Type.query.filter_by(id=id).first()


    @staticmethod
    def remove(id):
        type_model = Type.query.filter_by(id=id).first()
        db_session.delete(type_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, slug, label):
        if id == 'None':
            type_model = Type()
            is_edit = False
        else:
            type_model = TypeService.get(id)
            is_edit = True

        if(len(slug) < 3):
            return dict(
                is_edit = is_edit,
                message = 'Минимальная длина slug 3 символа'
            )

        if(len(label) < 3):
            return dict(
                is_edit = is_edit,
                message = 'Минимальная длина label 3 символа'
            )

        type_model.slug = slug
        type_model.label = label

        db_session.add(type_model)
        db_session.commit()

        return False
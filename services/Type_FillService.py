from db.models import Type_Fill
from db.base import db_session

class Type_FillService:
    
    
    @staticmethod
    def find():
        return Type_Fill.query.all()


    @staticmethod
    def get(id):
        return Type_Fill.query.filter_by(id=id).first()

    @staticmethod
    def get_by_type(type_id):
        return Type_Fill.query.filter_by(type_id=type_id).all()


    @staticmethod
    def remove(id):
        type_fill_model = Type_FillService.get(id)
        db_session.delete(type_fill_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, type_id, fill_id):
        if id == 'None':
            type_fill_model = Type_Fill()
        else:
            type_fill_model = Type_FillService.get(id)

        type_fill_model.type_id = type_id
        type_fill_model.fill_id = fill_id
        
        db_session.add(type_fill_model)
        db_session.commit()

        return False
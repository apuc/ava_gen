from db.models import Fill
from db.base import db_session

class FillService:
    
    
    @staticmethod
    def find():
        return Fill.query.all()


    @staticmethod
    def get(id):
        return Fill.query.filter_by(id=id).first()


    @staticmethod
    def remove(id):
        fill_model = FillService.get(id)
        db_session.delete(fill_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, value):
        if id == 'None':
            fill_model = Fill()
        else:
            fill_model = FillService.get(id)

        fill_model.value = value

        db_session.add(fill_model)
        db_session.commit()
        
        return True
import uuid
from db.models import Ava
from db.base import db_session

class AvaService:
    
    
    @staticmethod
    def find():
        return Ava.query.all()


    @staticmethod
    def get(id):
        return Ava.query.filter_by(id=id).first()
        

    @staticmethod
    def remove(id):
        ava_model = Ava.query.filter_by(id=id).first()
        db_session.delete(ava_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, sex, age):
        if id == 'None':
            ava_model = Ava()
            ava_model.id = str(uuid.uuid1())
            is_edit = False
        else:
            ava_model = Ava.query.filter_by(id=id).first()
            is_edit = True

        if(int(age) < 1):
            return dict(
                message = 'Возраст не может быть меньше 1',
                is_edit = is_edit
            )

        ava_model.age = age

        if(int(sex) == 0 or int(sex) == 1):
            ava_model.sex = sex
        else:
            return dict(
                message = 'Пол не определен',
                is_edit = is_edit
            )
        
        db_session.add(ava_model)
        db_session.commit()
        return False
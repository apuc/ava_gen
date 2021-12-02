from db.models import Figure
from db.base import db_session

class FigureService:
    
    
    @staticmethod
    def find():
        return Figure.query.all()


    @staticmethod
    def get(id):
        return Figure.query.filter_by(id=id).first()


    @staticmethod
    def remove(id):
        figure_model = FigureService.get(id)
        db_session.delete(figure_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, age, sex, type_id, rnd_fill):
        if id == 'None':
            figure_model = Figure()
            is_edit = False
        else:
            figure_model = FigureService.get(id)
            is_edit = True

        figure_model.type_id = type_id

        if(int(age) < 1):
            return dict(
                message = 'Возраст не может быть меньше 1',
                is_edit = is_edit
            )

        figure_model.age = age

        if(int(sex) == 0 or int(sex) == 1):
            figure_model.sex = sex
        else:
            return dict(
                message = 'Пол не определен',
                is_edit = is_edit
            )
        
        if(int(rnd_fill) == 0 or int(rnd_fill) == 1):
            figure_model.rnd_fill = rnd_fill
        else:
            return dict(
                message = 'Случайный цвет не определен не определен',
                is_edit = is_edit
            )
        db_session.add(figure_model)
        db_session.commit()

        return False
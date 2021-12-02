from db.models import Path
from db.base import db_session

class PathService:
    
    
    @staticmethod
    def find():
        return Path.query.all()


    @staticmethod
    def get(id):
        return Path.query.filter_by(id=id).first()


    @staticmethod
    def remove(id):
        path_model = PathService.get(id)
        db_session.delete(path_model)
        db_session.commit()
        return True

    
    @staticmethod
    def save(id, d, extend_fill, fill_id, priority, figure_id, status):

        if id == 'None':
            path_model = Path()
            is_edit = False
        else:
            path_model = PathService.get(id)
            is_edit = True

        if(not (int(extend_fill) == 0 or int(extend_fill) == 1)):
            return dict(
                message = 'extend_fill не определен',
                is_edit = is_edit
            )
        
        if(not (int(status) == 0 or int(status) == 1)):
            return dict(
                message = 'status не определен',
                is_edit = is_edit
            )
        path_model.d = d
        path_model.extend_fill = extend_fill
        path_model.fill_id = fill_id
        path_model.priority = priority
        path_model.figure_id = figure_id
        path_model.status = status
        db_session.add(path_model)
        db_session.commit()
        
        return False
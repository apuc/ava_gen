from db.models import Figure, Path, Fill, Type
from services.PathService import PathService
from services.TypeService import TypeService
from services.FillService import FillService
from services.FigureService import FigureService
import drawSvg as draw
import random

r = lambda: random.randint(0,255)
rnd_fill = '#%02X%02X%02X' % (r(),r(),r())
def generate():
    svg = draw.Drawing(90, 102, origin=(0, -102), displayInline=False)
    path = PathService.find()
    types = TypeService.find()
    figures = FigureService.find()

    """
    Delete same figures
    """
    i=0
    
    while i < len(figures):
        j=0
        while j < len(figures):
            if(len(figures)<=i):
                break
            if(figures[j].type_id == figures[i].type_id and i != j):
                figures.remove(figures[i] if random.random() > 0.5 else figures[j])
                i-=1
                break
            j+=1
        i+=1

    is_d = False
    for element in path:
        fill = FillService.get(element.fill_id).value
        status = element.status
        for figure in figures:
            if(element.figure_id == figure.id):
                is_d = True
                d = element.d
                extend_fill = element.extend_fill
                if extend_fill:
                    fill = rnd_fill

        if(is_d):
            svg.append(draw.Path(d = d, fill=fill))
        is_d = False


    svg.saveSvg('example.svg')




if __name__ == '__main__':
    generate()
from services.PathService import PathService
from services.TypeService import TypeService
from services.FillService import FillService
from services.FigureService import FigureService
from services.Type_FillService import Type_FillService
import drawSvg as draw
import random

rnd_fill = random.choice(FillService.find()).value
hair_fill = FillService.get(random.choice(Type_FillService.get_by_type(7)).fill_id).value
brows_fill = FillService.get(random.choice(Type_FillService.get_by_type(9)).fill_id).value
eyes_fill = FillService.get(random.choice(Type_FillService.get_by_type(10)).fill_id).value

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
                    this_type = TypeService.get(figure.type_id).slug
                    if(this_type == 'eyes'):
                        fill = eyes_fill
                    elif(this_type == 'hair'):
                        fill = hair_fill
                    elif(this_type == 'brows'):
                        fill = brows_fill
                    else:
                        fill = rnd_fill

        if(is_d):
            svg.append(draw.Path(d = d, fill=fill))
        is_d = False


    svg.saveSvg('example.svg')

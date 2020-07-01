import copy
import numpy
from PIL import Image

SPREAD = 250
LOCAL_SPREAD = 6

COLOR_DATA = {
    (227, 227, 227): "Дорога населенного пункта",
    (40, 40, 40): "Один из многочисленных домов",
    (130, 80, 130): "Доки, где корабли разгружают груз а моряки танцуют с портовыми девками",
    (100, 150, 30): "Торговая лавка, скупающая всё по выгодной цене",
    (120, 180, 255): "Храм для молитв и исцелений",
    (100, 70, 0): "Таверна с вечно горящим камином",
    (255, 255, 255): "Центр города",
    (10, 10, 50): "Глубокий тёмный океан",
    (30, 140, 200): "Быстрая река",
    (30, 100, 150): "Озеро, полное рыбы",
    (80, 255, 120): "Влажный песчаный берег",
    (255, 255, 130): "Главное учебное здание - Пансионат"
}

PLACE_COLOR = {
    "0":numpy.array([0, 30, 255], dtype=int),
    "1":numpy.array([120, 120, 120], dtype=int),
    "2":numpy.array([120, 255, 0], dtype=int),

    "3":numpy.array([150, 0, 0], dtype=int),
    "4":numpy.array([0, 60, 0], dtype=int),
    "5":numpy.array([120, 210, 20], dtype=int),

    "6":numpy.array([10, 50, 10], dtype=int),
    "7":numpy.array([190, 225, 40], dtype=int),
    "8":numpy.array([120, 90, 0], dtype=int),

    "9":numpy.array([20, 150, 255], dtype=int),
    "10":numpy.array([190, 255, 150], dtype=int),
    "11":numpy.array([20, 30, 70], dtype=int),

    "12":numpy.array([0, 60, 0], dtype=int),
    "13":numpy.array([255, 0, 255], dtype=int),
    "14":numpy.array([190, 255, 150], dtype=int),

    "15":numpy.array([170, 0, 0], dtype=int)
}

class GlobalMap():
    def __init__(self):
        #self.map = numpy.nan_to_num(numpy.genfromtxt('db/map.txt', delimiter=',')).astype(int)
        #(3042, 3042)
        self.img_map = Image.open("database/test_map.png")

    def calc_position(self, x, y, size):
        x1 = 0 if x-size<=0 else x-size
        x2 = 5000 if x+size>=5000 else x+size

        y1 = 0 if y-size<=0 else y-size
        y2 = 5000 if y+size>=5000 else y+size

        return x1, x2, y1, y2

    def get_map(self, position, size):
        x, y = position
        x1, x2, y1, y2 = self.calc_position(x, y, size)
        #set player position
        tmp = copy.copy(self.img_map)
        tmp.putpixel((x, y), (255, 0, 0))
        tmp = tmp.crop((x1, y1, x2+1, y2+1))
        tmp = tmp.resize((500, 500), Image.NEAREST)


        tmp.save("db/tmp_img.png")

        return open("database/tmp_img.png", 'rb')

    def move_person(self, _from, _to):
        #print("coords - ", _from, _to)
        x, y = _from
        try:
            x1, y1 = int(_to[0]), int(_to[1])

            if x1 in range(0, 5001) and y1 in range(0, 5001):
                return [x1, y1]
            else:
                raise ValueError

        except Exception as E:
            print(Exception)
            return [x, y]

    def get_point_description(self, position):
        """Select color of the pixel where player stands and 
           print common cell description"""
        x, y = map(int, position)
        pixel = self.img_map.getpixel((x, y))[:3]
        return COLOR_DATA[pixel]
        

MAP = GlobalMap()
import numpy
from PIL import Image

SPREAD = 400
LOCAL_SPREAD = 50

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
        self.map = numpy.nan_to_num(numpy.genfromtxt('database/map.txt', delimiter=',')).astype(int)
        #(3042, 3042)
        self.img_map = numpy.array(Image.open("database/full_map.png"))

    def get_full_map(self, explored, position):
        x, y = position
        #x
        if x - SPREAD <=0:
            x1 = 0
        else:
            x1 = x-SPREAD

        if x+SPREAD>=3041:
            x2 = 3041
        else:
            x2 = x+SPREAD
        #y
        if y - SPREAD <=0:
            y1 = 0
        else:
            y1 = y-SPREAD

        if y+SPREAD>=3041:
            y2 = 3041
        else:
            y2 = y+SPREAD

        tmp = []
        for i in range(x1, x2):
            tmp.append([])
            for j in range(y1, y2):
                tmp[-1].append(self.img_map[i][j])

        tmp = numpy.array(tmp)
        im = Image.fromarray(tmp)
        im.save("database/tmp_img.png")

        del tmp
        del im

        return open("database/tmp_img.png", 'rb')

    def get_local_map(self, explored, position):
        x, y = position
        #x
        if x - LOCAL_SPREAD <=0:
            x1 = 0
        else:
            x1 = x-LOCAL_SPREAD

        if x+LOCAL_SPREAD>=3041:
            x2 = 3041
        else:
            x2 = x+LOCAL_SPREAD
        #y
        if y - LOCAL_SPREAD <=0:
            y1 = 0
        else:
            y1 = y-LOCAL_SPREAD

        if y+LOCAL_SPREAD>=3041:
            y2 = 3041
        else:
            y2 = y+LOCAL_SPREAD

        tmp = []
        for i in range(x1, x2):
            tmp.append([])
            for j in range(y1, y2):
                tmp[-1].append(self.img_map[i][j])
        
        tmp = numpy.array(tmp)
        im = Image.fromarray(tmp)
        im.save("database/tmp_img.png")

        del tmp
        del im
        return open("database/tmp_img.png", 'rb')


MAP = GlobalMap()

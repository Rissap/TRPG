class KeyboardGenerator():
    """generating different matrix of keyboard"""
    def __init__(self):
        self.pattern = [[2, 1, 2], [2, 2], [2], [1,1,1,1,2], [1,1,1,2], [1,1,1], [3,3,3,1], [1], [1,1], [1,1,1], [1,1,1,1], [1,1,1,1,1]]
        self.foo = [self.gen212, self.gen22, self.gen01, self.gen11112, self.gen1112, self.gen111, self.gen3331, self.gen1, self.gen1, self.gen1, self.gen1, self.gen1]

    def generate(self, keyboard, text):
        a = []
        for el in text.split("||"):
            a.append(len(el.split("|")))

        index = self.pattern.index(a)
        self.foo[index](keyboard, text)
    
    def gen1(self, keyboard, text):
        rows = text.split("||")
        for el in rows:
            keyboard.row(el)

    def gen212(self, keyboard, text):
        rows = text.split("||")
        a, b, c = rows[0].split("|"), rows[1].split("|"), rows[2].split("|")
        keyboard.row(a[0], a[1])
        keyboard.row(b[0])
        keyboard.row(c[0], c[1])

    def gen22(self, keyboard, text):
        rows = text.split("||")
        a, b = rows[0].split("|"), rows[1].split("|")
        keyboard.row(a[0], a[1])
        keyboard.row(b[0], b[1])

    def gen01(self, keyboard, text):
        a = text.split("|")
        keyboard.row(a[0], a[1])

    def gen11112(self, keyboard, text):
        rows = text.split("||")
        a, b, c, d, e = rows[0].split("|"), rows[1].split("|"), rows[2].split("|"), rows[3].split("|"), rows[4].split("|")
        keyboard.row(a[0])
        keyboard.row(b[0])
        keyboard.row(c[0])
        keyboard.row(d[0])
        keyboard.row(e[0], e[1])

    def gen1112(self, keyboard, text):
        rows = text.split("||")
        a, b, c, d = rows[0].split("|"), rows[1].split("|"), rows[2].split("|"), rows[3].split("|")
        keyboard.row(a[0])
        keyboard.row(b[0])
        keyboard.row(c[0])
        keyboard.row(d[0], d[1])

    def gen111(self, keyboard, text):
        rows = text.split("||")
        keyboard.row(rows[0])
        keyboard.row(rows[1])
        keyboard.row(rows[2])

    def gen3331(self, keyboard, text):
        rows = text.split("||")

        a, b, c = rows[0].split("|")
        d, e, f = rows[1].split("|")
        h, i, j = rows[2].split("|")

        q = [a, b, c, d, f, h, i, j]
        for el in range(len(q)):
            q[el] = chr(int(q[el], 16))

        keyboard.row(q[0], q[1], q[2])
        keyboard.row(q[3], e, q[4])
        keyboard.row(q[5], q[6], q[7])
        keyboard.row(rows[3])

KEYGEN = KeyboardGenerator()
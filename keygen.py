class KeyboardGenerator():
    """generating different matrix of keyboard"""
    def __init__(self):
        self.pattern = [[2, 1, 2], [2, 2], [2], [1,1,1,1,2], [1,1,1,2]]
        self.foo = [self.gen212, self.gen22, self.gen1, self.gen11112, self.gen1112]

    def generate(self, keyboard, text):
        a = []
        for el in text.split("||"):
            a.append(len(el.split("|")))

        for index in range(len(self.pattern)):
            if self.pattern[index] == a:
                self.foo[index](keyboard, text)

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

    def gen1(self, keyboard, text):
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
class Position:

    def __init__(self, name, price=0, desc='', paid=False):
        self.name = name
        self.price = price
        self.desc = desc
        self.paid = paid

    def pay(self):
        self.paid = True

    def modify(self, what, new_val):
        if what == 1:
            self.name = new_val
        elif what == 2:
            self.price = new_val
        elif what == 3:
            self.desc == new_val

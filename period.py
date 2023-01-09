import position
from position import Position
from json import JSONEncoder


class Period:
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]

    def __init__(self, year, month, positions=[], ):
        self.positions = positions
        self.year = year
        self.month = month

    def add_position(self, name: str = '', price: int = 0, desc: str = '', paid: bool = False, positions=[]) -> None:

        if len(positions) > 0:
            self.positions.extend(positions)
        else:
            p = Position(name, price, desc, paid)
            self.positions.append(p)

    def delete_position(self, index: int) -> None:
        del self.positions[index - 1]

    def modify_position(self, index: int, what: int, new):
        self.positions[index - 1].modify(what, new)

    def mark_as_paid(self, index):
        self.positions[index - 1].pay()

    def display(self):
        print("Year: {0}, month: {1}".format(self.year, self.months[self.month - 1]))
        print()
        print("-" * 100)

        # print positions
        print("{:2} | {:30} | {:8} | {:44} | {:2}".format("Lp", "name", "price", "description", "paid"))
        print("-" * 100)
        total = 0
        total_paid = 0
        for i, p in enumerate(self.positions):
            if p.paid:
                paid = 'X'
                total_paid += p.price
            else:
                paid = ''

            print("{0:2} | {1:30} | {2:8} | {3:44} | {4:2}".format(i + 1, p.name, p.price, p.desc, paid))

            total += p.price

        # print totals
        print()
        print("Total: {}".format(total))
        print("Paid: {}".format(total_paid))
        print()


class PeriodEncoder(JSONEncoder):
    def default(self, p):
        d = {"year": p.year, "month": p.month, "positions": list(x.__dict__ for x in p.positions)}

        return d

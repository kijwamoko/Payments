import json
from period import Period
from period import PeriodEncoder
from position import Position
import utiities


class PeriodHandler:
    menu = ["Add positions from template",
            "Add position manually",
            "Mark position as paid",
            "Modify position",
            "Delete position",
            "Display",
            "Save",
            "Exit",
            ]

    choice_map = ["ADDTEMP", "ADDMAN", "ASPAID", "MODIFY", "DELETE", "DISPLAY", "SAVE", "EXIT"]

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.p = None

    def handle(self):
        pass

    def display_period(self):
        self.p.display()

    def delete_position(self):
        index = int(input("Get position index from display list (<=0 to cancel)"))

        if index <= 0 or index > len(self.p.positions):
            print("Position with index {} doesn't exist.".format(index))
            return False

        self.p.delete_position(index)
        print("Position {} deleted.".format(index))
        return True

    def mark_position_as_paid(self):
        index = int(input("Get position index from display list (<=0 to cancel)"))

        if index <= 0 or index > len(self.p.positions):
            print("Position with index {} doesn't exist.".format(index))
            return False

        self.p.mark_as_paid(index)
        return True

    def modify_position(self):
        index = int(input("Get position index from display list (<=0 to cancel)"))

        if index <= 0 or index > len(self.p.positions):
            print("Position with index {} doesn't exist.".format(index))
            return False

        index2 = int(input("What do you want to modify? (1 - Name, 2 - Price, 3 - Description"))

        if index2 == 1:
            new = input("enter new Name")
        elif index2 == 2:
            new = float(input("Enter new Price"))
        elif index2 == 3:
            new = input("Enter new description")
        else:
            print("Wrong choice")
            return False

        self.p.modify_position(index, index2, new)
        return True

    def add_manual_position(self):
        name = input('Get name')
        desc = input("Get description")
        price = float(input("Get price"))
        paid = input("Is position already paid? (y/n)")

        if paid == 'y':
            paid = True
        else:
            paid = False

        self.p.add_position(name=name, price=price, desc=desc, paid=paid, positions=[])

        return True

    def save(self):
        pass


class PeriodFileHandler(PeriodHandler):

    def __init__(self, year, month, directory='periods'):
        super().__init__(year, month)

        # Create period object
        # create object from file, if file exists, otherwise initialize object
        filename = f"{self.year}_{self.month}.json"
        self.mypath = directory + '/' + filename

        try:
            with open(self.mypath) as json_file:
                data = json.load(json_file)

                # first create positions list
                positions = []
                for pos in data['positions']:
                    positions.append(Position(pos['name'], pos['price'], pos['desc'], pos['paid']))

                self.p = Period(data['year'], data['month'], positions)

                print('Object created from file data')
        except FileNotFoundError:
            print("File {} doesn't exist yet".format(filename))
            self.p = Period(year, month)

        if self.p is None:
            raise RuntimeError("Fatal error!!! Period object could not be created")

    def save(self):
        file = json.dumps(self.p, indent=4, cls=PeriodEncoder)

        with open(self.mypath, "w") as outfile:
            outfile.write(file)
            print("Data saved to file {}".format(self.mypath))
            return True

    def handle(self):
        super().handle()

        changed = False
        while True:

            # print menu
            for i, pos in enumerate(PeriodHandler.menu):
                print("{}. {}".format(i + 1, pos))

            choice = int(input())
            func = PeriodHandler.choice_map[choice - 1]

            if func == "ADDTEMP":
                self.p.add_position(positions=utiities.get_template_positions())
                print("Positions added from template file")

                changed = True

            elif func == "ADDMAN":
                changed = self.add_manual_position

            elif func == "DELETE":
                changed = self.delete_position()

            elif func == "ASPAID":
                changed = self.mark_position_as_paid()

            elif func == "DISPLAY":
                self.display_period()

            elif func == "SAVE":
                if self.save():
                    changed = False

            elif func == 'MODIFY':
                changed = self.modify_position()

            elif func == "EXIT":
                if changed:
                    answer = input('Data was changed and not saved. Do you want to exit anyway? (y/n)')
                    if answer.casefold() == 'y':
                        break
                else:
                    break
            else:
                print("Function {} doesn't exist, please correct your choice".format(func))

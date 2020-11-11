"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
import json


class WarehouseEquipments:
    shelf = {}
    in_work = {}
    __current_num = 1000

    def __init__(self, shelf={}):
        self.take_storage_equipments(shelf)

    def take_storage_equipments(self, equipments):
        for machine in equipments:
            self.take_storage(machine)

    def take_storage(self, equipment):
        if isinstance(equipment, OfficeEquipment):
            for _ in range(equipment.number):
                self.__current_num += 1
                equipment.inventory_number = self.__current_num
                self.shelf[self.__current_num] = equipment

    def find_by_inventory(self, number):
        return self.shelf[number]

    def move_in_work(self, inventory, division):
        self.in_work[inventory] = (self.shelf[inventory], division)
        del (self.shelf[inventory])

    def move_in_shelf(self, inventory):
        self.shelf[inventory], _ = self.in_work[inventory]
        del (self.in_work[inventory])

    def print_shelf(self):
        for inventory, equipment in self.shelf.items():
            print(f'{inventory} {equipment.type} {equipment.brand} {equipment.model}')

    def print_in_work(self):
        for inventory, (equipment, division) in self.in_work.items():
            print(f'{inventory} {equipment.type} {equipment.brand} {equipment.model}  {division}')



class OfficeEquipment:
    brand = ''
    model = ''
    inventory_number = 0
    dimensions = (0, 0)
    weight = 0
    place = (0, 0)
    is_network = False
    number = 0

    def __init__(self, brand, model, number=1):
        self.brand = brand
        self.model = model
        self.number = number


class Printer(OfficeEquipment):
    type = 'Принтер'
    letter_size = ''
    color = False


class CopyMachine(OfficeEquipment):
    type = 'Копир'
    auto_feeder = False


class Scanner(OfficeEquipment):
    type = 'Сканер'
    is_pdf_ready = False


class MenuController:
    __WH = None

    def __init__(self, wh: WarehouseEquipments):
        self.__WH = wh
        self.builder = [None, Printer, Scanner, CopyMachine]
        self.action = [self.flag_exit,
                       self.refresh, self.add_equipment, self.move_in_work, self.move_shelf, self.dump]

    def run(self):
        while True:
            self.action[1]()
            key = self.print_menu()
            if self.action[key]():
                break

    def flag_exit(self):
        return True;

    def print_menu(self):
        print('1 - Обновить')
        print('2 - Добавить')
        print('3 - Выдать')
        print('4 - Принять')
        print('-----------')
        print('5 - Дамб')

        print('0 - Выход')
        key = input('? :')
        return int(key)

    def dump(self):
        print(json.dumps(self.__WH.shelf))
        print(json.dumps(self.__WH.in_work))

    def refresh(self):
        print('=== Cocтояние склада')
        self.__WH.print_shelf()
        print('')
        print('=== Выдано')
        self.__WH.print_in_work()
        return False

    def add_equipment(self):
        print('=== Введите оборудование')
        type_eq = input('Модель (1-Принтер, 2-Сканер, 3-Копир) :')
        brand = input('Бренд :')
        model = input('Модель:')
        number = input('Количество :')
        eq = self.builder[int(type_eq)](brand, model, int(number))
        self.__WH.take_storage(eq)
        return False

    def move_in_work(self):
        inventory = input('ВВедите инв N :')
        division = input('Введите отдел :')
        self.__WH.move_in_work(int(inventory), division)
        return False

    def move_shelf(self):
        inventory = input('ВВедите инв N :')
        self.__WH.move_in_shelf(int(inventory))
        return False


class SideKick:
    @staticmethod
    def full_wh(wh: WarehouseEquipments):
        sc_1 = Scanner('Canon', 'CanoScan LiDE 400')
        sc_2 = Scanner('Epson', 'Perfection V19')
        sc_3 = Scanner('Panasonic', 'KV-SL1066')
        pr_1 = Printer('Xerox', 'Phaser 3020BI')
        pr_2 = Printer('HP', 'LaserJet Pro M15w')
        pr_3 = Printer('Brother', 'HL-L2340DWR')
        cp_1 = CopyMachine('Xerox', 'B1022')
        cp_2 = CopyMachine('Xerox', 'B215')
        cp_3 = CopyMachine('Konica-Minolta', 'A0XY026')
        wh1.take_storage_equipments([sc_1, sc_2, sc_3, pr_1, pr_2, pr_3])


if __name__ == '__main__':
    wh1 = WarehouseEquipments()
    SideKick.full_wh(wh1)
    MenuController(wh1).run()

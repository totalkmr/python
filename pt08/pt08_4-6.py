class EquipStore:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class OfficeEquipment:
    def __init__(self, type_equip, model, date_prod):
        self.type_equip = type_equip
        self.model = model
        self.date_prod = date_prod

    def __str__(self):
        return f'| Type: {self.type_equip}\t | Model: {self.model}\t | Date production: {self.date_prod} |'


class OutcomeException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Balance:
    balance = {}

    def __init__(self, store=0):
        self.store = None
        if store is not None:
            self.use(store)

    def use(self, store):
        self.store = store
        if not (store in self.balance.keys()):
            self.balance[store] = []

    def income(self, equipment):
        self.balance[self.store].append(equipment)

    def outcome(self, equipment):
        try:
            if not (equipment in self.balance[self.store]):
                raise OutcomeException('Данного оборудования нет на складе.')
            else:
                self.balance[self.store].remove(equipment)
        except OutcomeException:
            print('\nДанного оборудования нет на складе.')

    def report(self):
        return '\n'.join(f'\n{key.name}, {key.address} ({len(value)}):' + f'\n\t' + f'\n\t'.join(map(str, value))
                         for key, value in self.balance.items())


class Printer(OfficeEquipment):
    def __init__(self, type_equip, model, date_prod, type_print):
        super().__init__(type_equip, model, date_prod)
        self.type_print = type_print


class Scanner(OfficeEquipment):
    def __init__(self, type_equip, model, date_prod, optical_resolution):
        super().__init__(type_equip, model, date_prod)
        self.optical_resolution = optical_resolution


class Copier(OfficeEquipment):
    def __init__(self, type_equip, model, date_prod, print_speed):
        super().__init__(type_equip, model, date_prod)
        self.print_speed = print_speed


printer = Printer('printer', 'hp', '01.01.2020', 'ink')
scanner = Scanner('scanner', 'canon', '12.12.2019', 2500)
copier = Copier('copier', 'xerox', '07.06.1977', 30)

main_store = EquipStore('Main store', 'Lenina str., 45')
balance = Balance(main_store)

balance.income(scanner)
balance.income(printer)
balance.income(copier)

print(balance.report())

balance.outcome(copier)

print(balance.report())

balance.outcome(copier)
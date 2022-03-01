# task_11_5.py
from actions.warehouse_dict import Warehouse
from actions.office_equipment_dict import Printer, Scanner, Xerox


warehouse_1 = Warehouse()
warehouse_1.note = 'текст моей записки'
warehouse_1.title = 'Склад оргтехники #1'

print()

print("Создание объектов оргтехники:")
printer_1 = Printer('HP LaserJet P2015', 'printer',
                    '01', True, warehouse_1.our_warehouse)
print(printer_1.diagnostics())
printer_2 = Printer('HP LaserJet P3005', 'printer',
                    '02', True, warehouse_1.our_warehouse)
print(printer_2.diagnostics())
scanner_1 = Scanner('HP ScanJet 5590P', 'scanner',
                    '03', True, warehouse_1.our_warehouse)
print(scanner_1.diagnostics())
xerox_1 = Xerox('XEROX WorkCentre 3550', 'xerox',
                '04', True, warehouse_1.our_warehouse)
print(xerox_1.diagnostics())

print()

# __str__
print(f'"{warehouse_1.title}" - имеющееся оборудование:')
for key, value in warehouse_1.our_warehouse.items():
    print(f'\tserial: {key}, "{value[0]}", {value[1]}')
print()

departments = ['production',  # производство
               'accounting',  # бухгалтерия
               'supply',  # снабжение
               'sales',  # отдел продаж
               'advertising',  # отдел рекламы
               'management'  # руководство компании
               ]

print(departments)
location = dict()

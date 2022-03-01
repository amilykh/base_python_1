# task_11_4.py
from actions.warehouse import Warehouse
from actions.office_equipment import Printer, Scanner


warehouse_1 = Warehouse()
warehouse_1.note = 'текст моей записки'
warehouse_1.title = 'Склад оргтехники #1'

print()

print("Создание объектов оргтехники:")
printer_1 = Printer('HP LaserJet P2015', 'printer',
                    '01', warehouse_1.our_warehouse)
print(printer_1.diagnostics())
printer_2 = Printer('HP LaserJet P3005', 'printer',
                    '02', warehouse_1.our_warehouse)
print(printer_2.diagnostics())
scanner_1 = Scanner('HP ScanJet 5590P', 'scanner',
                    '03', warehouse_1.our_warehouse)
print(scanner_1.diagnostics())

print('\n')

# __str__
print(f'"{warehouse_1.title}" - имеющееся оборудование:')
for equipment in warehouse_1.our_warehouse:
    print(f'\t{equipment}')
print()
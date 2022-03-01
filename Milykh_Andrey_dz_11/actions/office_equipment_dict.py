from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name_equipment: str, type_equipment: str,
                 serial_number: str, is_new: bool, warehouse: dict):
        self.name_equipment = name_equipment
        self.type_equipment = type_equipment
        self.serial_number = serial_number
        self.warehouse = warehouse
        self.is_new = is_new
        self.warehouse.update({self.serial_number: [self.name_equipment,
            self.type_equipment, self.is_new]})

    def __str__(self):
        return f'"{self.name_equipment}", serial: {self.serial_number}'

    @abstractmethod
    def diagnostics(self) -> str:
        pass


class Printer(OfficeEquipment):
    def diagnostics(self) -> str:
        return f'Я {self.__class__.__name__}' \
               f' "{self.name_equipment}", serial: {self.serial_number} !'

    def printing(self):
        pass


class Scanner(OfficeEquipment):
    def diagnostics(self) -> str:
        return f'Я {self.__class__.__name__}' \
               f' "{self.name_equipment}", serial: {self.serial_number} !'

    def scanning(self):
        pass


class Xerox(OfficeEquipment):
    def diagnostics(self) -> str:
        return f'Я {self.__class__.__name__}' \
               f' "{self.name_equipment}" serial: {self.serial_number} !'

    def photocopying(self):
        pass

class Warehouse:
    def __init__(self):
        self.our_warehouse: set = set()
        self.title = 'empty'

    def __setattr__(self, attr, value):
        if attr == 'title' and isinstance(value, str):
            self.__dict__[attr] = value
            print(f'Вы переписали название склада, теперь это "{self.title}"')
        elif attr == 'our_warehouse':
            self.__dict__[attr] = value
        else:
            print(f'Атрибут "{attr}" или значение "{value}" недопустимы')

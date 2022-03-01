# task_11_1.py
# import datetime as dt
# import io


class Date:
    def __init__(self, date: str):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def get_date(cls, date):
        list_date = date.split('-')
        list_date_best = [i.strip('0') for i in list_date]
        list_date_num = list(map(int, list_date_best))
        return list_date_num[0], list_date_num[1], list_date_num[2]


d1 = Date('22-04-1870')
print(d1)
day, month, year = Date.get_date(d1.date)
print(day)
print(month)
print(year)

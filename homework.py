# Колькулятор для подсчета денег и колорий
import datetime as dt
date_format = '%d.%m.%Y'

class Record: # Этот класс работает пиздато, но пока хуевинько !!!!!
    """Class records amount cash in rubles  or callories in kcal, current date,
       comment and sends data in calculator."""
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.date = date
        self.comment = comment


class Calculator:
    """Class saves new record, counts spend of ... today, counts spend of ... 
    for seven days."""
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records = []  # здесь лежат все объекты класса records, 
        # то есть все записи

        self.records_day = []  # здесь лежат все значчения summ
        self.records_day_only = []  # здесь лежат все значения amount 
        # для настоящего дня
        self.last_of_seven_days = []
        

    def add_record(self, record):
        """Method appends new record."""
        self.records.append(record)
        print(record.date)

    def get_today_stats(self):
        """counts cost per day."""
        now = dt.datetime.now().date()
        summ = 0

        for i in self.records:
            if i.date == now:
                summ += i.amount
        return summ

    def get_week_stats(self):
        """counts cost per week."""
        summ = 0
        now = dt.datetime.now().date()
        tomorow = now + dt.timedelta(days=1)
        week_ago = now - dt.timedelta(days=7)

        for i in self.records:
            if week_ago<i.date<tomorow:
                summ += i.amount
        return summ
    

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remained = self.limit - super().get_today_stats()
        if remained > 0:
            return (f'Сегодня можно съесть что-нибудь еще, но c общей'
                    f'калорийностью не более {remained} Ккал.')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):

    def get_today_cash_remained(self, currency):
        USD_RATE = 93.04
        EURO_RATE = 99.01
        result = super().get_today_stats()
        total = self.limit - result
        
        if currency == 'rub':
            ret = f'{total}, rub'
        elif currency == 'usd':
            ret = f'{abs(round(total/ USD_RATE, 2))}, usd'
        else:
            ret = f'{abs(round(total/ EURO_RATE, 2))}, euro'

        if total > 0:
            return (f'На сегодня осталось {ret}.')
        else:
            return (f'Денег нет! Держись: твой долг - {ret}.')
        


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=105, comment='Печенье'))
cash_calculator.add_record(Record(amount=1505, comment='Стоянка'))
# print(cash_calculator.get_today_stats())
# print(dt.datetime.now().date())
print(cash_calculator.get_today_cash_remained('usd'))
# print(cash_calculator.get_week_stats())

#calories_calculator = CaloriesCalculator(2000)
#calories_calculator.add_record(Record(amount=205, comment='Вафли'))
#calories_calculator.add_record(Record(amount=305, comment='Булочка'))
#print(calories_calculator.get_calories_remained())




# Колькулятор для подсчета денег и колорий
import datetime as dt
date_format = '%d.%m.%Y'
now = dt.datetime.now().date()

class Records:
    """Class records amount cash in rubles  or callories in kcal, current date, comment and sends data in calculator"""
    def __init__(self, amount, date, comment) -> None:
        self.amount = amount
        self.date = dt.datetime.strptime(date, date_format)
        self.comment = comment


class Calculator:
    """Class saves new record, counts spend of ... today, counts spend of ... for seven days"""
    def __init__(self, limit) -> None:
        self.limit = limit

    records = [] # здесь лежат все объекты класса records, то есть все записи
    
    def add_record(self, record):
        """Method appends new record """
        self.records.append(record)

    records_day = [] # здесь лежат все значчения summ 
    def get_today_stats(self):
        """counts cost per day"""
        records_day_only = [] # здесь лежат все значения amount для настоящего дня
        for i in self.records:
            if i.date == now:
                records_day_only.append(i.amount)
        summ = 0
        for i in records_day_only:
            summ += i
        return summ

        
    def get_week_stats(self):
        """counts cost per week"""
        last_of_seven_days = []
        start = now - dt.timedelta(days=7)
        for i in range(7):
            last_of_seven_days.append(now - dt.timedelta(i))
        summ = 0
        for i in self.records:
            if i.date in last_of_seven_days:
                summ += i.amount
        return summ
    


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remained = self.limit - super().get_today_stats()
        if remained > 0:
            return f'Сегодня можно съесть что-нибудь еще, но c общей калорийностью не более {remained} Ккал'
        else:
            return f'Хватит есть!'


    
    
class CashCalculator(Calculator):
    USD_RATE = 93.04
    EURO_RATE = 99.01
    def get_today_cash_remained(self, curruncy):
        if curruncy  == 'rub':
            return super().get_week_stats()
        elif currency =='usd':
            return super().get_week_stats()/USD_RATE
        else:
            return super().get_today_stats()/EURO_RATE
        




cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Records(amount=105, comment= 'Печенье', date = '5.11.2023'))


print(cash_calculator.get_today_cash_remained('rub'))

print(cash_calculator.get_today_stats)

print(cash_calculator.amount)






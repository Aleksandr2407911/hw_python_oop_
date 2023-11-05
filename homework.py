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
    
    def add_record(record):
        """Method appends new record """
        records.append(record)

    records_day = [] # здесь лежат все значчения summ 
    def get_today_stats():
        """counts cost per day"""
        records_day_only = [] # здесь лежат все значения amount для настоящего дня
        for i in records:
            if i.date == now:
                records_day_only.append(i.amount)
        summ = 0
        for i in records_day_only:
            summ += i
        return summ

        
    def get_week_stats():
        """counts cost per week"""
        last_of_seven_days = []
        start = now - dt.timedelta(days=7)
        for i in range(7):
            last_of_seven_days.append(now - dt.timedelta(i))
        for i in records:
            if i.date in last_of_seven_days:
                summ += i.amount
        return summ
    






        

         

        
        




class CaloriesCalculator(Calculator):
    



class CashCalculator(Calculator):







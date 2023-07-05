class Year:  
    def __init__(self, days):  
        self.days = days  
 
    @property  
    def days(self):  
        return self.__days  
 
    @days.setter  
    def days(self, days):  
        if days == 366 or days == 365:  
            self.__days = days  
        else:  
            raise Exception('Некорректное значение')  
 
    @days.deleter 
    def days(self): 
        del self.__days 
 
year = Year(365)  
print(year.days)  
 
year.days = 366 
print(year.days)  
 
del year.days
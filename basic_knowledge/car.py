class car():
    def __init__(self,logo,model,year):
        self.logo=logo
        self.model=model
        self.year=year
        self.miles_reading=0

    def car_info(self):
        total_name=str(self.year)+' '+self.logo+' '+self.model
        return total_name.title()
    
    def car_miles(self):
        print('This car has '+str(self.miles_reading)+' miles on it.')
    
    def car_miles_update(self,miles):
        if miles>self.miles_reading:
            self.miles_reading=miles
        else:
            print("WARMING!No roll back on miles!")
    
    def car_miles_increment(self,miles):
        if miles>0:
            self.miles_reading=self.miles_reading+miles
        else:
            print('No trick!')

class battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print('This car has a '+str(self.battery_size)+'-kWh battery')
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message='This car can go approcimately '+str(range)
        message+=' miles on a full charge.'
        print(message)



class electriccar(car):
    def __init__(self,logo,model,year):
        super().__init__(logo,model,year)
        self.battery=battery()
    
    def car_miles(self):
        print("Needn't record car's miles as electriccar!")

# my_tesla=electriccar('tesla','model s',2016)
# print(my_tesla.car_info())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.car_miles()

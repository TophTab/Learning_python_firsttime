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

my_car=car('audi','a4',2016)
print(my_car.car_info())
my_car.car_miles_update(23)
my_car.car_miles()
my_car.car_miles_update(10)
my_car.car_miles()
my_car.car_miles_increment(50)
my_car.car_miles()
my_car.car_miles_increment(-50)
my_car.car_miles()
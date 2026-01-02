class Vehicle:
    def __init__(self,brand,speed,price,color,gear,fuel_type,engine_status):
        self.brand=brand
        self.speed=speed
        self.price=price
        self.color=color
        self.gear=gear
        self.fuel_type=fuel_type
        self.engine_status=engine_status
    def start(self):
        print(f"{self.brand} Vehicle is starting")

    def show_detail(self):
        print(f"Brand-:: {self.brand}")
        print(f"Speed-:: {self.speed}")  
        print(f"Price-:: {self.price}")
        print(f"Color-:: {self.color}")  
        print(f"Gear-:: {self.gear}")
        print(f"Fuel Type-:: {self.fuel_type}") 
        print(f"Engine -:: {self.engine_status}")
      

class Car(Vehicle):
    def __init__(self, brand, speed,price,color,gear,fuel_type,engine_status,doors):
        Vehicle.__init__(self,brand,speed,price,color,gear,fuel_type,engine_status)
        self.doors=doors
    def show_detail(self):
        Vehicle.show_detail(self)
        print(f"Doors-:: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed,price,color,gear,fuel_type,engine_status,bike_type):
        Vehicle.__init__(self,brand,speed,price,color,gear,fuel_type,engine_status)
        self.bike_type=bike_type

    def show_detail(self):
        Vehicle.show_detail(self)
        print(f"Bike type-:: {self.bike_type}")

class Truck(Vehicle):
    def __init__(self,brand, speed,price,color,gear,fuel_type,engine_status,capacity):
        Vehicle.__init__(self,brand,speed,price,color,gear,fuel_type,engine_status)
        self.capacity=capacity

    def show_detail(self):
        Vehicle.show_detail(self)
        print(f"Capacity-:: {self.capacity} Tons")

car=Car("Farari",230,"Rs.3000000","Red",4,"Petrol","ON",5)
bike=Bike("Bullet",150,"Rs.150000","Z Black",2,"Petrol","ON","Drive Everthing")
truck=Truck("Tata",500,"Rs.450000","Silver",8,"Petrol","ON",25)
print()

print("--Car Detail--")
car.start()
car.show_detail()
print()
print()

print("--Bike Detail--")
bike.start()
bike.show_detail()
print()
print()

print("--Truck Detail--")
truck.start()
truck.show_detail()


                  
        
        

                   
        


       
                 
              
          
        
       
        
        


        
         

        


        



        
                   


                 

        
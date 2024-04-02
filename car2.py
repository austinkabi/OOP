class car:
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model
    def car_defaults (self):
        print("car make is",self.make)
        print("car year is",self.year)
        print("car model is",self.model)
toyota=car("toyota","2013","saloon")
toyota.car_defaults()
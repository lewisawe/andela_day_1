class Car(object):
    def __init__(self, name = 'General', model = 'GM', carType = None):
        self.name = name
        self.model = model
        self.carType = carType
	self.num_of_wheels = 4
    if self.carType == 'trailer':
            self.num_of_wheels = 8
	else:
            self.carType = 'saloon'
		
	if (self.name == 'Porshe') or (self.name == 'Koenigsegg'):
            self.num_of_doors = 2
	else:
            self.num_of_doors = 4

	self.speed = 0	
	

    def is_saloon(self):
        return self.carType == 'saloon'

    def drive(self, spd):		
        if self.carType == 'trailer':
	    self.speed = (spd * 77) / 7
        else:
            self.speed = (spd * 1000) / 3
		
    return self

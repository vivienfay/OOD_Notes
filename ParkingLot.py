# UseCases
# 1. A vehicle comes, parkinglot assign an available spot to it
# 2. A vehicle leave, check the total cnt and time, clear spot

class ParkingLot(object):
    def __init__(self):
        self.__slots = [] # List[ParkingSpot]
    
    def __checkAvailable(self):
        raise isFullException
        return #Dictionary[type: int]

    def __findSpotForVehicle(self, Vehicle): #spt
        return

    def parkVehicle(self, Vehicle): #ticket
        return

    def calculateFee(self, ticket): #int
        return
    
    def clearSpot(self, spot): #void
        return

class ParkingSpot(object):
    def __init__(self):
        self._isAvailable # boolean
        self._fee
        self._size

    def isAvailable(self): # boolean
        return 
    
    def clearSpot(self):
        return

    def getSize(self):
        return

class Vehicle(object):
    def __init__(self):
        self._size #size
        self._ticket
        self._spot
    
    def getSize(self):
        return

    def leaveSpot(self):
        return

class Motocycle(Vehicle):
    def __init__(self):
        super().__init__()

class CompactCar(Vehicle):
    def __init__(self):
        super().__init__()

class LargeCar(Vehicle):
    def __init__(self):
        super().__init__()

class Ticket(object):
    def __init__(self):
        self.__startTime #timestamp
        self.__endTime #timestamp
        self.__spot #spot
        self.__vehicle #vehicle

class isFullException(Exception):
    pass

class inValidTicket(Exception):
    pass
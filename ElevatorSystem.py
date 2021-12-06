# Use Case
# 1. Responds to the request from internal or external
# (1) Internal: someone click the level, move to that level
# Request -> Elevator: if the same Direction, insert to the direction list, 
# otherwise insert to different list
# (2) External: click direction, elevator move to that level
# Request -> ElevatorSystem -> Return Available Elevator
# 2. If elevator is overweight, throw exception
# 3. PressButton

class ElevatorSystem(object):
    def __init__(self):
        self.elevators = [] # List[Elevator]

    def handleExternalRequest(self, ExternalRequest):
        return #return void

class Elevator(object):
    def __init__(self):
        self.__currentLevel #int
        self.__status #Status
        self.__uplist # List[int]
        self.__downlist #List[int]
        self.__currentWeigth

    def handleExternalRequest(self, ExternalRequest):
        return
    
    def handleInternalRequest(self, InternalRequest):
        return

    def __move(self, Direction):
        return
    
    def __isValidRequest(self, Request):
        raise InvalidReqeustException

    def __openGate(self):
        return

    def __closeGate(self):
        return

    def __getWeight(self):
        return

class Request(object):
    def __init__(self):
        self.__level #int

class InternalRequest(Request):
    def __init__(self):
        super().__init__()
    
class ExternalRequest(Request):
    def __init__(self):
        super().__init__()
        self.__direction # Direction

class Button(object):
    def __init__(self):
        self.isLightened #boolean
    
    def click(self): #sendout request
        return

class ElevatorButton(Button):
    def __init__(self):
        super().__init__()
        self.__level # int
    
    def click(self): #send out internal request
        super().click()
        return

class LevelButton(Button):
    def __init__(self):
        super().__init__()
        self.__direction # Direction
    
    def click(self): #sendout external request
        super().click()

class Direction(Enum):
    Up, Down = 1, -1

class Status(Enum):
    Up, Down, Idle = 1, -1, 0


class InvalidReqeustException(Exception):
    pass

# Core Object
# Restaurant
# Table
# Menu
# Dish
# Order
# Party

# Use Case
# 1. Recieve the customer party, check if any available tables with appropriate size
# 2. take the order, provide dished
# 3. check the bills
# 4. leave the table, clear tables and dishes

class Restaurant(object):
    def __init__(self):
        self.__tables # HashMap<int: table>
        self.__menu #menu
    
    def findTable(self, Party): # return table
        raise NoAvailableTableException
        return

    def takeOrder(self, order): #order
        return

    def checkOut(self, bill): # Int
        # clear table
        return 

class Table(object):
    def __init__(self):
        self.__size #int
        self.__isAvailable #boolean
        self.__bill #bill
    
    def setAvailablity(self): #void
        return

    def getAvailable(self): #boolean
        return


class Order(object):
    def __init__(self):
        self.__dishes # List[dish]
        self.__table # table
        self.__party # party

    def getPrice(self): #return float
        return 

    def addDish(self, dish): # void
        return

    def removeDish(self, dish): #void
        return

class Menu(object):
    def __init__(self):
        self.__prices # HashMap <String: int>

    def getPrice(self): #int
        return

class Party(object):
    def __init__(self):
        self.__size # int
    
    def getSize(self): #int
        return

class Dish(object):
    def __init__(self):
        self.__type #string
        self.__price #float
    


class NoAvailableTableException(Exception):
    pass
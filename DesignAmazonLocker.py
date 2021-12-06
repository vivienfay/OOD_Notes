# 1. Delivery guy scanned the code and put the package to bin, 
# Locker system can help to find the available bin for the suitable
# bin with the suitable size
# 2. Once LockerSystem get the package stored in the bin, 
# system will send the notification to user, which includes the 
# barcode or PIN code
# 3. User input the barcode and Pincode and bin door open. User 
# pick up the package
# 4. If the package is stored for over 1 day, penalty fee will be 
# requested based on the day is stored. User have to pay after they 
# scanned the barCode/Pin code and before the bin code open.

class LockerSystem(object):
    def __init__(self, bins):
        self.__bins = bins # List[Bin]
        self.__availableBins # HashMap<Size, List[Bin]>
        self.__overdueFee # float
    
    def HandlePutRequest(self, account, package): #Account, Package, return Notification
        self.__findBin(package)
        self.__putPackage(bin, package)
        self.__sendNotification(package)
        pass

    def __findBin(self, package): #return Bin
        pass
    def __putPackage(self, bin, package, timestamp): # return void
        pass
    def __sendNotification(self, package):  #void
        pass

    def getPackage(self, Code, timestamp): # return package
        pass
    def payOverdue(self, Code, package, bin): # return boolean
        pass

    def __calculateOverdueFee(self, timestamp, bin): #return
        pass
    def __opendoor(self):
        pass
    def __closedoor(self):
        pass
    def __clearBin(self):
        pass

class Account(object):
    def __init__(self, username, password):
        self.__username = username #string
        self.__password = password #string

class Bin(object):
    def __init__(self, size):
        self.__size = size # Size[ENUM]
        self.__isAvailable # boolean
        self.__package # package
    
    def setAvailable(self): #void
        pass
    def getAvailable(self): #boolean
        pass
    def putPackage(self, package): #input Package, return void
        pass
    def pickUpPackage(self):
        pass

class Package(object):
    def __init__(self, size):
        self.__size #size
        self.__ownerPhoneNumber # string
    def getSize(self):
        pass
    def getPhoneNumber(self):
        pass

class Notification(object):
    def __init__(self, phoneNumber, barCode, pinCode):
        self.__barCode = barCode #barCode
        self.__pinCode = pinCode #binCode
        self.__phoneNumber #stirng
    
    def getBarCode(self): #return BarCode
        pass
    def getPinCode(self): #return PinCode
        pass

class Code(object):
    def __init__(self):
        self.__code #string
    def scanCode():
        pass

class BarCode(Code):
    def __init__(self):
        super().__init__()

class PinCode(Code):
    def __init__(self):
        super().__init__()

class Payment(object):
    def __init__(self, paymentRequestId):
        self.__paymentRequestId #integer
        self.__Paid #boolean
    
    def Pay(self): #return void
        pass
    def getPayStatus(self): # return boolean
        pass

class Size(enumerate):
    small, medium, large = 1, 2, 3

class NotEnoughBinException(Exception):
    pass

class OccupiedBinExcpetion(Exception):
    pass

class InvalidCode(Exception):
    pass

class EmptyBin(Exception):
    pass


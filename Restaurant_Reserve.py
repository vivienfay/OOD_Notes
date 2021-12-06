## Use Case

# 1. Customer can reserve or walkin 
# 2. Restaurant
# 3. Bill
# 4. Reserve
# 5. Menu
# 6. Meal
# 7. Table


class Restaurant(object):
    def __init__(self,):

class Menu(object):
    def __init__(self,):

class MenuItem(object):
    def __init__(self,):

class Table(object):
    def __init__(self,):

class Reservation(object):
    def __init__(self,):

class Customers(object):
    def __init__(self,):

class Order(object):
    def __init__(self,):

class Meal(object):
    def __init__(self,):

class Bill(object):
    def __init__(self,):

class Payment(object):
    def __init__(self,):

class CashPayment(Payment):
    def __init__(self,):
        super().__init__()

class CreditCardPayment(Payment):
    def __init__(self,):
        super().__init__()

class ApplePay(Payment):
    def __init__(self,):
        super().__init__()

class DebitCardPayment(Payment):
    def __init__(self,):
        super().__init__()


class InvalidPaymentAmount(Exception):
    pass

class InvalidOrder(Exception):
    pass

class InvalidReservationException(Exception):
    pass

class NoAvailableException(Exception):
    pass

### Method

- Clarify 
	- what
	- how
	-  Who
		- 思考是否
- Core Object
    - Package:  如果什么都不声明， 变量和函数都是package level visible的，在同一个package内的其他类
    - Public: 如果声明是public，变量和函数都是public level visible的， 任何其他的类都可以访问（+）
    - Private: 如果声明是private，变量和函数都是class level visible的，仅有定义这些变量和函数的类自己可以访问（封装）
    - Protected: 如果声明是protected，变量和函数在能被定义他们的类访问的基础上，还能被该类的子类所访问（继承）（#）
- Cases
	- 要实现的功能放在白纸黑字上use cases
- Class(UML泪图)
	- 遍历你所列出的use cases
	- 对于每个use case 更加详细描述use case在做什么事情
	- 针对这个描述，在已有的core objects里填充进所需要的信息
- Correctness



### Good Practice

1. Raise Exception

### Design Pattern

### 1. Strategy Design Pattern

- 管理类题目：处理payment


### 2. Singleton


### 3. State Design Pattern
### 4. Decor Design Pattern

context -> 

# 类型

## 1. 管理类

- 预定：

- LRU Cache: 搜索 》 预定 LinkedHashMap

### 1. clarify

名词， 所有的属性，管理的名词,

1. Parking Lot
2. Vehicle


### 2. Core Object

- 主体
- 什么是input/output




### 3. Use Case

从管理员角度出发
- Reserve
- Serve
- CheckOut

### 4. Class

- 使用收据的形式来保管信息

例子：图书馆。 User/Book/Recipt


# 2. 实物类 

- Vending Machine
- Jukebox
- CD player
- ATM machine
- Coffee Maker

技巧：

- 可以运用很多的design pattern


# 3. 棋牌类

- 玩家
- 规则
- 胜负
- 积分


- 棋牌类术语 board，suit， hand,
- 棋牌类状态：initialization， play， win/lose check + tie 流局

-----


# Case 1: Elevator

### 1. Clarify:

### 2. Core Object

### 3. Cases:
1. Handle Request
2. Take external request
3. Take internal request
4. Open Gate
5. Press Button
5. Close Gate

### 4. Class:

- External Request


- Internal Request


- Elevator System


- Elevator Button
    -level
    -Elevator elevator
    +InternalRequest prerssButton()




- Elevator System

### 5. Correctness
    1. Check if use cases validated
    2. Follow good practice
    3. S.O.L.I.D
    4. Design Pattern

# Case 2: Design Parking Lot

### 1. Clarify

What: Parking lot size? level? / Vehicle type? / Parking Spot type/disabled/electric car?

how: how to park the car? design the specific spot for certain car/ car spot can be combined

How: how to park? new car come in -> return an available spot -> a new spot was occupied by the new car-> need to show the number of available spots? -> free or paid pay by day/hour?


### 2. Core Object

- Parking lot
- Vehicle (Car, bus, motorcycle)
- Parking Spot ()


### 3. Use Case

- Parking Lot
    - Get Available count
    - Park Vehicle
    - Clear Spot
    - Calculate price

- Serve: Park vehicle
- Checkout: Clear Spot + Calculate price


### 4. Class


- Vehicle
    - #int size
    - +int getSize()  

- Bus
    - +int size

- Car
    - +int size

- Motorcycle
    - +int size

- Parkinglot
    - -List(Level) levels
    - -float HourlyRate
    - +int getAvailableCount
    - -List(Spot)findSpot(Vehcle v)
    - +void ParkVehicle(Vechicle v)
    - +void clearspot(ticket t)
    - float calculatePrice(Ticket t)

- Level
    - -List(Spot) spots
    - -int availableCount
    - +int getAvailableCount()
    - +void updateAvailableCount()
    
    
- Spot
    - -boolean available
    - Level I
    - +boolean isAvaiable()
    - +void takeSpot()
    - +void leaveSpot()
    
    
- Ticket
    - -vehicle
    - List(Spot)spots
    - Time startTime


- ParkingLotFullExpception
- 

# Case 3: Restaurant Reservation

### 1. Clarify

- What
- Who
- How

### 2. Core Object
- Restaurant
- Table
- Order
- Meal
- Party
### 3. Cases
- Find Table
- Take Order
- Checkout
- Reservation: Select / Search / Canceel
### 4. Class

- Party
    - -int capacity
    - -int getcapacity

- Restaurant
    - List(Tables)tables
    - List(Meal) menu
    - Map(Table, List(orders)) orders
    + table findtable()
    + void takeorder(order o)
    + void checkout(order o)

- Table
    - int capacity
    - Boolean Available
    + boolean isAvailable()
    + void makeUnavalable()
    + void makeAvailable()
    + int Getcapacity()

- Order
    - List(Meal) meals
    - table t
    - party p
    + float getPrice

- Meal
    - -float price
    - float getPrice


- NoTableException

### 5. Correction

# Case 4: Hotel Reservation

### 1. Clarify

- What: Search criteria -> Search() -> List(Result) -> Select() -> Cancel


### 3. Use  Case
- Search for available rooms
- Make Reservation
- Cancel Reservation



### 4. Class
- Request




- Hotel


- RoomType



- Room
    - int capacity
    - float price
    
    
-     
    
    

# Case 5: Vending Machine 

### 1. Clarify

- Who: Payment(coin, cash, credit card, ), item, 
- What: 
- How: select the item, refill

### 2. Core Object
    
- Vending Machine
- Item
- Coin
    
### 3. Use  Case

- Select item
- Insert the coin
- execute transaction
- cancel transaction
- refill item

### 4. Class
- VendingMachine
    - -List(coins) coins 
    - -List(items) items
    - -Map(string, iteminfo) itemIdentifier
    - -Map(iteminfo, list(item)) items
    - -iteminfo currentSelection
    - -list(coin) currentcoins
    - -state state
    - +float selectitem(string selection)
    - +float insertCoin(List(coin) coins)
    - +pair(item, list(coin)) executeTransaction()
    - -List(coin) refund()
    - -list(coin) cancelitem()
    + void refillItems(list(item) items)
    + void setState(State s)
    
    
- item
    

- coin enumerrationi
    - penny
    - nickle
    - dime 
    - quarter
    - float value

- sprite



- coke


- mountaindew


- iteminfo
    - -float price
    - +float getPrice()
    
- State Interface
    
    
 - NotEnoughMoneyException
 - NotEnoughItemException
 
 
 # Case 6: Coffee Maker
 
 
 
# Case 7: Tic Tac Toe


- TicTacToe
    - -Board board
    - -char currentMove
    - +makeMove(int row, int col)
    - -void changePlayer()

- Board
    - -char[][] board
    - +void initializeboard()
    - +void makeMove(int row, int col, char currentMove)
    - +boolean checkWin()
    - +boolean isBoardFull()



```python

```

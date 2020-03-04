# Specifications

Congratulations! You have been hired to join our FRA 241 company. We gladly present you
with your new project to prove your worth. Our company is expanding. We have several
warehouses located all around the company. Each warehouse has different capacity. However,
there is no system connected all the warehouse for the smart system. These are some
specifications of the warehouse.
### Warehouse Specifications
  - A warehouse has many rows.
  - A row is a 2-dimensional grid.
  - Each space in a grid is used to store an item.
  - Each warehouse has a robot to pick up and store items.
  - There are 5 warehouses. Warehouse 1 connects with a conveyor belt, Warehouse 2, and
    Warehouse 3. Warehouse 2 connects with Warehouse 4 and 5.
  - There is a robot running around to transfer items from a warehouse to a conveyor belt.
  - Warehouse 1, 2, and 3 have 5 rows of 10x10 grid.
  - Warehouse 4 has 7 rows of 5x5 grid.
  - Warehouse 5 has 20 rows of 20x20 grid.
  - The conveyor belt can hold up to 10 items, first-come-first-serve.
    You need to design a program such that
  - When received an order, a robot will pick up an item from a warehouse and transfer it
    to the belt.
  - When received an order, the belt will output 1 item at a time.
  - When received a command, a robot will store an item at a specific location.
Your job is to design a system to accomplish these requirements. I recommend that you should
utilize your Data Structure knowledge. Writing the program using Object Oriented
Programming can simplify your job, making your life easier.
Product ID
Each product has a unique id in a form of 4 characters: xyz
x represents a type of the item. It has a value of A to Y.
y represents a row number of the item. It has a value of 1 to 5.
z represents a row number of the item. It has a value of 00 to 99.
For example, a product id A125 should be at warehouse 1, row 1, and slot number 25.
### Input Command
There are several commands we can give to the system. The commands have following
formats.
- 0XXXX Retrieve a product id XXXX
- 1XXXX Store a product id XXXX
- 2XY00 Sort warehouse X at row Y
- 30000 Retrieve a product from the conveyor belt
- 40000 Output information of all warehouses
- 5XXXX Search for a product ID XXXX
- 9XXXXYYYY Manually put a product id XXXX at position YYYY
### Output
These are output formats for each of the command above.
- Retrieving command: 0XXXX
If the system can operate successfully, the system should print out the following
statements in this order:
  o Moving from Belt to A
  o Moving from A to C
  o Getting a product id XXXX from warehouse C: row y slot z
  o Moving from C to A
  o Moving from A to Start
  o Place product id XXXX on the belt
  o Retrieving Successfully!
If belt is full, the system should print out following statements:
  o Belt is full. Cannot retrieve the product
If slot is empty, the system should print out following statements:
  o Slot is empty. Cannot retrieve the product.
- Storing command: 1XXXX
If the system can operate successfully, the system should print out the following
statements in this order:
  o Moving from Belt to A
  o Moving from A to C
  o Storing a product id XXXX in warehouse C: row y slot z
  o Moving from C to A
  o Moving from A to Start
  o Storing Successfully!
If slot is unavailable, the system should print out following statements in this order:
  o Slot is occupied. Cannot store the product.
- Sorting command: 2XY00
If the system can operate successfully, the system should print out the following
statements in this order:
  o Sorting process for warehouse A is complete.
- Retrieving from the belt command: 30000
If the system can operate successfully, the system should print out the following
statements in this order:
o Retrieve a product with id XXXX from the belt.
o The belt now has x products on the line.
If there is nothing on the belt, the system should print out following statements in this
order:
o The belt is empty. Cannot retrieve the product from the belt.
- Warehouse Information: 40000
If the system can operate successfully, the system should print out the following
statements in this order:
o Warehouse A
o Numbers of Rows: 5
o Numbers of total products: 8
o Product in row 1: id A100, C108, E111
o Product in row 2: id –
o Product in row 3: id L355
o Product in row 4: id Q450
o Product in row 5: id U500, W501, Y502
- Searching for a product: 5XXXX
If the system can operate successfully, the system should print out the following
statements in this order:
o Found the product at XXXX.
If the system cannot find the product, the system should print out following statements
in this order:
o Product not found.
- Manually moving the product: 9XXXXYYYY
If the system can operate successfully, the system should print out the following
statements in this order:
o Move product XXXX to YYYY
If the slot is occupied, the system should print out following statements in this order:
o Slot is occupied. Failed to move.

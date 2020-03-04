# from Company import Company

class InputCommand:
    def __init__(self, company):
        self.company = company

    def getProductfromWarehouse(self, productId):
        com = self.company
        belt = self.company.belt
        if belt.isFull():
            return
        wID, row, grid = self.company.searchProduct(productId)
        if wID == -1:
            print("Slot is empty. Cannot retrieve the product.")
            return
        warehouse = self.company.warehouses[wID - 1]
        warehouse.retrieveProductfromWarehouse(row, grid)

        path = self.company.robot.getPath(wID)
        self.company.robot.pritGoTo(path)
        belt.addProduct(productId)
        print("Getting a product id " + str(productId) + " from warehouse " + com.warehouses[
            wID - 1].name + " row " + str(row) + " slot " + str(grid))
        self.company.robot.printGoBack(path)
        print("Retrieving Successfully! ")

    def sotringProductinWarehouse(self, productID, wID, row, grid):
        warehouse = self.company.warehouses[wID - 1]
        com = self.company
        if warehouse.checkSlot(row, grid) != "Z":
            print("Slot is occupied. Cannot store the product.")
            return
        path = self.company.robot.getPath(wID)
        warehouse.storeProduct(productID, row, grid)
        self.company.robot.pritGoTo(path)
        print(
            "Storing a product id " + str(productID) + " in warehouse " + com.warehouses[wID - 1].name + ": row " + str(
                row) + " slot " + str(grid))
        self.company.robot.printGoBack(path)
        print("Storing Successfully! ")

    def sort(self, wID, row):
        warehouse = self.company.warehouses[wID - 1]
        com = self.company
        warehouse.sort(row)
        print("Sorting process for warehouse " + com.warehouses[wID - 1].name + " is complete")

    def retrivingFromBelt(self):
        belt = self.company.belt
        item = belt.retrieveProductfromBelt()
        if item == None:
            return
        print("Retrieve a product with id " + str(item) + " from the belt. ")

    def printWarehouseInfo(self):
        for w in self.company.warehouses:
            w.printInfo()

    def searchWarehouse(self, productId):
        wId, row, grid = self.company.searchProduct(productId)
        if wId == -1:
            print("Product not found.")
            return
        print("Found the product at " + str(chr(wId + 64)) + str(row) + str(grid) + ".")

    def manuallyMove(self, wID1, row1, slot1, wID2, row2, slot2):
        warehouse = self.company.warehouses[wID2 - 1]
        if warehouse.checkSlot(row2, slot2) != "Z":
            print("Slot is occupied. Failed to move.")
            return
        warehouse = self.company.warehouses[wID1 - 1]
        product = warehouse.getProduct(row1, slot1)
        warehouse = self.company.warehouses[wID2 - 1]
        warehouse.storeProduct(product, row2, slot2)
        print("Move product " + str(chr(wID1 + 64)) + str(row1) + str(slot1) + " to " + str(chr(wID2 + 64)) + str(
            row2) + str(slot2) + ".")

    def inputCommand(self, command):
        com = self.company
        if command[0] == "0":
            productId = command[1:5]
            self.getProductfromWarehouse(productId)

        elif command[0] == "1":
            productId = command[1:5]
            w, row, slot = self.company.modLocation(productId)
            self.sotringProductinWarehouse(productId, w, row, slot)

        elif command[0] == "2":
            productId = command[1:5]
            w, row, slot = self.company.modLocation(productId)
            self.sort(w, row)

        elif command == "30000":
            self.retrivingFromBelt()

        elif command == "40000":
            self.printWarehouseInfo()

        elif command[0] == "5":
            productId = command[1:5]
            self.searchWarehouse(productId)

        elif command[0] == "9":
            productId = command[1:5]
            w, row, slot = self.company.modLocation(productId)
            wy = self.company.modLocation(command[5])
            new_place = command[5:9]
            wy, rowy, sloty = self.company.modLocation(new_place)
            self.manuallyMove(w, row, slot, wy, rowy, sloty)


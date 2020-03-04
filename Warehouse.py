# from Company import Company

class Warehouse:
    def __init__(self, name, row, slot):
        self.rows = [[]] * row
        self.count = 0
        self.name = name
        for i in range(0, len(self.rows)):
            self.rows[i] = ["Z"] * (slot * slot)

    def getName(self):  # get name of Warehouse
        return self.name

    def getNumberofRow(self):  # get number of row in warehouse
        return len(self.rows)

    def getNumberofSlot(self, row):  # get number of slot in row
        return len(self.rows[row - 1])

    def storeProduct(self, productId, row, grid,):  # Store
        if self.isEmpty(row, grid):
            self.rows[row - 1][grid] = productId
            self.count = self.count + 1
        elif self.isEmpty(row2, grid2):
            self.rows[row2 - 1][grid2] = productId
            self.count = self.count + 1
        else:
            print("Slot is occupied. Cannot store the product. ")

    def checkSlot(self, row, grid):  # What inside
        if grid > len(self.rows[row - 1]) - 1:
            return "Index out of range"
        return self.rows[row - 1][grid]

    def isEmpty(self, row, grid):
        return self.rows[row - 1][grid] == 'Z'

    def retrieveProductfromWarehouse(self, row, grid):
        self.count = self.count - 1
        product = self.rows[row - 1][grid]
        self.rows[row - 1][grid] = 'Z'
        return product

    def sort(self, row):
        self.rows[row - 1].sort()

    def getRow(self, row):
        return self.rows[row - 1]

    # def search(self,productId):
    #     pass

    def getNumberofProduct(self):
        return self.count

    def getProductinRow(self, row):
        productinrow = ""
        for p in self.rows[row - 1]:
            if p != "Z":
                productinrow = productinrow + p + ", "
        if productinrow == "":
            return "-"
        return productinrow[:-2]

    def printInfo(self):
        print("Warehouse " + self.name)
        print("Numbers of Rows: " + str(len(self.rows)))
        print("Numbers of total products: " + str(self.getNumberofProduct()))
        for i in range(0, len(self.rows)):
            print("Product in row " + str(i + 1) + " : id " + str(self.getProductinRow(i + 1)))

    def search(self, productId):
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                if self.rows[i][j] == productId:
                    return i + 1, j
        return -1, -1



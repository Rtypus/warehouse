from Warehouse import Warehouse
from Belt import Belt
from Robot import Robot
from InputCommand import InputCommand


class Company:
    def __init__(self):
        self.warehouses = [[]] * 5
        self.warehouses[0] = Warehouse("1", 5, 10)
        self.warehouses[1] = Warehouse("2", 5, 10)
        self.warehouses[2] = Warehouse("3", 5, 10)
        self.warehouses[3] = Warehouse("4", 7, 5)
        self.warehouses[4] = Warehouse("5", 20, 20)
        self.belt = Belt()
        self.robot = Robot()
        self.input = InputCommand(self)

    def getWarehousebyName(self, name):
        index = ord(name) - 65
        return self.warehouses[index]

    def searchProduct(self, productId):
        for index_warehouse in range(0, len(self.warehouses)):
            row, grid = self.warehouses[index_warehouse].search(productId)
            if row != -1:
                return index_warehouse + 1, row, grid
        return -1, -1, -1

    def inputCommand(self, cmd):
        self.input.inputCommand(cmd)

    def modLocation(self, productID):
        w = productID[0]
        r_s = productID[1]
        r = int(r_s)
        s_s = productID[2:4]
        s = int(s_s)
        as_w = ord(w)
        wID = ((ord(w) - 65) % 8)
        if as_w == 89:
            wID = 5
            if r == 1:
                return wID, r, s + 300
            if r == 2:
                return wID, r, s + 300
            if r == 3:
                return wID, r, s + 300
            if r == 4:
                return wID, r, s + 300
            if r == 5:
                return wID, r, s + 300

        elif wID == 0:
            wID = 1
            row = r
            return wID, row, s

        elif wID == 1:
            wID = 2
            row = r
            return wID, row, s

        elif wID == 2:
            wID = 3
            row = r
            return wID, row, s

        elif wID == 3:
            if as_w == 68:
                wID = 5
                r = r + 15
                return wID, r, s + 300
            elif as_w == 76:
                wID = 5
                r = r + 5
                return wID, r, s + 300
            elif as_w == 84:
                wID = 5
                r = r + 10
                return wID, r, s + 300

        elif wID == 4:
            wID = 5
            row = r
            if ((as_w - 1) % 9) - 3 == 0:
                return wID, row, s
            elif ((as_w - 1) % 9) - 3 == 1:
                return wID, row, s + 100
            elif ((as_w - 1) % 9) - 3 == 2:
                return wID, row, s + 200


        elif wID == 5:
            wID = 5
            row = r + 5
            if ((as_w - 1) % 9) - 4 == 0:
                return wID, row, s
            elif ((as_w - 1) % 9) - 4 == 1:
                return wID, row, s + 100
            elif ((as_w - 1) % 9) - 4 == 2:
                return wID, row, s + 200


        elif wID == 6:
            wID = 5
            row = r + 10
            if ((as_w - 1) % 9) - 5 == 0:
                return wID, row, s
            elif ((as_w - 1) % 9) - 5 == 1:
                return wID, row, s + 100
            elif ((as_w - 1) % 9) - 5 == 2:
                return wID, row, s + 200

        elif wID == 7:
            wID = 5
            row = r + 15
            if ((as_w - 1) % 9) - 6 == 0:
                return wID, row, s
            elif ((as_w - 1) % 9) - 6 == 1:
                return wID, row, s + 100
            elif ((as_w - 1) % 9) - 6 == 2:
                return wID, row, s + 200

    def modIfFull(self, productID):
        w = productID[0]
        r_s = productID[1]
        r = int(r_s)
        s_s = productID[2:4]
        s = int(s_s)
        as_w = ord(w)
        row = (as_w + r) % 7
        slot = s % 25
        wID = 4
        return wID, row, slot

    def allModLocation(self,productID):
        wID1,row1,slot1=self.modLocation(productID)
        wID2,row2,slot2=self.modIfFull(productID)
        return wID1,row1,slot1,wID2,row2,slot2
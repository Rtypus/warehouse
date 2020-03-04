class Belt:
    def __init__(self):
        self.que=[]

    def addProduct(self,productId):
        if self.isFull():
            print("Belt is full. Cannot retrieve the product")
            return
        self.que.append(productId)

    def retrieveProductfromBelt(self):
        if len(self.que)==0:
            print("The belt is empty. Cannot retrieve the product from the belt. ")
            return
        product=self.que.pop(0)
        print("The belt now has " + str(len(self.que)) + " products on the line.")
        return product

    def isFull(self):
        return len(self.que) == 10

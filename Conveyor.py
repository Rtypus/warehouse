class ConveyorBelt:

    def __init__(self):

        self.data=[]

    def push(self,data):
        l = len(self.data)
        #print(l)
        if l < 11:
            self.data.append(data)

    def pop(self,):
        data = self.data[len(self.data)-1]
        print(data)
        del self.data[len(self.data)-1]
        return data

    def print(self):
        print(self.data)

B=ConveyorBelt()

B.push(5)

B.push(6)

B.push(7)

B.push(8)

B.print()

B.pop()

B.print()

B.push(9)

B.pop()

B.print()

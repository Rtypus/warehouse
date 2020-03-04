class Robot:
    def __init__(self):
        self.path = []

    def getPath(self, wID):
        if wID == 1:
            return ["1"]
        elif wID == 2:
            return ["1", "2"]
        elif wID == 3:
            return ["1", "3"]
        elif wID == 4:
            return ["1", "2", "4"]
        elif wID == 5:
            return ["1", "2", "5"]

    def pritGoTo(self, path):
        print("Moving from Belt to 1")
        for i in range(0, len(path) - 1):
            print("Moving from " + path[i] + " to " + path[i + 1])

    def printGoBack(self, path):
        path = path[::-1]
        for i in range(0, len(path) - 1):
            print("Moving from " + path[i] + " to " + path[i + 1])
        print("Moving from 1 to Start")

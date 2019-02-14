class MyPowerList:

    def __init__(self, initialList=[]):
        if type(initialList) is list:
            self.pList = initialList
        else:
            raise ValueError("Constuctor parameter is not a list")

    
    '''def addItem(self, item):
        self.pList.append(item)

    def removeItem(self, index):
        try:
            del(self.pList[index])
        except Exception as e:
            print("Couldn't delete item: "+str(e))

    def sort(self):
        for x in range(len(self.pList)):
            current = self.pList[x]
            index = x
            while index > 0 and self.pList[index - 1] > current:
                self.pList[index] = self.pList[index - 1]
                index = index-1
            self.pList[index] = current

    def lMerge(self, mergeList):
        self.pList = mergeList+self.pList

    def rMerge(self, mergeList):
        self.pList = self.pList+mergeList

    def writeToFile(self, path):
        with open(path, 'w') as f:
            for item in self.pList:
                f.write("%s " % item)'''

    def readFromFile(self, path):
        with open(path, 'r') as f:
            self.pList = list(map(lambda x: int(x), f.read().split()))

    def printList(self):
        print(self.pList)




class FreeSegment:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.length = 0

class Memory:

    def __init__(self):
        # Assuming each index in the array corresponds to 1MB of free memory
        self.list = [None]*10
        print(str(len(self.list)) + ' MB allocated')
        self.segmentList = []

    def allocate(self, amount):
        if amount>len(self.list) or None not in self.list or self.list.count(None) < amount:
            print('Cannot allocate: Amount exceeds memory limit')
        else:
            i = 0
            while i < len(self.list):
                if self.list[i] is None:
                    newSeg = FreeSegment()
                    newSeg.start = i
                    j = i
                    while self.list[j] is None and i != len(self.list)-1:
                        if j == len(self.list)-1:
                            newSeg.end = j
                            if newSeg.end - newSeg.start + 1 >= amount:
                                self.segmentList.append(newSeg)
                                i = j
                                break
                        elif self.list[j+1] is not None:
                            newSeg.end = j
                            if newSeg.end - newSeg.start + 1 >= amount:
                                self.segmentList.append(newSeg)
                                i = j
                                break
                        else:
                            j += 1
                i += 1

            for i in range(len(self.segmentList)):
                min = len(self.list) + 1
                minIndex = 0
                if self.segmentList[i].length < min:
                    min = self.segmentList[i].length
                    minIndex = i

            # Allocate the memory
            alphabet = 'ABCDEFGHIJKLMNOPQRZTUVWXYZ'
            for i in range(len(alphabet)-1):
                if alphabet[i] not in self.list:
                    newLetter = alphabet[i]


                    start = self.segmentList[minIndex].start
                    k=start
                    for j in range(start,start + amount):
                        self.list[j] = newLetter
                    break
            self.segmentList.pop(0)
    def printList(self):
        print(self.list)

    def printSegList(self):
        for i in range(len(self.segmentList)):
            print('Start: '+str(self.segmentList[i].start))
            print('End: ' + str(self.segmentList[i].end))
            print('Length: ' + str(self.segmentList[i].length))

    def free(self, partName):
        for i in range(len(self.list)):
            if self.list[i] == partName:
                self.list[i] = None



m = Memory()
m.allocate(2)
m.allocate(3)
m.allocate(4)
m.free('B')
m.allocate(2)
m.free('C')
m.allocate(7)
m.printSegList()
print('PRINTING LIST')
m.printList()






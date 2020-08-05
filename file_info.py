
import math

def get_byteArr(file_obj):
    return map(ord,file_obj.read())

def get_freqList(byteArr, fileSize):
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr)/fileSize)
    return freqList

def get_entropy(freqList):
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent

class all:
    def __init__(self, file_name):
        f = open(file_name, "rb")
        self.byteArr = get_byteArr(f)
        f.close()
        self.fileSize = len(self.byteArr)
        self.freqList = get_freqList(self.byteArr, self.fileSize)
        self.entropy = get_entropy(self.freqList)

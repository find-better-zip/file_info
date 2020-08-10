
import math

def get_byteArr(file_obj):
    return list(file_obj.read()) # 파일의 문자열을 배열화 함

def get_fileSize(byteArr):
    return len(byteArr) # 파일의 문자열 길이를 수치화 함

def get_freqList(byteArr, fileSize):
    freqList = []  
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if ord(byte) == b:
                ctr += 1 # 파일 전체를 뒤져서 해당 아스키 코드와 일치하면 ctr의 값을 1씩 추가한다.
        freqList.append(float(ctr)/fileSize) # 해당 알파벳 갯수/(파일 크기)를 추가
    return freqList

def get_entropy(freqList):
    ent = 0.0 # 엔트로피 초기화
    for freq in freqList: 
        if freq > 0:
            ent += freq * math.log(freq, 0.5) * freq# freqList 리스트에서 -log_1/2(freq) 수행 후 ent 값을 더해줌
    return ent

class all:
    def __init__(self, file_obj):
        self.byteArr = get_byteArr(file_obj)
        self.fileSize = get_fileSize(self.byteArr)
        self.freqList = get_freqList(self.byteArr, self.fileSize)
        self.entropy = get_entropy(self.freqList)

if __name__=='__main__':
    file_name = str(input("file name : "))
    file = open(file_name,"r")
    info = all(file)
    file.close()
    print("fileSize :", info.fileSize,"(byte)")
    print("freqList :", info.freqList)
    print("entropy :", info.entropy)

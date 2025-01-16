import struct
import time


def main():
    start = time.time()
    for i in range(40):
        readFromFile("test.mp4", "mdat")
    print(time.time() - start)

    print(getBrandFromFile("test.mp4"))
    print(getCompatibleBrandFromFile("test.mp4"))
    print(getMinorBrandFromFile("test.mp4"))        

def readFromFile(inputFile, boxName):
    
    if not inputFile.endswith(".mp4"):
        return

    try:
        currentBox = ""
        with open(inputFile,"rb") as file:
            while currentBox != boxName :
                boxSize = file.read(4)
                if len(boxSize) < 4:
                        return "End of file"
                boxSize = struct.unpack(">I", boxSize)[0]
                currentBox = file.read(4).decode('utf-8')
                if currentBox == boxName:
                    file.read(boxSize - 8)
                else:
                    file.seek(boxSize - 8, 1)
    except:
        return

def getBrandFromFile(inputFile):
    brand = ""
    try:
        with open(inputFile,"rb") as file:
            file.seek(8, 0)
            brand = file.read(4).decode("utf-8")
    except:
        return
    
    return brand

def getCompatibleBrandFromFile(inputFile):
    brand = ""
    try:
        with open(inputFile,"rb") as file:
            file.seek(16, 0)
            brand = file.read(4).decode("utf-8")
    except:
        return 
    
    return brand

def getMinorBrandFromFile(inputFile):
    minorBrand = ""
    try:
        with open(inputFile,"rb") as file:
            file.seek(12, 0)
            minorBrand = struct.unpack(">I",file.read(4))[0]
    except:
        return
    
    return minorBrand



if __name__ == "__main__":
    main()
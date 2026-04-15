
from os.path import normpath

def fetchRawMPU8Code(name: str) -> str:
    
    fileName = f"MPU8Code/{name}.mpu8"
    
    file = open( normpath (fileName), "r")
    answer = file.read()
    file.close()
    
    return answer

def fetchRawURCLCode(name: str) -> str:
    
    fileName = f"MPU8Code/URCLCode/{name}.mpu8"
    
    file = open( normpath (fileName), "r")
    answer = file.read()
    file.close()
    
    return answer


def convertBinaryListToNumber(inst: list, instLength: int = 8) -> int:
    result:int = 0
    currentValue:int = 1 # we start at rightmost bit, (value = 1)
    for i in range(instLength-1, -1, -1):
        result+=currentValue*inst[i]
        currentValue*=2
    return result
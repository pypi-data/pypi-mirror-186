from subprocess import Popen
from random import randint
from sys import argv
import MakeOrBreak
import json

def runAsBackgroundProcess(mode, choice, interval):
   controllerFileLocation = MakeOrBreak.__path__[0] + "/controller.py" 
   Popen(['python3', controllerFileLocation, str(mode), str(choice), str(interval)])

def readDataFromFile(contentType):
   dataFileLocation = MakeOrBreak.__path__[0] + "/data.json"
   file = open(dataFileLocation)
   return json.load(file)['data'][contentType]

def generateRdmNumber(start, end):
   return randint(start, end)

def getSysArgs():
   return argv


if __name__ == "__main__":
   runAsBackgroundProcess()
   print(generateRdmNumber(0, 10))

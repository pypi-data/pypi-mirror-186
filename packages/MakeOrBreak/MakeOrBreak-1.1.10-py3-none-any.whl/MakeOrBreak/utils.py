import MakeOrBreak.config as config
import json

from subprocess import Popen, run
from random import randint
from sys import argv

def runAsBackgroundProcess(mode, intervalType, interval):
   Popen(['python3', config.CONTROLLER_FILE_LOCATION, str(mode), str(intervalType), str(interval)])

def runAsForegroundProcess(mode, intervalType, interval):
   run(['python3', config.CONTROLLER_FILE_LOCATION, str(mode), str(intervalType), str(interval)])

def readDataFromFile(contentType):
   file = open(config.DATA_FILE_LOCATION)
   return json.load(file)['data'][contentType]

def generateRdmNumber(start, end):
   return randint(start, end)

def getSysArgs():
   return argv


if __name__ == "__main__":
   runAsBackgroundProcess()
   print(generateRdmNumber(0, 10))

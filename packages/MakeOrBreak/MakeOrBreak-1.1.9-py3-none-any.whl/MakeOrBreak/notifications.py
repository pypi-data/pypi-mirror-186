from platform import system
import os

import MakeOrBreak.utils as utils
import MakeOrBreak.config as config
import MakeOrBreak.Exceptions.InvalidOSException as InvalidOSException


def determineNotificationContentType(mode):
   if mode == config.DIFFICULTY_MODE_MAPPING.get("Hard"):
      return config.CONTENT_TYPE[1]
   elif mode == config.DIFFICULTY_MODE_MAPPING.get("Normal"):
      return config.CONTENT_TYPE[utils.generateRdmNumber(0, len(config.CONTENT_TYPE) - 1)]
   elif mode == config.DIFFICULTY_MODE_MAPPING.get("Easy"):
      return config.CONTENT_TYPE[0]


def getNotificationContent(mode):
   contentType = determineNotificationContentType(mode)
   contentData = utils.readDataFromFile(contentType)

   return contentData[utils.generateRdmNumber(0, len(contentData) - 1)]

def createNotification(mode):
   content = getNotificationContent(mode)
   os_system = system()
   command = None

   if os_system == "Darwin":
      command = f'''
      osascript -e 'display notification "{content}" with title "MakeOrBreak"'
      '''
   elif os_system == "Linux":
      command = f'''
      notify-send "MakeOrBreak" "{content}"
      '''
   elif os_system == "Windows":
      raise InvalidOSException.InvalidOSException("Windows OS is currently not supported..")
   else:
      raise InvalidOSException.InvalidOSException("Unknown OS detected..")

   os.system(command)

if __name__ == "__main__":
   for i in range(10):
      createNotification()
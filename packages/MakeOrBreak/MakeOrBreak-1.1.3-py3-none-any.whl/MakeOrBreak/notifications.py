from platform import system
import os

import MakeOrBreak.utils as utils
import MakeOrBreak.mappings as mappings


def determineNotificationContentType(mode):
   if mode == mappings.DIFFICULTY_MODE_MAPPING.get("Hard"):
      return mappings.CONTENT_TYPE[1]
   elif mode == mappings.DIFFICULTY_MODE_MAPPING.get("Normal"):
      return mappings.CONTENT_TYPE[utils.generateRdmNumber(0, len(mappings.CONTENT_TYPE) - 1)]
   elif mode == mappings.DIFFICULTY_MODE_MAPPING.get("Easy"):
      return mappings.CONTENT_TYPE[0]


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
   else:
      raise Exception("Unknown OS detected..")

   os.system(command)


if __name__ == "__main__":
   for i in range(10):
      createNotification()
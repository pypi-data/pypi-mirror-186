import MakeOrBreak.utils as utils
import MakeOrBreak.config as config
import MakeOrBreak.configurations as configurations

def main():
   processRunType, mode, choice, interval = configurations.setConfiguration()
   print("\n Configurations set..")

   if processRunType == config.BACKGROUND_CONFIGURATION_MAPPING.get("Background"):
      utils.runAsBackgroundProcess(mode, choice, interval)
   else:
      utils.runAsForegroundProcess(mode, choice, interval)

if __name__ == "__main__":
   main()

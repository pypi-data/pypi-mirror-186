import MakeOrBreak.utils as utils
import MakeOrBreak.configurations as configurations

def main():
   mode, choice, interval = configurations.setConfiguration()
   print("\n Configurations set..")
   utils.runAsBackgroundProcess(mode, choice, interval)

if __name__ == "__main__":
   main()

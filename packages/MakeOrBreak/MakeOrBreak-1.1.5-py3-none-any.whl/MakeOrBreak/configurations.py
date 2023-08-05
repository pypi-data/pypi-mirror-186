import MakeOrBreak.config as config
import MakeOrBreak.utils as utils

def setConfiguration():
   valid = False

   while not valid:
      print("Please set up your app by selecting 1 of the following:")
      print("1. Proceed with default configurations (Random Intervals and Normal Mode)")
      print("2. Customise configurations")
      print("3. Exit")
      print("Note that you will not be able to change your selected configuration later in the same session")
      choice = input("(1/2/3): ")

      if choice == "1":
         mode = config.DIFFICULTY_MODE_MAPPING.get("Normal")
         intervalType = config.INTERVAL_TYPE_MAPPING.get("Random")
         interval = -1
      elif choice == "2":
         mode = setModeConfiguration()
         interval, intervalType = setIntervalConfiguration()
      elif choice == "3":
         quit()
      else:
         print("Invalid choice! Please read carefully before choosing your choice again!\n")
         continue

      processRunType = setBackgroundProcessConfiguration()

      return [processRunType, mode, intervalType, interval]


def setModeConfiguration():
   print("\nMode Configuration:")
   valid = False

   while not valid:
      print("1. Hard Mode - Only insults will be generated")
      print("2. Normal Mode - A mix of insults and compliments will be generated")
      print("3. Easy Mode - Only compliments will be generated")
      print("4. Exit")
      choice = int(input())

      if choice == 1:
         print("Hard Mode selected")
      elif choice == 2:
         print("Normal Mode selected")
      elif choice == 3:
         print("Easy Mode selected")
      elif choice == 4:
         quit()
      else:
         print("Invalid choice! Please read carefully before choosing your choice again!\n")
         continue

      return choice


def setIntervalConfiguration():
   print("\nInterval Configuration:")
   valid = False

   while not valid:
      print("1. For hourly notifications")
      print("2. To customise the interval")
      print("3. To randomise the interval")
      print("4. Exit")
      choice = int(input())

      # Hourly Reminders
      if choice == 1:
         interval = 3600
         print("App is now running on hourly intervals.")
      # Customer Reminders
      elif choice == 2:
         interval = int(input("Interval(in s): "))
         print(f"App is now running on an interval of {interval}s.")
      # Random intervals
      elif choice == 3:
         interval = -1
         print("App is now running on random intervals.")
      elif choice == 4:
         quit()
      # Wrong choice
      else:
         print("Invalid choice! Please read carefully before choosing your choice again!\n")
         continue

      return [choice, interval]


def setBackgroundProcessConfiguration():
   print("\nLastly, would you like to run this program in the Background?")
   print("*NOTE* If you choose to run this program in the background, you will have to manually kill this python3 process. Make sure you know how to perform this action before choosing this option")
   input("Press enter to continue...")

   valid = False
   while not valid:
      print("1. Yes, run in the Background")
      print("2. No, run in the Foreground")
      print("3. Exit")
      choice = int(input())

      if choice == 1:
         print("Program will now run in the background")
      elif choice == 2:
         print("Program will run in the Foreground. You may ctrl-c to quit and stop this program")
      elif choice == 3:
         quit()
      else:
         print("Invalid choice! Please read carefully before choosing your choice again!\n")
         continue

      return choice - 1

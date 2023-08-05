import MakeOrBreak

BACKGROUND_CONFIGURATION_MAPPING = {
   "Background": 0,
   "Foreground": 1
}

INTERVAL_TYPE_MAPPING = {
   "Hourly": 0,
   "Custom": 1,
   "Random": 2
}

DIFFICULTY_MODE_MAPPING = {
   "Hard": 0,
   "Normal": 1,
   "Easy": 2,
}

CONTENT_TYPE = ['compliments', 'insults']

CONTROLLER_FILE_LOCATION = MakeOrBreak.__path__[0] + "/controller.py"
DATA_FILE_LOCATION = MakeOrBreak.__path__[0] + "/data.json"
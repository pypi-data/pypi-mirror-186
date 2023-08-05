import time

import MakeOrBreak.mappings as mappings
import MakeOrBreak.utils as utils
import MakeOrBreak.notifications as notifications

def timer(): 
	mode = int(utils.getSysArgs()[1]) - 1
	intervalType = int(utils.getSysArgs()[2])
	interval = int(utils.getSysArgs()[3])

	#'1' hourly interval reminders
	#'2' custom interval
	#'3' random interval reminders

	while True:
		notifications.createNotification(mode)

		randomTime = utils.generateRdmNumber(0, 3600)
		if intervalType == mappings.INTERVAL_TYPE_MAPPING.get("Hourly"):
			time.sleep(3600)
		elif intervalType == mappings.INTERVAL_TYPE_MAPPING.get("Custom"):
			time.sleep(interval)
		else:
			time.sleep(randomTime)


if __name__ == "__main__":
	timer()

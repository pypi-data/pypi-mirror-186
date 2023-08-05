import time

import MakeOrBreak.utils as utils
import MakeOrBreak.config as config
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

		randomTime = utils.generateRdmNumber(0, 1800)
		if intervalType == config.INTERVAL_TYPE_MAPPING.get("Hourly"):
			time.sleep(3600)
		elif intervalType == config.INTERVAL_TYPE_MAPPING.get("Custom"):
			time.sleep(interval)
		else:
			time.sleep(randomTime)


if __name__ == "__main__":
	timer()

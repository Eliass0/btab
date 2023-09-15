import os
import glob
import requests
import time
import json
import numpy

current_directory = os.getcwd()


def check_wav_files():
	wav_files = glob.glob(os.path.join(current_directory, '*.wav'))
	num_wav_files = len(wav_files)
	return num_wav_files

def check_checkpoint_files():
	checkpoint_files = glob.glob(os.path.join(current_directory, '*.checkpoint'))
	num_checkpoint_files = len(wav_files)
	return num_checkpoint_files

def calculate_progress():
	raw = check_wav_files()/check_checkpoint_files()
	rounded = round(raw, 3)
	progress = round((rounded*100),2)
	return progress

def post_message(message):
	# Replace 'YOUR_WEBHOOK_URL' with the actual webhook URL you obtained in step 1.
	webhook_url = "YOUR_WEBHOOK_URL"

	# Create a payload containing the message you want to send.
	payload = {
	    'content': message
	}

	# Convert the payload to JSON.
	headers = {
	    'Content-Type': 'application/json'
	}

	response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

	# Check the response status code.
	if response.status_code == 204:
	    print("Message sent successfully: \n'" + message + "'")
	else:
	    print('Failed to send message. Status code: ', response.status_code)

def log_message(message):
	print("Message: \n'" + message + "'")

def main():
	current_progress = calculate_progress()
	post_message("Watcher now online.\nCurrent Progress: " + str(current_progress) + "%")
	delay = 900
	while(True):
		time.sleep(delay)
		# How much progress has been made since last check
		delta = round((calculate_progress() - current_progress),5)
		# Save current progress to varialbe for next operations
		current_progress = calculate_progress()
		# Calculate the speed at which the progress is made
		percent_per_second = delta/delay
		if(delta != 0): # If there is any progress make ETA calculations
			seconds_per_percent = numpy.reciprocal(percent_per_second)
			progress_left = 100 - current_progress

			time_left_in_seconds = progress_left * seconds_per_percent
			time_left_in_minutes = time_left_in_seconds / 60
			time_left_in_hours = time_left_in_minutes / 60
		else:
			time_left_in_seconds = "NaN"
			time_left_in_minutes = "NaN"
			time_left_in_hours = "NaN"



		


		post_message(
			"Current Progress: " + str(current_progress) + "%\n" + 
			"Pace: " + str(delta) + "%/" + str(delay) + "sec\n" + 
			"Time Left: " + str(int(time_left_in_minutes)) + " minutes"
			)

main()
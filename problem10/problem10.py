import datetime

def surpise():
	print("SURPRISE")

def wait_millis(f, duration):
	seconds = duration / 1000
	milliseconds = duration % 1000	

	# Get a datetime object for the current time
	current_time = datetime.datetime.now()
	execute_time = current_time + datetime.timedelta(0, seconds, milliseconds)
	
	while(True):
		current_time = datetime.datetime.now() 
		
		if (current_time > execute_time):
			f()

			return

def main():
	duration = int(input("How many milliseconds should we wait: "))
	wait_millis(surpise, duration)

if __name__ == '__main__':
	main()

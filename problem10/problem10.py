import datetime
from sys import argv

def surpise():
	print("Function Call")

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
	if (len(argv) < 2):
		print('Please enter the number of milliseconds')
		return

	duration = int(argv[1])
	wait_millis(surpise, duration)

if __name__ == '__main__':
	main()

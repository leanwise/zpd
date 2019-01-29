import time
import threading



def handle_client():
	time.sleep(0.025)

count = 0


with open('clients.txt', 'r') as f:
	start = time.time()
	for client in f:
		threading.Thread(target=handle_client).start()
	end = time.time()

print("Time:", end-start)
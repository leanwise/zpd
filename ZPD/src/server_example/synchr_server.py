import time

def handle_client():
	time.sleep(0.025)

start = time.time()
with open('clients.txt', 'r') as f:
	for client in f:
		handle_client()
end = time.time()

print("Time:", end-start)
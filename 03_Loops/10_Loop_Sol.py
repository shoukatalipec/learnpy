import time

max_tries = 3
wait_time = 1
attemps = 0

while attemps <= max_tries:
  print("Attempts",attemps+1,"- wait time", wait_time)
  time.sleep(wait_time)
  wait_time *= 2
  attemps += 1
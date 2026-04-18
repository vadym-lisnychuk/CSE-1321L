import time

Timestamp = int(input("Enter the timestamp in seconds: "))
print(f"Timestamp: {Timestamp}")
print(f"Date and time: {time.ctime(Timestamp)}")
sleeper = int(input("Enter pause length in seconds: "))
print("Waiting...")
time.sleep(sleeper)
print("Done!")
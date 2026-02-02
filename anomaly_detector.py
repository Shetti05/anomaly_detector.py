import random
import statistics
import time

data = []

while True:
    value = random.randint(30, 90)
    data.append(value)

    if len(data) > 20:
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)

        if value > mean + 2 * stdev:
            print(f"🚨 Anomaly Detected: {value}")
        else:
            print(f"Normal value: {value}")

        data.pop(0)

    time.sleep(2)

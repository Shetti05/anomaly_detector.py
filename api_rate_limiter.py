import time
from collections import defaultdict

RATE_LIMIT = 5  # requests
WINDOW = 60     # seconds

users = defaultdict(list)

def request(user_id):
    current_time = time.time()
    users[user_id] = [t for t in users[user_id] if current_time - t < WINDOW]

    if len(users[user_id]) < RATE_LIMIT:
        users[user_id].append(current_time)
        print(f"✅ Request allowed for {user_id}")
    else:
        print(f"❌ Rate limit exceeded for {user_id}")

# Simulation
for i in range(10):
    request("user_1")
    time.sleep(5)

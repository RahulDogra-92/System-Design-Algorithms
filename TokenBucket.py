# Description:
# Leaky Bucket and Token Bucket are algorithms used for rate limiting. The Leaky Bucket algorithm processes requests at a fixed rate, while the Token Bucket allows for bursts of requests.

# Use Case: Rate limiting API requests
# Python Example (Token Bucket):

import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def consume(self, tokens=1):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        else:
            return False

bucket = TokenBucket(10, 1)  # 10 tokens capacity, 1 token/sec refill rate

# Simulate API requests
for _ in range(20):
    if bucket.consume():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(0.3)

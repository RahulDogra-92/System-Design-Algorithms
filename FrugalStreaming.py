# Description:
# Frugal Streaming is an algorithm designed for efficient quantile computation in streaming data, particularly useful for real-time systems where memory is constrained.

# Use Case: Real-time monitoring of website response times
# Python Example:

import random

class FrugalQuantile:
    def __init__(self, quantile):
        self.quantile = quantile
        self.estimate = None

    def update(self, value):
        if self.estimate is None:
            self.estimate = value
        elif value > self.estimate:
            if random.random() > (1 - self.quantile):
                self.estimate += 1
        elif value < self.estimate:
            if random.random() > self.quantile:
                self.estimate -= 1

    def get_estimate(self):
        return self.estimate

# Simulate streaming response times
stream = [random.uniform(100, 500) for _ in range(1000)]
frugal = FrugalQuantile(quantile=0.5)  # Median

for response_time in stream:
    frugal.update(response_time)

print(f"Estimated median response time: {frugal.get_estimate()} ms")

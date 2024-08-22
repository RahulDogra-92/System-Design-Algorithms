# Description:
# Lossy Count is an algorithm for finding frequently occurring items in a data stream, with some allowance for error to save memory.

# Use Case: Identifying trending topics on social media
# Python Example:

from collections import defaultdict

class LossyCount:
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.freq = defaultdict(int)
        self.delta = defaultdict(int)
        self.total_items = 0

    def add(self, item):
        self.total_items += 1
        if item in self.freq:
            self.freq[item] += 1
        else:
            self.freq[item] = 1 + self.delta.get(item, 0)
        
        if self.total_items % (1/self.epsilon) == 0:
            for key in list(self.freq):
                if self.freq[key] + self.delta[key] <= self.total_items * self.epsilon:
                    del self.freq[key]
                    del self.delta[key]

    def get_frequent_items(self):
        return {k: v for k, v in self.freq.items() if v >= self.total_items * self.epsilon}

lossy = LossyCount(epsilon=0.01)

# Simulate a data stream of hashtags
hashtags = ["#python", "#ai", "#datascience", "#ai", "#python", "#ai"]

for tag in hashtags:
    lossy.add(tag)

print("Frequent items:", lossy.get_frequent_items())

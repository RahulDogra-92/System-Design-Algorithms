# Description:
# A Bloom Filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It can return false positives but never false negatives. It’s often used when space is limited and some level of uncertainty is acceptable.

# Use Case: Checking if a username is available
# Python Example:


from bloom_filter2 import BloomFilter

# Initialize Bloom Filter with desired capacity and error rate
bloom = BloomFilter(max_elements=1000, error_rate=0.1)

# Add some usernames to the filter
usernames = ["alice", "bob", "charlie"]
for username in usernames:
    bloom.add(username)

# Check if a username is already taken
def is_username_available(username):
    if username in bloom:
        return False
    else:
        return True

print(is_username_available("alice"))  # Output: False
print(is_username_available("eve"))    # Output: True

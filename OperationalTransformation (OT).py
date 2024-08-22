# Description:
# Operational Transformation is a technique that allows for concurrent edits in shared documents while maintaining consistency across all copies.

# Use Case: Collaborative text editors
# Python Example:

class Document:
    def __init__(self):
        self.content = ""

    def apply(self, operation):
        position, char, action = operation
        if action == "insert":
            self.content = self.content[:position] + char + self.content[position:]
        elif action == "delete":
            self.content = self.content[:position] + self.content[position+1:]

# Simulate a document and operations
doc = Document()
operations = [(0, "H", "insert"), (1, "i", "insert"), (2, "!", "insert")]

for op in operations:
    doc.apply(op)

print(f"Document content: {doc.content}")

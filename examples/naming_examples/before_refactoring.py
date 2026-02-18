"""
Example: Poor Naming Practices
This file demonstrates common naming mistakes that should be avoided.
"""

# ❌ BAD: Generic and unclear variable names
x = 100
y = 50
z = x + y

# ❌ BAD: Single letter for important data
d = {"Alice": 85, "Bob": 92, "Charlie": 78}
l = ["apple", "banana", "cherry"]

# ❌ BAD: Unclear function names
def calc(a, b):
    return a + b

def getData():
    return ["user1", "user2", "user3"]

def process(x):
    return x * 2

# ❌ BAD: Abbreviated and cryptic names
usr_nm = "John Doe"
usr_age = 30
usr_addr = "123 Main St"

# ❌ BAD: Non-descriptive boolean
flag = True
status = False

# ❌ BAD: Generic class name with unclear purpose
class Manager:
    def __init__(self):
        self.data = []
    
    def add(self, item):
        self.data.append(item)
    
    def get(self):
        return self.data

# ❌ BAD: Meaningless temp variables
def calculate():
    temp1 = 10
    temp2 = 20
    temp3 = temp1 + temp2
    return temp3

# ❌ BAD: Function that doesn't describe what it does
def doStuff(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

# ❌ BAD: Unclear purpose
def check(email):
    return "@" in email and "." in email

# Using the poorly named code
if __name__ == "__main__":
    print(f"Total: {z}")
    print(f"Data: {d}")
    print(f"User: {usr_nm}, Age: {usr_age}")
    
    mgr = Manager()
    mgr.add("item1")
    mgr.add("item2")
    print(mgr.get())
    
    print(doStuff(10))
    print(check("test@example.com"))

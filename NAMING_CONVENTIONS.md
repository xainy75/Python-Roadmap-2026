# Python Naming Conventions Guide

## 📝 Overview

This guide demonstrates best practices for naming variables and functions in Python, following PEP 8 guidelines and industry standards.

## 🎯 General Principles

### 1. **Be Descriptive and Clear**
- Names should reveal intent and purpose
- Avoid abbreviations unless universally understood
- Use full words instead of single letters (except in specific contexts)

### 2. **Be Consistent**
- Follow the same naming patterns throughout your codebase
- Use established conventions for your project

### 3. **Be Concise but Not Cryptic**
- Balance between descriptive and overly verbose
- Remove unnecessary words

---

## 📦 Variable Naming

### Snake Case for Variables
Python uses `snake_case` for variable names (lowercase with underscores).

#### ❌ Bad Examples
```python
x = 10                           # Too vague
n = "John"                       # Non-descriptive
temp = 25.5                      # Ambiguous
data = [1, 2, 3]                # Generic
usrAge = 30                      # Wrong case (camelCase)
UserName = "Alice"               # Wrong case (PascalCase)
```

#### ✅ Good Examples
```python
user_count = 10
student_name = "John"
temperature_celsius = 25.5
student_grades = [1, 2, 3]
user_age = 30
username = "Alice"
```

### Specific Variable Types

#### Boolean Variables
Use descriptive names that indicate true/false state, often prefixed with `is_`, `has_`, `can_`, `should_`.

```python
# ❌ Bad
active = True
logged = False
admin = True

# ✅ Good
is_active = True
is_logged_in = False
has_admin_privileges = True
can_edit = False
should_validate = True
```

#### Collections (Lists, Sets, Tuples)
Use plural nouns to indicate multiple items.

```python
# ❌ Bad
student = ["Alice", "Bob", "Charlie"]
number = [1, 2, 3, 4, 5]
data = {"key1": "value1"}

# ✅ Good
students = ["Alice", "Bob", "Charlie"]
prime_numbers = [1, 2, 3, 4, 5]
user_preferences = {"key1": "value1"}
active_connections = set()
```

#### Constants
Use `UPPER_CASE_WITH_UNDERSCORES` for constants.

```python
# ❌ Bad
max = 100
pi = 3.14159
apikey = "abc123"

# ✅ Good
MAX_CONNECTIONS = 100
PI = 3.14159
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30
```

---

## 🔧 Function Naming

### Snake Case for Functions
Python uses `snake_case` for function names (lowercase with underscores).

#### ❌ Bad Examples
```python
def calc():                      # Too vague
    pass

def getData():                   # Wrong case (camelCase)
    pass

def process():                   # Not specific
    pass

def x():                         # Meaningless
    pass

def doStuff():                   # Vague and wrong case
    pass
```

#### ✅ Good Examples
```python
def calculate_total_price():
    pass

def get_user_data():
    pass

def process_payment():
    pass

def validate_email_address():
    pass

def send_notification():
    pass
```

### Function Name Patterns

#### Actions: Use Verbs
Functions should start with action verbs that describe what they do.

```python
# ❌ Bad
def user(name):
    pass

def email():
    pass

# ✅ Good
def create_user(name):
    pass

def send_email():
    pass

def validate_input():
    pass

def update_database():
    pass
```

#### Queries: Use `get_`, `find_`, `fetch_`
For functions that retrieve data.

```python
# ❌ Bad
def user_by_id(user_id):
    pass

def data():
    pass

# ✅ Good
def get_user_by_id(user_id):
    pass

def fetch_customer_data():
    pass

def find_matching_records():
    pass
```

#### Boolean Functions: Use `is_`, `has_`, `can_`, `should_`
For functions returning boolean values.

```python
# ❌ Bad
def valid(email):
    pass

def admin(user):
    pass

# ✅ Good
def is_valid_email(email):
    pass

def has_admin_access(user):
    pass

def can_delete_file(user, file):
    pass

def should_retry(attempt_count):
    pass
```

---

## 📋 Class Naming

Use `PascalCase` (CapitalizedWords) for class names.

```python
# ❌ Bad
class user:
    pass

class student_record:
    pass

class dataProcessor:
    pass

# ✅ Good
class User:
    pass

class StudentRecord:
    pass

class DataProcessor:
    pass

class EmailValidator:
    pass
```

---

## 🎓 Context-Specific Guidelines

### Loop Variables

#### Short Loops (1-3 lines)
Single letters are acceptable for simple, short loops.

```python
# ✅ Acceptable for short, simple loops
for i in range(10):
    print(i)

for x, y in coordinates:
    print(x, y)
```

#### Longer Loops
Use descriptive names for better readability.

```python
# ✅ Better for longer or nested loops
for student_index in range(len(students)):
    student = students[student_index]
    # ... more complex logic

for row_number in range(grid_height):
    for column_number in range(grid_width):
        # ... process grid cell
```

### Private Methods and Variables
Use single leading underscore for internal use.

```python
class UserManager:
    def __init__(self):
        self._connection = None    # Internal variable
    
    def _validate_credentials(self):    # Internal method
        pass
    
    def login_user(self):    # Public method
        self._validate_credentials()
```

---

## 🚫 Common Mistakes to Avoid

1. **Single Letter Variables** (except in specific contexts)
   ```python
   # ❌ Bad
   a = 10
   b = 20
   c = a + b
   
   # ✅ Good
   width = 10
   height = 20
   area = width + height
   ```

2. **Abbreviations**
   ```python
   # ❌ Bad
   usr_nm = "Alice"
   calc_avg = lambda x: sum(x) / len(x)
   
   # ✅ Good
   username = "Alice"
   calculate_average = lambda x: sum(x) / len(x)
   ```

3. **Meaningless Names**
   ```python
   # ❌ Bad
   temp = fetch_data()
   data = process(temp)
   result = save(data)
   
   # ✅ Good
   raw_user_data = fetch_data()
   validated_user_data = process(raw_user_data)
   save_status = save(validated_user_data)
   ```

4. **Generic Names**
   ```python
   # ❌ Bad
   list1 = [1, 2, 3]
   list2 = ["a", "b", "c"]
   
   # ✅ Good
   student_ids = [1, 2, 3]
   course_codes = ["a", "b", "c"]
   ```

---

## 📚 Quick Reference

| Type | Convention | Example |
|------|-----------|---------|
| Variable | `snake_case` | `user_count`, `total_price` |
| Function | `snake_case` | `calculate_total()`, `get_user()` |
| Class | `PascalCase` | `UserManager`, `DataProcessor` |
| Constant | `UPPER_CASE` | `MAX_SIZE`, `API_KEY` |
| Private | `_leading_underscore` | `_internal_method()` |
| Boolean | `is_/has_/can_` prefix | `is_active`, `has_permission` |

---

## 🔗 References

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [PEP 8 - Naming Conventions](https://pep8.org/#naming-conventions)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

## 💡 Remember

> "Programs must be written for people to read, and only incidentally for machines to execute."
> — Harold Abelson

Clear, descriptive names make your code:
- ✅ Easier to understand
- ✅ Easier to maintain
- ✅ Easier to debug
- ✅ More professional
- ✅ Self-documenting

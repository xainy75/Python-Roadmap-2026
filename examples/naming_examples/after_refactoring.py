"""
Example: Good Naming Practices
This file demonstrates the same functionality with improved, descriptive names.
"""

# ✅ GOOD: Clear and descriptive variable names
product_price = 100
shipping_cost = 50
total_cost = product_price + shipping_cost

# ✅ GOOD: Descriptive names for collections
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
available_fruits = ["apple", "banana", "cherry"]

# ✅ GOOD: Clear function names with action verbs
def calculate_sum(first_number, second_number):
    """Calculate the sum of two numbers."""
    return first_number + second_number

def get_user_list():
    """Retrieve a list of all registered users."""
    return ["user1", "user2", "user3"]

def double_value(value):
    """Double the input value."""
    return value * 2

# ✅ GOOD: Full, descriptive variable names
user_full_name = "John Doe"
user_age = 30
user_address = "123 Main St"

# ✅ GOOD: Descriptive boolean with clear meaning
is_account_active = True
has_completed_registration = False

# ✅ GOOD: Specific class name that describes purpose
class TaskManager:
    """Manages a list of tasks for a user."""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the task list."""
        self.tasks.append(task)
    
    def get_all_tasks(self):
        """Retrieve all tasks."""
        return self.tasks

# ✅ GOOD: Meaningful variable names
def calculate_rectangle_area():
    """Calculate the area of a rectangle."""
    width = 10
    height = 20
    area = width + height
    return area

# ✅ GOOD: Function name clearly describes the action
def get_even_numbers(count):
    """
    Generate a list of even numbers up to the specified count.
    
    Args:
        count: Maximum number to check for even values
        
    Returns:
        List of even numbers from 0 to count-1
    """
    even_numbers = []
    for number in range(count):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# ✅ GOOD: Boolean function with clear purpose
def is_valid_email(email_address):
    """
    Validate if an email address has basic required components.
    
    Args:
        email_address: Email string to validate
        
    Returns:
        True if email contains @ and ., False otherwise
    """
    has_at_symbol = "@" in email_address
    has_dot = "." in email_address
    return has_at_symbol and has_dot

# Using the well-named code
if __name__ == "__main__":
    print(f"Total cost: ${total_cost}")
    print(f"Student grades: {student_grades}")
    print(f"User: {user_full_name}, Age: {user_age}")
    
    task_manager = TaskManager()
    task_manager.add_task("Complete homework")
    task_manager.add_task("Review Python concepts")
    print(f"Tasks: {task_manager.get_all_tasks()}")
    
    print(f"Even numbers: {get_even_numbers(10)}")
    print(f"Valid email: {is_valid_email('test@example.com')}")

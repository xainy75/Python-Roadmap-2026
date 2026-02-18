# Naming Conventions Examples

This directory contains practical examples demonstrating proper naming conventions in Python.

## 📁 Files

### 1. `before_refactoring.py`
Shows common naming mistakes and poor practices that should be avoided:
- Generic variable names (x, y, z)
- Single letters for important data
- Unclear function names
- Abbreviated names
- Non-descriptive booleans

### 2. `after_refactoring.py`
Shows the same code refactored with proper naming conventions:
- Descriptive variable names
- Clear function names with action verbs
- Meaningful boolean names
- Well-named classes and methods

### 3. `user_management.py`
Real-world example of a user management system demonstrating:
- Class naming (User, UserManager)
- Method naming (create_user, authenticate_user, find_user_by_username)
- Boolean methods (is_valid_username, is_valid_email, is_valid_password)
- Constants (MAX_LOGIN_ATTEMPTS, SESSION_TIMEOUT_MINUTES)
- Descriptive variable names throughout

### 4. `data_processing.py`
Real-world example of data processing with proper naming:
- Class naming (DataValidator, DataProcessor, FileHandler)
- Method naming (process_records, calculate_success_rate, filter_records_by_threshold)
- Clear parameter names
- Descriptive internal variables

## 🎯 How to Use These Examples

1. **Study the comparison**: Compare `before_refactoring.py` with `after_refactoring.py` to see the impact of good naming.

2. **Run the examples**: Execute each file to see how the code works:
   ```bash
   python before_refactoring.py
   python after_refactoring.py
   python user_management.py
   python data_processing.py
   ```

3. **Learn from patterns**: Notice the patterns:
   - Variables use `snake_case`
   - Functions use action verbs
   - Classes use `PascalCase`
   - Constants use `UPPER_CASE`
   - Boolean variables/functions start with `is_`, `has_`, `can_`, etc.

4. **Apply to your code**: Use these patterns in your own Python projects.

## 📚 Additional Resources

For comprehensive guidelines, see the main [NAMING_CONVENTIONS.md](../../NAMING_CONVENTIONS.md) document.

"""
Example: User Management System
Demonstrates proper naming conventions in a real-world scenario.
"""

from typing import List, Dict, Optional
from datetime import datetime


# Constants with clear names
MAX_LOGIN_ATTEMPTS = 3
SESSION_TIMEOUT_MINUTES = 30
MIN_PASSWORD_LENGTH = 8


class User:
    """Represents a user in the system."""
    
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.is_active = True
        self.is_verified = False
        self.created_at = datetime.now()
        self.last_login = None
        self.failed_login_attempts = 0
    
    def __repr__(self):
        return f"User(id={self.user_id}, username={self.username})"


class UserManager:
    """Manages user operations including creation, authentication, and retrieval."""
    
    def __init__(self):
        self.users: List[User] = []
        self.active_sessions: Dict[int, datetime] = {}
    
    def create_user(self, username: str, email: str, password: str) -> Optional[User]:
        """
        Create a new user account.
        
        Args:
            username: Desired username for the account
            email: User's email address
            password: User's password
            
        Returns:
            Created User object if successful, None otherwise
        """
        if not self.is_valid_username(username):
            print(f"Invalid username: {username}")
            return None
        
        if not self.is_valid_email(email):
            print(f"Invalid email: {email}")
            return None
        
        if not self.is_valid_password(password):
            print(f"Password does not meet requirements")
            return None
        
        user_id = len(self.users) + 1
        new_user = User(user_id, username, email)
        self.users.append(new_user)
        
        print(f"User created successfully: {username}")
        return new_user
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate a user with username and password.
        
        Args:
            username: Username to authenticate
            password: Password to verify
            
        Returns:
            True if authentication successful, False otherwise
        """
        user = self.find_user_by_username(username)
        
        if user is None:
            print(f"User not found: {username}")
            return False
        
        if not user.is_active:
            print(f"User account is not active: {username}")
            return False
        
        if user.failed_login_attempts >= MAX_LOGIN_ATTEMPTS:
            print(f"Account locked due to too many failed attempts: {username}")
            return False
        
        # In a real system, you would verify password hash here
        is_password_correct = self._verify_password(password)
        
        if is_password_correct:
            user.last_login = datetime.now()
            user.failed_login_attempts = 0
            self.active_sessions[user.user_id] = datetime.now()
            print(f"Login successful: {username}")
            return True
        else:
            user.failed_login_attempts += 1
            print(f"Invalid password for user: {username}")
            return False
    
    def find_user_by_username(self, username: str) -> Optional[User]:
        """
        Find a user by their username.
        
        Args:
            username: Username to search for
            
        Returns:
            User object if found, None otherwise
        """
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def find_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Find a user by their ID.
        
        Args:
            user_id: User ID to search for
            
        Returns:
            User object if found, None otherwise
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def get_active_users(self) -> List[User]:
        """
        Retrieve all active users.
        
        Returns:
            List of active User objects
        """
        active_users = [user for user in self.users if user.is_active]
        return active_users
    
    def deactivate_user(self, user_id: int) -> bool:
        """
        Deactivate a user account.
        
        Args:
            user_id: ID of the user to deactivate
            
        Returns:
            True if successful, False otherwise
        """
        user = self.find_user_by_id(user_id)
        
        if user is None:
            print(f"User not found with ID: {user_id}")
            return False
        
        user.is_active = False
        print(f"User deactivated: {user.username}")
        return True
    
    def is_valid_username(self, username: str) -> bool:
        """Check if username meets requirements."""
        min_length = 3
        max_length = 20
        
        if len(username) < min_length or len(username) > max_length:
            return False
        
        if not username.isalnum():
            return False
        
        return True
    
    def is_valid_email(self, email: str) -> bool:
        """Check if email address is valid."""
        has_at_symbol = "@" in email
        has_dot = "." in email
        return has_at_symbol and has_dot
    
    def is_valid_password(self, password: str) -> bool:
        """Check if password meets security requirements."""
        return len(password) >= MIN_PASSWORD_LENGTH
    
    def _verify_password(self, password: str) -> bool:
        """
        Internal method to verify password hash.
        In a real system, this would check against stored hash.
        """
        # Simplified for demonstration
        return len(password) >= MIN_PASSWORD_LENGTH


# Example usage
if __name__ == "__main__":
    # Initialize the user manager
    user_manager = UserManager()
    
    # Create new users
    print("=== Creating Users ===")
    alice = user_manager.create_user("alice123", "alice@example.com", "SecurePass123")
    bob = user_manager.create_user("bob456", "bob@example.com", "BobPassword456")
    
    # Authenticate users
    print("\n=== Authenticating Users ===")
    user_manager.authenticate_user("alice123", "SecurePass123")
    user_manager.authenticate_user("bob456", "WrongPassword")  # Should fail
    
    # Find users
    print("\n=== Finding Users ===")
    found_user = user_manager.find_user_by_username("alice123")
    if found_user:
        print(f"Found user: {found_user}")
    
    # Get active users
    print("\n=== Active Users ===")
    active_users = user_manager.get_active_users()
    print(f"Number of active users: {len(active_users)}")
    for user in active_users:
        print(f"  - {user.username} (ID: {user.user_id})")
    
    # Deactivate a user
    print("\n=== Deactivating User ===")
    if alice:
        user_manager.deactivate_user(alice.user_id)

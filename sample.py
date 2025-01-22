from datetime import datetime
from typing import Tuple

def get_greeting_and_time() -> Tuple[str, str]:
    """
    Determines appropriate greeting based on time of day and formats current time.
    
    Returns:
        Tuple[str, str]: A tuple containing (greeting message, formatted time)
    """
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        hour = now.hour

        greetings = {
            range(0, 12): "Good morning",
            range(12, 18): "Good afternoon",
            range(18, 24): "Good evening"
        }

        greeting = next((message for time_range, message in greetings.items() 
                        if hour in time_range), "Hello")  # Default fallback

        return greeting, current_time

    except Exception as e:
        print(f"Error getting time/greeting: {e}")
        return "Hello", "Unknown time"

def greet_user(name: str = "Friend") -> None:
    """
    Greets user with appropriate time-based message.
    
    Args:
        name (str): Name of the person to greet. Defaults to "Friend"
    """
    try:
        greeting, current_time = get_greeting_and_time()
        
        print(f"Hello, {name}!")
        print(f"The time is {current_time}.")
        print(f"{greeting}!")
        
    except Exception as e:
        print("Sorry, there was an error generating your greeting.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    # Example usage
    greet_user()
    # Custom name: greet_user("Gloria")
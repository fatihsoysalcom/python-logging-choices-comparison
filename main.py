import logging
import sys

# --- Choice 1: Simple 'print()' statements ---
# This is the most basic "free choice". Easy to use, no setup.
# Good for quick scripts, debugging, or very small projects.
def perform_task_with_print(data):
    print(f"INFO: Processing data: {data}") # Simple info
    result = data * 2
    print(f"DEBUG: Intermediate result: {result}") # Simple debug
    if result > 10:
        print(f"WARNING: Result {result} is high!") # Simple warning
    return result

# --- Choice 2: Python's standard 'logging' module ---
# A more robust "free choice" (built-in). Offers levels, handlers, formatters.
# Better for production applications, larger projects, and structured logging.

# Configure the logger once
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # Set overall logging level to capture all messages

# Create a console handler and set its level
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO) # Only INFO and above will show on console by default

# Create a formatter for structured output
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# (Optional) You could also add a file handler for persistent logs
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.DEBUG) # Log all debug messages to file
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

def perform_task_with_logging(data):
    logger.debug(f"Starting task with data: {data}") # Detailed debug info, only visible if console_handler level is DEBUG
    result = data * 3
    logger.info(f"Processed data {data}, result: {result}") # General info
    if result > 15:
        logger.warning(f"Result {result} is unusually high!") # Important warning
    try:
        if data == 0:
            raise ValueError("Data cannot be zero for this operation.")
    except ValueError as e:
        logger.error(f"Error processing data {data}: {e}", exc_info=True) # Error with traceback
    return result

# --- Main execution ---
if __name__ == "__main__":
    print("--- Demonstrating 'print()' for logging (Simple, but limited) ---")
    # This choice is quick for small scripts, but lacks structure, levels, and easy configuration.
    perform_task_with_print(5)
    perform_task_with_print(8)
    print("\n")

    print("--- Demonstrating Python's 'logging' module (Robust, configurable) ---")
    # This choice offers more control, better for larger projects, and allows easy redirection of logs.
    # It's still "free" as it's part of the standard library.
    perform_task_with_logging(4)
    perform_task_with_logging(6)
    perform_task_with_logging(0) # To trigger an error log
    print("\n")

    print("--- Summary of Choices ---")
    print("For quick scripts or debugging, 'print()' is a simple 'free choice'.")
    print("For robust applications, Python's built-in 'logging' module is a smarter 'free choice'.")
    print("It provides structured output, log levels, and flexible handlers (console, file, network, etc.).")
    print("Choosing the right tool (even if both are 'free') depends on your project's needs and scale.")

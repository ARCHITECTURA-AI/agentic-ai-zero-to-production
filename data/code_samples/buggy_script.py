"""
Buggy script designed to crash with a ZeroDivisionError.
Allows checking how sandboxes or agent loops contain run-time exceptions.
"""

def execute_flawed_logic():
    print("Beginning process...")
    # Standard divide by zero error
    divisor = 0
    result = 100 / divisor
    print(f"Result: {result}")

if __name__ == "__main__":
    execute_flawed_logic()

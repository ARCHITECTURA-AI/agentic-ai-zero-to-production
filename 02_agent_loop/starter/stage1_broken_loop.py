"""
Stage 1 Starter: Broken Agent Loop.
This demonstrates an infinite loop with zero active step boundary management.
"""

def execute_broken_react_loop(objective: str) -> None:
    print(f"Goal: {objective}")
    steps_taken = 0
    
    # DANGEROUS: Pure while-True loop with no escape boundary checks!
    while True:
        steps_taken += 1
        print(f"Executing step {steps_taken}... running tools...")
        # Imagine an LLM outputting the exact same query over and over again!
        # If the tool has a subtle bug or the parsing fails, we are trapped!
        
        # Simulating failure to solve goal:
        if steps_taken > 100:
            print("System crashed or ran out of execution memory!")
            break

"""
Broken Agent Loop sample showing infinite recursion issues.
This demonstrates what happens when there is no budget or step limiter.
"""
import time

def broken_agent_loop(objective: str):
    print(f"Goal: {objective}")
    state = "executing"
    step = 0
    
    # DANGEROUS: No max_steps checks!
    while state != "done":
        step += 1
        print(f"Step {step}: Agent is searching for action...")
        time.sleep(0.1) # Simulate tool execution
        
        # Simulate static reasoning drift where agent gets stuck in loop
        if step > 5:
            print("  [Loop detected] Proposing same tool execution again and again...")
            # We never set state = "done", generating an infinite execution cycle!

if __name__ == "__main__":
    broken_agent_loop("Refund Alice's double renewal charge.")

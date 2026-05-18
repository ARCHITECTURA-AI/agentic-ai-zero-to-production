"""
Vulnerable Tool sample.
Executes raw shell instructions or evaluates untrusted user inputs directly.
"""
import subprocess

def run_untrusted_calculation(expression: str) -> str:
    """Vulnerable function that evaluates expressions.
    
    If the prompt injects system calls, this can compromise the machine!
    """
    print(f"Executing: eval('{expression}')")
    try:
        # DANGEROUS: Using eval directly on untrusted inputs!
        # E.g., expression = "__import__('os').system('echo VULNERABLE')"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def execute_untrusted_system_command(user_command: str) -> str:
    """DANGEROUS: Executes raw subprocess commands."""
    try:
        # Vulnerable shell integration
        output = subprocess.check_output(user_command, shell=True, text=True)
        return output
    except Exception as e:
        return str(e)

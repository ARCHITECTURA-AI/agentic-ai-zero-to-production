"""
Solution file for Exercise 9.1.
Timeout-secured, AST-audited Python script execution sandbox.
Blocks dangerous operations and mitigates execution loops.
"""
import ast
import threading
from typing import Dict, Any

class SecurityViolation(Exception):
    pass

class ASTSecurityAuditor(ast.NodeVisitor):
    """Audits the script's AST to block illegal calls and imports before execution."""
    FORBIDDEN_CALLS = {"eval", "exec", "open", "compile", "globals", "locals", "__import__"}

    def visit_Import(self, node: ast.Import):
        raise SecurityViolation("Imports are blocked in the basic execution sandbox.")

    def visit_ImportFrom(self, node: ast.ImportFrom):
        raise SecurityViolation("Import From statements are blocked in the sandbox.")

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            if node.func.id in self.FORBIDDEN_CALLS:
                raise SecurityViolation(f"Calling dangerous builtin function '{node.func.id}' is blocked.")
        self.generic_visit(node)

def run_code_sandbox(code_str: str, timeout_sec: float = 0.5) -> Dict[str, Any]:
    """Audits Python code and runs it within restricted globals and thread timeout guards."""
    # 1. AST Auditing Phase
    try:
        tree = ast.parse(code_str)
        auditor = ASTSecurityAuditor()
        auditor.visit(tree)
    except SecurityViolation as sv:
        return {"status": "BLOCKED", "output": f"Security Violation: {str(sv)}"}
    except Exception as e:
        return {"status": "BLOCKED", "output": f"Compilation Error: {str(e)}"}

    # 2. Setup Sandboxed Globals
    # Only allow standard benign functions
    restricted_builtins = {
        "print": print,
        "range": range,
        "len": len,
        "abs": abs,
        "str": str,
        "int": int,
        "float": float,
        "dict": dict,
        "list": list
    }
    
    sandbox_globals = {
        "__builtins__": restricted_builtins,
        "result": None
    }

    # 3. Timed Thread Execution
    execution_error = None
    execution_result = None

    def worker():
        nonlocal execution_error, execution_result
        try:
            # Execute python code string inside restricted globals namespace
            exec(code_str, sandbox_globals)
            execution_result = sandbox_globals.get("result")
        except Exception as err:
            execution_error = err

    thread = threading.Thread(target=worker)
    thread.start()
    thread.join(timeout=timeout_sec)

    if thread.is_alive():
        # Execution exceeded the safety timeout
        return {"status": "TIMEOUT", "output": "Execution timed out."}

    if execution_error:
        return {"status": "BLOCKED", "output": f"Runtime Exception: {str(execution_error)}"}

    return {"status": "SUCCESS", "output": str(execution_result)}

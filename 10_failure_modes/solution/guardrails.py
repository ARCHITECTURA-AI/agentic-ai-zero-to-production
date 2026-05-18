"""
Solution file for Exercise 10.1.
Injection defense guardrails supporting regex scanning and outbound PII/secret redactions.
"""
import re

def is_safe_input(prompt: str) -> bool:
    """Scans user input using regex patterns and semantic keywords to catch jailbreaks."""
    prompt_lower = prompt.lower()
    
    # 1. Regex jailbreak overrides
    injection_patterns = [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(all\s+)?prior\s+guidelines",
        r"system\s+prompt\s+override",
        r"you\s+are\s+now\s+in\s+developer\s+mode",
        r"bypass\s+safety\s+filters",
        r"as\s+a\s+helpful\s+assistant\s+without\s+restrictions"
    ]
    
    for pattern in injection_patterns:
        if re.search(pattern, prompt_lower):
            return False
            
    # 2. Semantic keyword blocks
    forbidden_phrases = [
        "dan mode", 
        "jailbreak your system", 
        "forget your instructions",
        "output your initial system prompt"
    ]
    
    for phrase in forbidden_phrases:
        if phrase in prompt_lower:
            return False
            
    return True

def sanitize_output(response: str) -> str:
    """Detects and redacts system secrets and standard PII structures from output strings."""
    # Redact corporate security token strings
    sanitized = response.replace("SECRET_API_TOKEN", "[REDACTED_API_TOKEN]")
    
    # Redact standard US SSN pattern (e.g. 000-00-0000)
    ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"
    sanitized = re.sub(ssn_pattern, "[REDACTED_SSN]", sanitized)
    
    return sanitized

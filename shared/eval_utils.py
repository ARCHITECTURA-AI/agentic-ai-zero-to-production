import re
from typing import List, Set

def evaluate_exact_match(prediction: str, target: str, ignore_case: bool = True) -> bool:
    """Check if the predicted string exactly matches the target string."""
    if ignore_case:
        return prediction.strip().lower() == target.strip().lower()
    return prediction.strip() == target.strip()

def evaluate_regex_match(text: str, pattern: str) -> bool:
    """Verify that a target regular expression compiles and matches the given text."""
    try:
        match = re.search(pattern, text, re.IGNORECASE)
        return bool(match)
    except re.error:
        return False

def evaluate_keyword_overlap(text: str, keywords: List[str]) -> float:
    """Compute ratio of target keywords found in the generated output text."""
    if not keywords:
        return 1.0
        
    cleaned_text = text.lower()
    found_keywords = sum(1 for kw in keywords if kw.lower() in cleaned_text)
    
    return float(found_keywords) / len(keywords)

def evaluate_contains_all(text: str, required_clauses: List[str]) -> bool:
    """Check that all required phrases appear inside the output string."""
    cleaned = text.lower()
    return all(clause.lower() in cleaned for clause in required_clauses)

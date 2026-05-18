"""
Solution file for Exercise 5.1.
Implements robust exact-matching, regular expression scanning, and keyword overlap metrics.
"""
from typing import List
import re

def grade_routing_decision(prediction: str, target: str) -> bool:
    """Verifies that the predicted category matches the gold target exactly, ignoring case/trim."""
    return prediction.strip().lower() == target.strip().lower()

def verify_ticket_id_present(text: str) -> bool:
    """Uses a regular expression to assert that a support ticket ID (TKT-#####) exists in the output."""
    pattern = r"TKT-\d{5}"
    match = re.search(pattern, text)
    return bool(match)

def calculate_keyword_score(text: str, required_keywords: List[str]) -> float:
    """Computes the ratio of domain keywords present in the text."""
    if not required_keywords:
        return 1.0
        
    text_lower = text.lower()
    matches = sum(1 for kw in required_keywords if kw.lower() in text_lower)
    return float(matches) / len(required_keywords)

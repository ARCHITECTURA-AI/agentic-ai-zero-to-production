"""
Starter file for Exercise 5.1.
Write deterministic grading logic using regex patterns and keyword overlaps.
"""
from typing import List
import re

def verify_ticket_id_present(text: str) -> bool:
    """Asserts that a standard ticket ID (format: TKT-#####) is present inside the response."""
    # TODO: Compile a regex pattern to find ticket IDs and return match status.
    return False

def calculate_keyword_score(text: str, required_keywords: List[str]) -> float:
    """Calculates the ratio of required keywords present in the text."""
    # TODO: Scan the text (lowercased) and return the ratio of matching words.
    return 0.0

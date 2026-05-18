"""
Solution file for Exercise 8.2.
Robust offline semantic metric calculators for testing grounding (faithfulness) and answer relevancy.
"""
import re
from typing import Dict, Any

def calculate_faithfulness(response: str, context: str) -> Dict[str, Any]:
    """Calculates groundness metric scoring whether claims are supported by source context.
    
    Uses filtered semantic stopword intersect sets.
    """
    words_resp = set(re.findall(r"\b\w{3,}\b", response.lower()))
    words_ctx = set(re.findall(r"\b\w{3,}\b", context.lower()))
    
    # Custom stop words list
    stops = {
        "the", "and", "but", "for", "with", "this", "that", "these", "those",
        "you", "your", "they", "them", "not", "have", "been", "was", "were",
        "has", "had", "are", "will", "would", "should", "could"
    }
    
    key_resp = words_resp - stops
    key_ctx = words_ctx - stops
    
    if not key_resp:
        return {"score": 1.0, "reason": "Response has no valid content words."}
        
    overlap = key_resp.intersection(key_ctx)
    score = len(overlap) / len(key_resp)
    
    return {
        "score": round(score, 2),
        "reason": f"Grounded claims match: {len(overlap)} of {len(key_resp)} unique keywords."
    }

def calculate_relevance(response: str, query: str) -> Dict[str, Any]:
    """Calculates question alignment metric checking if response maps key topics of the query."""
    words_resp = set(re.findall(r"\b\w{3,}\b", response.lower()))
    words_query = set(re.findall(r"\b\w{3,}\b", query.lower()))
    
    stops = {
        "the", "and", "but", "for", "with", "what", "where", "when", "how",
        "why", "who", "your", "please", "help"
    }
    
    key_resp = words_resp - stops
    key_query = words_query - stops
    
    if not key_query:
        return {"score": 1.0, "reason": "Query contains no target subject words."}
        
    overlap = key_resp.intersection(key_query)
    score = len(overlap) / len(key_query)
    
    # Scale score to model query-to-answer similarity
    final_score = min(score * 1.5, 1.0)
    
    return {
        "score": round(final_score, 2),
        "reason": f"Topic coverage matches: {len(overlap)} of {len(key_query)} terms."
    }

from typing import Dict, Tuple

# Token Pricing Table (Prices in USD per 1M tokens)
# Format: (input_price_1m, output_price_1m)
MODEL_PRICING: Dict[str, Tuple[float, float]] = {
    "gpt-4o-mini": (0.150, 0.600),
    "gpt-4o": (2.500, 10.000),
    "gpt-3.5-turbo": (0.500, 1.500),
    "claude-3-haiku-20240307": (0.250, 1.250),
    "claude-3-5-sonnet-20240620": (3.000, 15.000),
}

def calculate_step_cost(
    prompt_tokens: int,
    completion_tokens: int,
    model_name: str = "gpt-4o-mini"
) -> float:
    """Compute the actual cost of a single completion step in US Dollars.
    
    If the model is not found, defaults to 'gpt-4o-mini' pricing standards.
    """
    model_key = model_name.lower()
    
    # Try fuzzy matching
    pricing = MODEL_PRICING.get("gpt-4o-mini")
    for name, rates in MODEL_PRICING.items():
        if name in model_key:
            pricing = rates
            break
            
    input_rate, output_rate = pricing
    
    input_cost = (prompt_tokens / 1_000_000.0) * input_rate
    output_cost = (completion_tokens / 1_000_000.0) * output_rate
    
    return input_cost + output_cost

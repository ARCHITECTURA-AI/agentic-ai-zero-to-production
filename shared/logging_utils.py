import sys
import json
import logging
from datetime import datetime
from typing import Any, Dict

class StructuredFormatter(logging.Formatter):
    """Custom formatter to render log metadata structures as JSON strings."""
    def format(self, record: logging.LogRecord) -> str:
        log_payload: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }
        # Add custom metrics or contextual fields if passed in 'extra'
        if hasattr(record, "step"):
            log_payload["step"] = getattr(record, "step")
        if hasattr(record, "cost_usd"):
            log_payload["cost_usd"] = getattr(record, "cost_usd")
        if hasattr(record, "tokens_used"):
            log_payload["tokens_used"] = getattr(record, "tokens_used")
        if hasattr(record, "tool_name"):
            log_payload["tool_name"] = getattr(record, "tool_name")
            
        return json.dumps(log_payload)

def get_logger(name: str) -> logging.Logger:
    """Instantiate a structured JSON logger for student exercises."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Avoid duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter())
        logger.addHandler(handler)
        logger.propagate = False
        
    return logger

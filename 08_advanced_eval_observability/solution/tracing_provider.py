"""
Solution file for Exercise 8.1 & 8.3.
Production-grade hierarchical OpenTelemetry-like tracing provider with duration tracking and session pricing calculations.
"""
from typing import Dict, Any, List, Optional
import time
import uuid

class Span:
    """Represents a single trace node executing work."""
    def __init__(self, name: str, parent_id: Optional[str] = None):
        self.span_id = str(uuid.uuid4())[:8]
        self.name = name
        self.parent_id = parent_id
        self.start_time = time.time()
        self.end_time = 0.0
        self.duration_ms = 0.0
        self.tags = {}
        self.status = "UNFINISHED"

class Tracer:
    """Thread-safe multi-span registry coordinating parent-child tracking loops."""
    def __init__(self):
        self.spans: Dict[str, Span] = {}

    def start_span(self, name: str, parent_id: Optional[str] = None) -> Span:
        """Instantiates a timing span and maps it inside the active registry."""
        span = Span(name, parent_id)
        self.spans[span.span_id] = span
        return span

    def end_span(self, span_id: str, status: str = "OK", tags: Dict[str, Any] = None) -> None:
        """Finishes execution, calculates durations, and binds custom telemetry tags."""
        if span_id in self.spans:
            span = self.spans[span_id]
            span.end_time = time.time()
            span.duration_ms = (span.end_time - span.start_time) * 1000.0
            span.status = status
            if tags:
                span.tags.update(tags)

    def get_child_spans(self, parent_id: str) -> List[Span]:
        """Traverses and yields all sub-spans linked to a parent."""
        return [s for s in self.spans.values() if s.parent_id == parent_id]

    def aggregate_session_cost(self) -> float:
        """Traverses spans and computes standard aggregated dollar cost.
        
        Pricing Model:
        - Input Tokens: $1.50 per Million Tokens ($0.0000015 per token)
        - Output Tokens: $2.00 per Million Tokens ($0.0000020 per token)
        """
        total_cost = 0.0
        for span in self.spans.values():
            input_tokens = span.tags.get("input_tokens", 0)
            output_tokens = span.tags.get("output_tokens", 0)
            total_cost += (input_tokens * 0.0000015) + (output_tokens * 0.0000020)
        return total_cost

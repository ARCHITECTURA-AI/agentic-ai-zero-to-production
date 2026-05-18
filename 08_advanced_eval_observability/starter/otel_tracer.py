"""
Starter file for Exercise 8.1.
Implements standard nesting trace frameworks with span structures.
"""
from typing import Dict, Any, List, Optional
import time
import uuid

class Span:
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
    def __init__(self):
        self.spans: Dict[str, Span] = {}

    def start_span(self, name: str, parent_id: Optional[str] = None) -> Span:
        """Starts tracking a unit of work."""
        # TODO: Instantiate a span, record inside self.spans, and return it.
        return Span(name, parent_id)

    def end_span(self, span_id: str, status: str = "OK", tags: Dict[str, Any] = None) -> None:
        """Calculates execution duration and records tags."""
        # TODO: Stop timing, compute duration_ms, update status and tags.
        pass

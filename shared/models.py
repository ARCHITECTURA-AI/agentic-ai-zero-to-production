from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

# ── ROUTING DECISION MODELS ──────────────────────────────────────────────────
class RouterDecision(BaseModel):
    """Represents a validated ticket or action routing decision."""
    category: str = Field(..., description="Target queue, e.g. 'refund', 'tech_support', 'billing', 'general'")
    reason: str = Field(..., description="Detailed technical justification for this routing outcome")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Routing confidence value between 0.0 and 1.0")
    escalation_required: bool = Field(False, description="Flag indicating high-risk escalation needed")

# ── TOOL CALL MECHANICS MODELS ───────────────────────────────────────────────
class ToolCallAction(BaseModel):
    """Structured representation of a proposed agent tool action."""
    tool_name: str = Field(..., description="Name of the selected tool to execute")
    arguments: Dict[str, Any] = Field(default_factory=dict, description="Typed arguments matching tool's Pydantic schema")
    thought: str = Field(..., description="Self-reflection or reasoning explaining this tool invocation choice")

# ── PERFORMANCE EVALUATION MODELS ─────────────────────────────────────────────
class EvaluationMetrics(BaseModel):
    """Unified structure returned by evaluation engines."""
    score: float = Field(..., ge=0.0, le=1.0, description="Primary validation score between 0.0 and 1.0")
    success: bool = Field(..., description="Boolean flag representing pass/fail state")
    feedback: str = Field(..., description="Actionable critique detailing reasons for this score")
    latency_seconds: Optional[float] = Field(None, description="Time taken to compute the results")

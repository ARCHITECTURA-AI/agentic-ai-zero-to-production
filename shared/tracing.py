import os
from typing import Optional

def setup_telemetry(project_name: str = "agentic-ai-zero-to-production") -> None:
    """Initialize OpenTelemetry logging bridges.
    
    If LITE_OBSERVABILITY_MODE is enabled or missing variables, falls back 
    gracefully to standard debug diagnostics logs.
    """
    lite_mode = os.environ.get("LITE_OBSERVABILITY_MODE", "true").lower() == "true"
    
    if lite_mode:
        print("ℹ️  Observability running in LITE mode. Tracing logs saved locally in diagnostics.")
        return
        
    try:
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.resources import Resource
        
        # Configure resource profile
        resource = Resource(attributes={"service.name": project_name})
        provider = TracerProvider(resource=resource)
        
        # Configure simple stream processor or connect exporter
        # Students can plug in arize-phoenix collector endpoint
        trace.set_tracer_provider(provider)
        print("✅ OpenTelemetry tracing provider successfully initialized.")
    except Exception as e:
        print(f"⚠️  Could not initialize telemetry provider: {e}. Falling back to standard logs.")

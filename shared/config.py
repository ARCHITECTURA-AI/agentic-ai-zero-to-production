import os
from pathlib import Path
from dotenv import load_dotenv

# Load env variables from root directory
root_dir = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=root_dir / ".env")

# ── API KEY SETTINGS ─────────────────────────────────────────────────────────
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# ── MODEL NAME ASSIGNMENTS ───────────────────────────────────────────────────
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL_NAME", "gpt-4o-mini")
HEAVY_MODEL = os.environ.get("HEAVY_MODEL_NAME", "gpt-4o")

# ── SYSTEM SAFETY SETTINGS ───────────────────────────────────────────────────
MAX_EXECUTION_STEPS = int(os.environ.get("GUARDRAILS_MAX_STEPS", 10))
MAX_EXECUTION_COST_USD = float(os.environ.get("GUARDRAILS_MAX_COST_USD", 2.00))

# ── PATH ASSIGNMENTS ──────────────────────────────────────────────────────────
DATA_DIR = root_dir / "data"
TICKETS_PATH = DATA_DIR / "tickets"
KNOWLEDGE_BASE_PATH = DATA_DIR / "knowledge_base"
CODE_SAMPLES_PATH = DATA_DIR / "code_samples"
EVAL_SETS_PATH = DATA_DIR / "eval_sets"

# Make directories if they do not exist
DATA_DIR.mkdir(exist_ok=True)
TICKETS_PATH.mkdir(exist_ok=True)
KNOWLEDGE_BASE_PATH.mkdir(exist_ok=True)
CODE_SAMPLES_PATH.mkdir(exist_ok=True)
EVAL_SETS_PATH.mkdir(exist_ok=True)

# ── MOCK CONTROLS (For offline tests) ───────────────────────────────────────
MOCK_LLM_MODE = os.environ.get("MOCK_LLM_MODE", "false").lower() == "true"

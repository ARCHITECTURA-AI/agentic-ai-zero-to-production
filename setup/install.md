# Installation Guide

## Requirements

- Python 3.10 or higher
- pip
- git
- A terminal (Terminal on Mac/Linux, PowerShell on Windows)

## Step 1: Check your Python version

```bash
python --version
```

You need 3.10 or higher.
If you have an older version, download from python.org.

## Step 2: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-0-to-100
cd agentic-ai-0-to-100
```

## Step 3: Create a virtual environment

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

## Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

This will take 2-5 minutes.

## Step 5: Set up your environment variables

```bash
cp setup/sample.env .env
```

Open `.env` in any text editor and fill in your API keys.
See the API Keys section below for where to get them.

## Step 6: Verify your setup

```bash
python setup/verify_environment.py
```

You should see all green checkmarks.

## Step 7: Test API access

```bash
python setup/test_api_keys.py
```

You should see successful connection messages.

## API Keys

### OpenAI

1. Go to platform.openai.com
2. Click API Keys in the left sidebar
3. Click Create new secret key
4. Copy it into `.env` as `OPENAI_API_KEY`

### Anthropic (optional)

1. Go to console.anthropic.com
2. Click API Keys
3. Create a new key
4. Copy it into `.env` as `ANTHROPIC_API_KEY`

### LangSmith (optional but recommended)

1. Go to smith.langchain.com
2. Create a free account
3. Go to Settings → API Keys
4. Create a new key
5. Copy it into `.env` as `LANGSMITH_API_KEY`

## Corporate Network Note

If you are behind a corporate proxy, you may need to set:

```bash
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
```

Or on Windows:

```bash
set HTTP_PROXY=http://your-proxy:port
set HTTPS_PROXY=http://your-proxy:port
```

Test that you can reach the OpenAI API from inside your network before the training starts.
Run `setup/test_api_keys.py` to confirm.

## Common Issues

### "Module not found" error

Make sure your virtual environment is activated.
You should see `(.venv)` in your terminal.

### "Permission denied" on Windows

Run PowerShell as Administrator.
Or run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

### Slow installation

Use a faster mirror:
`pip install -r requirements.txt -i https://pypi.org/simple`

### API key not working

Make sure there are no spaces around the `=` sign in `.env`
Make sure you copied the full key including any prefix like `sk-`

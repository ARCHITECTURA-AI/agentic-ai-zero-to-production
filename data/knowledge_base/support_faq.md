# Support FAQ: Common Enquiries

### Q: What should I do if I get an API connection error?
First, ensure that your `.env` contains a valid key. If you are on a corporate laptop, try running the environment check: `python setup/verify_environment.py` and configuring the `HTTP_PROXY` shell values.

### Q: Can an agent refund my invoice directly?
Yes! Our support agent is capable of processing refunds under $100.00 USD autonomously. Transactions above that limit trigger billing operator validation gates.

### Q: How do I enable tracing telemetry?
Set the `LITE_OBSERVABILITY_MODE=false` flag in your environment configuration and start up a local Phoenix instance.

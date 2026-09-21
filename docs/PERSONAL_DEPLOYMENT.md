# 个人版部署

Recommended architecture:
Client -> API Gateway -> Auth/Quota -> Redis Queue -> GPU Workers -> S3/MinIO

Production concerns:
API keys, quotas, concurrency limits, cancellation, retries, model versioning, logging/audit,
GPU isolation, content safety and monitoring. Docker/Kubernetes can be added as scale increases.

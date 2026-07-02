# DevOps Portfolio App

A lightweight Flask application packaged with Docker and deployed via Helm — demonstrates the full container lifecycle from build to Kubernetes deployment.

## What this demonstrates

- **Multi-stage Docker build** — build dependencies in one stage, copy to slim runtime image
- **Non-root container** — runs as `appuser`, not root
- **Helm chart** — parameterized Kubernetes deployment with values overrides per environment
- **Health endpoints** — `/health` and `/ready` for Kubernetes probes

## App endpoints

| Endpoint | Response |
|----------|----------|
| `GET /` | JSON with app name, version, environment, timestamp |
| `GET /health` | `{"status": "healthy"}` |
| `GET /ready` | `{"status": "ready"}` |

## Docker

```bash
# Build
docker build -t devops-portfolio:0.1.0 .

# Run
docker run -p 5000:5000 devops-portfolio:0.1.0

# Test
curl http://localhost:5000/
curl http://localhost:5000/health
```

## Helm deployment

```bash
# Install to dev
helm install portfolio ./helm -f helm/values-dev.yaml

# Install to prod
helm install portfolio ./helm -f helm/values-prod.yaml

# Upgrade
helm upgrade portfolio ./helm --set image.tag=0.2.0
```

## Helm values

| Parameter | Default | Description |
|-----------|---------|-------------|
| `replicaCount` | 1 | Number of pods |
| `image.repository` | devops-portfolio | Container image |
| `image.tag` | 0.1.0 | Image tag |
| `service.type` | ClusterIP | Service type |
| `resources.limits.cpu` | 250m | CPU limit |
| `resources.limits.memory` | 128Mi | Memory limit |
| `ingress.enabled` | false | Enable ingress |
| `probes.enabled` | false | Enable liveness/readiness probes |

## Tags

`flask` `docker` `helm` `kubernetes` `multi-stage-build` `portfolio`

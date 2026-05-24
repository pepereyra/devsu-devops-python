# Demo DevOps Python

![CI-CD](https://github.com/pepereyra/devsu-demo-devops-python/actions/workflows/ci-cd.yml/badge.svg)

Production-ready DevOps technical assessment project based on Django, Docker, Kubernetes, GitHub Actions, Terraform and Google Cloud Platform.

---

# Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions CI/CD
   |
   +--> Ruff Static Analysis
   +--> Unit Tests
   +--> Coverage Report
   +--> Trivy Security Scan
   +--> Docker Build
   |
   v
GHCR Container Registry
   |
   v
GitOps Repository
   |
   v
Kustomize Overlays
   |
   v
GKE Cluster
   |
   +--> Deployment
   +--> HPA
   +--> Service
   +--> Ingress
   +--> Migration Job
   |
   v
Cloud SQL MySQL
```

---

# Technologies

- Python 3.11
- Django
- Docker
- Kubernetes (GKE Autopilot)
- Terraform
- GitHub Actions
- GitOps with Kustomize
- Cloud SQL MySQL
- Trivy
- Ruff
- Gunicorn

---

# Features

- Dockerized application
- CI/CD pipeline
- GitOps workflow
- Horizontal Pod Autoscaler
- Kubernetes Ingress
- Dedicated migration Job
- Static code analysis
- Vulnerability scanning
- Test coverage reporting
- Infrastructure as Code
- Security hardening

---

# Local Development

## Requirements

- Python 3.11
- pip

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run migrations

```bash
python manage.py migrate
```

## Run tests

```bash
python manage.py test
```

## Run locally

```bash
python manage.py runserver
```

Application available at:

```text
http://localhost:8000/api/
```

---

# Docker

## Build image

```bash
docker build -t devsu-devops-python .
```

## Run container

```bash
docker run -p 8000:8000 devsu-devops-python
```

---

# CI/CD Pipeline

Implemented using GitHub Actions.

Pipeline stages:

- Dependency installation
- Static code analysis with Ruff
- Unit tests
- Coverage report generation
- Docker build
- Container validation
- Healthcheck validation
- Trivy vulnerability scan
- Push image to GHCR
- GitOps repository update

---

# Kubernetes Deployment

The application is deployed on Google Kubernetes Engine (GKE) using:

- Deployment
- Service
- Ingress
- ConfigMaps
- Secrets
- HPA
- Migration Job
- Kustomize overlays

Environments:

- dev
- prod

---

# Terraform Infrastructure

Terraform provisions:

- VPC
- Subnet
- GKE Autopilot Cluster
- Cloud SQL MySQL

---

# Security Practices

- Non-root containers
- Read-only root filesystem
- Linux capabilities dropped
- Kubernetes Secrets
- Trivy vulnerability scanning
- Static code analysis
- Dedicated migration jobs

---

# Public Endpoint

Example endpoint:

```text
http://8.34.213.158/api/users/
```

---

# API Endpoints

## Create User

```http
POST /api/users/
```

Request:

```json
{
  "dni": "12345678",
  "name": "Pedro"
}
```

---

## Get Users

```http
GET /api/users/
```

---

## Healthcheck

```http
GET /api/health/live/
```

```http
GET /api/health/ready/
```

---

# Notes

Cloud SQL currently allows public access for technical assessment simplicity.

In production environments this should be replaced with:

- Private networking
- Authorized CIDRs
- Cloud SQL Auth Proxy
- TLS enforcement

---

# Repositories

Application repository:

```text
https://github.com/pepereyra/devsu-demo-devops-python
```

GitOps repository:

```text
https://github.com/pepereyra/devsu-devops-python-gitops
```

---

# License

Technical assessment project for DevOps evaluation purposes.
# CloudOps Platform

## Overview
CloudOps Platform is a hands-on DevOps project focused on building, deploying, and operating a cloud-native application on Microsoft Azure.

It provides an end-to-end implementation of modern DevOps practices, covering containerization, infrastructure automation, Kubernetes orchestration, CI/CD pipelines, and application monitoring.

The platform is built around a containerized REST API and leverages Docker, Ansible, Kubernetes, and GitHub Actions to deliver a reproducible and automated deployment environment.

## Project Objectives
The main objective of this project is to strengthen my skills in core DevOps tools and practices through hands-on experience.

Rather than studying each technology independently, I aim to combine them in a realistic, end-to-end use case, gaining practical experience in how they interact to build, deploy, automate, and monitor a cloud-native application.

## Architecture
*To be documented as the project progresses.*

## Technology Stack

Domain |                      Technology

Cloud |                       Azure \
Operating System |            Ubuntu Server LTS \
Configuration Management |    Ansible \
Container Runtime |           containerd \
Orchestration |               Kubernetes \
Kubernetes Installation |     kubeadm \
CLI |                         kubectl \
CNI |                         Calico \
API |                         Python / FastAPI \
Database |                    PostgreSQL \
Containerization |            Docker \
CI/CD |                       GitHub Actions \
Container Registry |          GitHub Container Registry \
Testing |                     Pytest \
Monitoring |                  Prometheus / Grafana \
Version Control |             Git / GitHub

## Repository Structure
cloudops-platform/ \
├── application/ \
├── docker/ \
├── ansible/ \
├── kubernetes/ \
├── .github/ \
│   └── workflows/ \
└── docs/

## Getting Started
*To be documented as the project progresses.*

## Project Roadmap
The project is planned over four main phases:

Phase 1 — Application & Containerization

    Develop the FastAPI application and integrate PostgreSQL.

    Implement automated tests with Pytest.

    Containerize the application with Docker and configure Docker Compose.

    Deliverable: A fully functional application running locally.

Phase 2 — Cloud Infrastructure & Automation

    Provision Linux virtual machines on Microsoft Azure.

    Automate system configuration and security with Ansible.

    Install and configure containerd and Kubernetes using kubeadm.

    Deploy the Kubernetes control plane and worker node.

    Deliverable: A functional and reproducible Kubernetes cluster.

Phase 3 — Kubernetes Deployment

    Deploy the application and database to Kubernetes.

    Configure networking, storage, ConfigMaps, and Secrets.

    Set up Ingress and HTTPS.

    Implement health checks, resource management, and rolling updates.

    Deliverable: The application running and accessible on Kubernetes.

Phase 4 — CI/CD & Monitoring

    Build CI/CD pipelines with GitHub Actions.

    Build and publish container images to GHCR.

    Automate application deployments.

    Set up Prometheus and Grafana.

    Test self-healing, failure recovery, and rollback mechanisms.

    Finalize documentation and prepare a project demonstration.

    Deliverable: An automated, monitored, and documented DevOps platform.

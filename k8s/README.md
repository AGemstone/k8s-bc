# Demo K8s/AWS

A simple demo designed to showcase how we can deploy an app using the free tier 
of AWS.

## Objectives:
* Single file per technology. Small project
* Connect Kubernetes with AWS

## Architecture

### Software
**Frontend**: Nginx + P5JS
**Backend**: FastAPI
**Database**: PostgreSQL

### Hardware

Single master node and single worker node. 1 CPU with 1GiB RAM (AWS t2-micro)
Master node only handles critical system pods/deployments and worker node handles the deployed app.



Project Overview -

This project demonstrates the deployment of a microservices-based application on Microsoft Azure, using Terraform for Infrastructure as Code (IaC) and Azure Kubernetes Service (AKS) for container orchestration.
The setup includes automated provisioning, CI/CD pipelines, secure secret management, and monitoring — following DevOps best practices.# microservices-project
This repo is dedicated of microservice project

Architecture Overview -
Components:

Azure Resource Group – Root container for all resources

Azure Virtual Network (VNet) – Provides secure network isolation

Azure Container Registry (ACR) – Stores Docker images

Azure Kubernetes Service (AKS) – Hosts and manages microservices containers

Azure Key Vault – Manages secrets, certificates, and keys securely

Azure Storage Account – Stores Terraform state and other persistent data

Azure Monitor + Application Insights – Provides monitoring and logging

Microservices Example:

user-service → Handles user registration and management

order-service → Handles order creation and tracking

api-gateway → Exposes unified API to frontend

terraform/
├── main.tf
├── variables.tf
├── terraform.tfvars
├── provider.tf
└── modules/
    ├── network/
    │   └── main.tf
    ├── acr/
    │   └── main.tf
    ├── aks/
    │   └── main.tf
    ├── keyvault/
    │   └── main.tf
    └── storage/
        └── main.tf


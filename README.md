# MLOps on AWS Repository

## Overview

This repository is a guide to setting up MLOps (Machine Learning Operations) on AWS, focusing on streamlining the deployment and management of machine learning models. The repository includes examples and templates to help you integrate MLOps practices into your machine learning workflows.

## Examples

### Table of Contents

| Example | Description |
| ------- | ----------- |
| [SageMaker](#sagemaker) | Demonstrates the use of AWS SageMaker for end-to-end machine learning workflows. |
| [CI/CD](#ci-cd) | Sets up a simple AWS CI/CD pipeline with EC2, ECR, and GitHub Actions. |

### SageMaker

#### sklearn_script.ipynb

This example notebook (`examples/sagemaker/sklearn_script.ipynb`) demonstrates the end-to-end process of training and deploying a machine learning model using AWS SageMaker. It covers the following steps:

1. **Data Preparation**: Loading and preparing the dataset for training.
2. **Model Training**: Training a machine learning model using scikit-learn.
3. **Model Deployment**: Deploying the trained model as an endpoint on AWS SageMaker.
4. **Inference**: Making predictions using the deployed model.

Feel free to explore and modify the notebook based on your specific use case.

### CI/CD

#### aws_cicd_setup.md

This example (`examples/ci-cd/aws_cicd_setup.md`) provides a simple setup for AWS CI/CD using EC2, ECR, and GitHub Actions. The CI/CD pipeline automates the build and deployment process, ensuring efficient development workflows. Follow the instructions in the document to implement this CI/CD setup for your project.
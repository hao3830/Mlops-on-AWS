
# MLOps on AWS Repository

## Overview

This repository is a guide to setting up MLOps (Machine Learning Operations) on AWS, focusing on streamlining the deployment and management of machine learning models. The repository includes examples and templates to help you integrate MLOps practices into your machine learning workflows.

## Prerequisites

Before getting started, ensure you have the necessary credentials and configurations. Create a `.env` file in the root of your project with the following variables:

```env
AWS_ARN_ROLE=
AWS_DEFAULT_REGION=
BUCKET_NAME=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

Make sure to fill in the values for each variable based on your AWS account and resources.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Examples

1. [SageMaker](#sagemaker)
    - [sklearn_script.ipynb](#sklearn-script)

### SageMaker

#### sklearn_script.ipynb

This example notebook (`examples/sagemaker/sklearn_script.ipynb`) demonstrates the end-to-end process of training and deploying a machine learning model using AWS SageMaker. It covers the following steps:

1. **Data Preparation**: Loading and preparing the dataset for training.
2. **Model Training**: Training a machine learning model using scikit-learn.
3. **Model Deployment**: Deploying the trained model as an endpoint on AWS SageMaker.
4. **Inference**: Making predictions using the deployed model.

Feel free to explore and modify the notebook based on your specific use case.


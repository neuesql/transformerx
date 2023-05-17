# Transformerz
A private hub for huggingface transformers hosting on your AWS/Azure/GCP Cloud.

# Problems
An enterprise company need to develop Generative AI model easily with secure and compliant running environment, not Sass public service. In the meanwhile, public cloud become more expensive and complicated for data scientist to manage it, currently Hugging face stopped the private hub for enterprise [https://huggingface.co/blog/introducing-private-hub](https://huggingface.co/datasets) support since 2023, Q1.
# Requirements
## 1. Not only public Sass Solution
Solution should not only deploy into shared and Sass environment in one geographic region, like Huggingface solution, but also it can deploy into private customerized network and different cloud.
## 2. Multi-Cloud Agnostic Deployment
Enterprise IT environment is complicated with legacy platform and Multi-cloud providers, solution need to deploy into AWS, Azure, GCP, K8S at least in Western European markets.  
## 3. Full backend Compatibility API
The server api need to be compatible with Huggingface Hub API  https://huggingface.co/docs/hub/api
## 4. Simple UI for Models, Datasets, Applications
Once backend have the endpoints, developers need to have a simple ui to view the Artifacts

# Architecture Overview
## 1. Block OverView 

![](docs/privatehub-flow.drawio.svg)

## 2. Deployment OverView
![](docs/privatehub.drawio.svg)

# Features in Details
## Backend API
Please download the full api list table [here](/docs/HuggingfaceAPI.xlsx) !!!
![](docs/Prority.png)

## Frontend UI

To be discuss

1. Models: list all models by tags like [https://huggingface.co/models](https://huggingface.co/models) 
2. Datasets: list all datasets by tags like [https://huggingface.co/datasets](https://huggingface.co/datasets)
3. Spaces: List all the Spaces(Application) template [https://huggingface.co/spaces](https://huggingface.co/spaces)




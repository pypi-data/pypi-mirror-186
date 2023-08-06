# Unified Vision Service Model Customization

## Intro

Unified Vision Service Model Customization is a model training service that allows users like developers to easily train an image classification model (Multiclass only for now) or object detection model, with low-code experience and very little understanding in machine learning or computer vision required.

This is an example repo showing how to train a model and predict with the trained model in Unified Vision Service. A manually crafted Python SDK is provdied. **Note this is NOT an official UVS SDK that is ready for production usage/integration, but more for convenience of trying out UVS model customization service at the absence of official SDK support.**

## SDK Tutorial

For tutorial about how to use this python SDK to train and predict with UVS, checkout [this tutorial in Python notebook](./tutorial.ipynb).

## Vision Studio Tutorial

For tutorial about how to use Vision Studio to train and predict with UVS, checkout [this Vision Studio tutorial](VisionStudioDemo.md).

## Existing Custom Vision Customers

Refer to [export_cvs_data_to_coco.ipynb](export_cvs_data_to_coco.ipynb) for instructions or directly run [export_cvs_data_to_coco.py](export_cvs_data_to_coco.py) to export Custom Vision images and annotations to your own blob storage, which can be later used for UVS model customization training.

Once data is exported, you can use either SDK or Vision Studio to train with it.

## FAQ

For frequently asked questions or quick trouble shoot, checkout [FAQ](FAQ.md).

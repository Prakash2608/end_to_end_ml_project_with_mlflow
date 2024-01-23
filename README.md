# end_to_end_ml_project_with_mlflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update hte components
7. Update the pipeline
8. Updtae the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Prakash2608/end_to_end_ml_project_with_mlflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.10 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/prakashraj822/end_to_end_ml_project_with_mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=prakashraj822 \
MLFLOW_TRACKING_PASSWORD=38cd7a42167fb066e8af4c87753c73d91e336771  \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/prakashraj822/end_to_end_ml_project_with_mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=prakashraj822

export MLFLOW_TRACKING_PASSWORD=38cd7a42167fb066e8af4c87753c73d91e336771

```
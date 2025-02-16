import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/Nikhil1998-Mogre/mini-proejct-model-serving.mlflow')
dagshub.init(repo_owner='Nikhil1998-Mogre', repo_name='mini-proejct-model-serving', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

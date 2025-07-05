FROM tensorflow/serving:latest

COPY model /models/tfmodel
ENV MODEL_NAME=tfmodel

EXPOSE 8501
ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]


#!/bin/bash -eu
# Creates a AI Platform Notebook instance using the environment supplied
# by the metadata.
#
# Usage:
#   basic instance:  ./create_notebook_instance.sh test-instance test.ipynb
#   custom instance: ./create_notebook_instance.sh test-instance test.ipynb \
#                       --accelerator="type=nvidia-tesla-p100,count=1" \
#                       --machine-type="n1-standard-4"
#
# Args:
#   first argument is the name of the GCE instance to create
#   second argument is the path to the notebook to source and upload
#   additional arguments are passed into the instance creation command

INSTANCE_NAME=$1
NOTEBOOK=$2
shift 2

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)"
NOTEBOOK_CONTAINER="$(python ${SCRIPT_DIR}/get_docker_tag.py --path=${NOTEBOOK})"

gcloud compute instances create "${INSTANCE_NAME}" \
  --image-family=common-container \
  --image-project=deeplearning-platform-release \
  --maintenance-policy=TERMINATE \
  --boot-disk-size=200GB \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --metadata="proxy-mode=project_editors,install-nvidia-driver=True,container=${NOTEBOOK_CONTAINER}" \
  "$@"

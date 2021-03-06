SHELL := /bin/bash
VIRTUALENV = LF_IL_virtualenv_learning
AG_VERSION = 2018-10-19

# Makefile to structure work on the AI-DO baselines.

# ---------- DOCKER --------------
# THIS WILL ONLY RUN ON LINUX, NOT on Mac, NOT on Windows since nvidia-docker is not supported
# Nvidia-docker is covered here: https://github.com/NVIDIA/nvidia-docker
# and https://devblogs.nvidia.com/gpu-containers-runtime/
prepare-docker:
				sudo apt-get update; \
				docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f; \
				sudo apt-get purge -y nvidia-docker; \
				curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -; \
				curl -s -L https://nvidia.github.io/nvidia-docker/$$(. /etc/os-release;echo $$ID$$VERSION_ID)/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list; \
				sudo apt-get update; \
				sudo apt-get install -y nvidia-docker2 nvidia-container-runtime; \
				sudo pkill -SIGHUP dockerd; \
				docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi;

# This may run for >10 min and longer (on GPU) if more data is used for learning.
learn-docker:
				docker build -t learn_container .; \
				docker run --runtime=nvidia learn_container;
				docker commit $(shell docker ps -alq) learn_container

# Extract data from docker container and copies it to the learning repository
copy_for_submission:
				mkdir ../submission/learned_models; \
				docker create -it --name dummy_for_copying learn_container:latest bash; \
				docker cp dummy_for_copying:/workspace/learned_models/frozen_graph.pb ../submission/learned_models; \
				docker rm -fv dummy_for_copying;

# ---------- REGULAR --------------
# This assumes that you have GPU drivers installed already.

# If only CPU is available for computation on your machine,
# change the line "pip install tensorflow-gpu" to "tensorflow" (without the GPU option)
install-dependencies:
				virtualenv $(VIRTUALENV); \
				. $(VIRTUALENV)/bin/activate; \
				pip install -e .; \
				pip install tensorflow-gpu;

learn-regular:
				. $(VIRTUALENV)/bin/activate; \
				python src/cnn_training_tensorflow.py --batch-size 32 --learning-rate 1e-5 --epochs 10 --optimizer GDS --save-frequency 1 --print-frequency 1; \
				# python src/freeze_graph.py;

freeze-graph:
				. $(VIRTUALENV)/bin/activate; \
				python src/freeze_graph.py;

regular_copy_for_submission:
				mkdir ../submission/learned_models; \
				cp learned_models/frozen_graph.pb ../submission/learned_models;


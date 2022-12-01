FROM gitpod/workspace-full

USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
RUN sudo apt-get -q update && \
    sudo apt install -yq libopencv-dev python3-opencv && \
    sudo pip install opencv-python
#
# More information: https://www.gitpod.io/docs/42_config_docker/
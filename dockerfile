#docker run -it --rm --gpus device=all -v $(pwd):/tf/notebooks -p 8888:8888 tensorflow/tensorflow:latest-jupyter
FROM tensorflow/tensorflow:latest-jupyter

#no interactive input
ENV DEBIAN_FRONTEND=noninteractive

#install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

RUN python3 -m pip install --upgrade pip
RUN pip install tensorflow_datasets seaborn scikit-learn
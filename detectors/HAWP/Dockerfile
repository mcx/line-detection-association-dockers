# Copyright (c) 2022, Kirill Ivanov, Anastasiia Kornilova and Dmitrii Iarosh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

ARG ALGORITHM_FOLDER=HAWP

WORKDIR /detector

# install dependencies
RUN apt-get update  \
    && apt-get install --no-install-recommends -y \
    libgl1 \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libglu1-mesa-dev \
    mesa-common-dev \
    ninja-build \
    wget \
    && rm -rf /var/lib/apt/lists/*

# install python requirements
COPY $ALGORITHM_FOLDER/requirements.txt requirements.txt

RUN python3 -m pip install --no-cache-dir -r requirements.txt

# download pretrained models
COPY $ALGORITHM_FOLDER/downloads.sh download_models.sh

RUN bash ./download_models.sh

COPY $ALGORITHM_FOLDER .

COPY ./common ./common

ENTRYPOINT ["python3", "run.py"]
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import requests

from graphpipe import remote

data = np.array(Image.open("/Users/caicloud 1/Documents/kubeflow-admin/docs/pytorch_support/mnist-pytorch/images/1.jpg"))
data = data.reshape([1] + list(data.shape))
data = np.rollaxis(data, 1, 1).astype(np.float32)  # channels first
data = np.expand_dims(data, axis=0)
data.astype(np.float32)
print(data.shape)

pred = remote.execute("http://192.168.22.197:30894", data)
print(pred)

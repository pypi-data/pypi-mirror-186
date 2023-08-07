# image2vector

## Introduce

Transforming images into 512-dimensional vectors by residual neural networks

⭐️ 🌟 ✨ ⚡️ ☄️ 💥

## Installation

Package is uploaded on PyPI.

You can install it with pip:

```shell
pip install image2vector
```

## Requirements

Python -- one of the following:

- CPython : 3.8 and newer ✅
- PyPy : Software compatibility not yet tested ❓

## Documentation

📄 Intensified preparation in progress

## Example

With the following code demo, you will learn the following

- Initialize a residual neural network
- Generate a vector of specified images
- Compare the Euclidean distance of two vectors

```python
from pathlib import Path
from typing import List
from iv import ResNet, l2

# Initialize a residual neural network
resnet: ResNet = ResNet(
    weight_file='weight/gl18-tl-resnet50-gem-w-83fdc30.pth'
)


# Generate a vector of specified images
# The generated vector is a List[float] data structure,
# the length of the list is 512, which means the vector is of 512 dimensions
vector_1: List[float] = resnet.gen_vector('example-1.jpg')

vector_2: List[float] = resnet.gen_vector('example-2.jpg')

# Compare the Euclidean distance of two vectors

distance: float = l2(vector_1, vector_2)

print('Euclidean Distance is ', distance)

```

> Where to get the `weight/gl18-tl-resnet50-gem-w-83fdc30.pth` file from, you can visit: http://cmp.felk.cvut.cz/cnnimageretrieval/data/networks/gl18/

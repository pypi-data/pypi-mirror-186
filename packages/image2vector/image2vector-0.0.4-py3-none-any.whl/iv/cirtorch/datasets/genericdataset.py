from PIL import Image
import torch.utils.data as data
import os
from PIL import Image
import torch
from typing import List, Optional
from torchvision.transforms.transforms import Compose


def imresize(image: Image.Image, imsize: int) -> Image.Image:
    image.thumbnail((imsize, imsize), Image.Resampling.LANCZOS)
    return image


def img_loader(img: Image.Image) -> Image.Image:
    return Image.fromarray(img)


class ImagesFromList(data.Dataset):
    def __init__(self, images, imsize: int, transform: Compose, loader=img_loader):
        assert images
        self.image = images
        self.imsize = imsize
        self.transform = transform
        self.loader = loader

    def __getitem__(self, index: int) -> Image.Image:
        path = self.image[index]
        img = self.loader(path)
        img = imresize(img, self.imsize)
        img = self.transform(img)

        return img

    def __len__(self):
        return len(self.image)

    def __repr__(self):
        return f'Dataset {self.__class__.__name__}\n'\
        f'    Number of images: {self.__len__()}\n'\
        f'    Root Location: {self.root}\n'\
        f'    Transforms (if any):  {self.root}\n'

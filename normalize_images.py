#!/usr/bin/env python3
import os

from PIL import Image, ImageOps

IMAGES_DIR = "./linjapona"
WRITE_DIR = "./out"


def nearest_power_of_two(n: int):
    """always >="""
    assert n >= 2

    p2 = 2
    while n > p2:
        p2 *= 2
    return p2


def get_max_dim(images: list):
    maxdim = 0
    for i in images:
        x, y = i._size
        if x > maxdim:
            maxdim = x
        if y > maxdim:
            maxdim = y
    return maxdim


def main():
    image_names = os.listdir(IMAGES_DIR)
    images = [Image.open(os.path.join(IMAGES_DIR, image)) for image in image_names]
    # for i in images:
    #     print(i.__dict__)
    maxdim = get_max_dim(images)
    border_dim = nearest_power_of_two(maxdim)
    os.makedirs(WRITE_DIR, exist_ok=True)
    for i, image in enumerate(images):
        x, y = image._size
        paste_into = Image.new(mode="1", size=(border_dim, border_dim), color="white")
        paste_into.paste(image, ((border_dim - x) // 2, (border_dim - y) // 2))
        paste_into = paste_into.resize((128, 128))
        paste_into.save(os.path.join(WRITE_DIR, image_names[i]))


if __name__ == "__main__":
    main()

from typing import Any
from nptyping import Array

import numpy as np
from PIL import Image


def apply_mask_pil(image: Image, mask: Array[bool, ..., ...]):
    image = np.asarray(image)
    masked_image = apply_mask(image, mask).filled(0)
    return Image.fromarray(masked_image)


def apply_mask(image, mask: Array[bool, ..., ...]):
    return np.ma.masked_array(image, np.invert(mask))

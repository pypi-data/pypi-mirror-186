from openride import Viewer
from typing import Tuple

import numpy as np
import os
import cv2


def image_to_ascii_art(img: np.ndarray, resolution: Tuple[int, int]) -> str:
    """Convert an Image to ASCII Art"""

    pixels = cv2.resize(img, resolution)
    pixels = np.mean(pixels, axis=-1).astype(int)

    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in np.ravel(pixels)]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index : index + resolution[0]] for index in range(0, new_pixels_count, resolution[0])]
    ascii_image = "\n".join(ascii_image)

    return ascii_image


class AsciiViewer(Viewer):
    def __init__(self, resolution: Tuple[int, int] = (80, 40)):
        super().__init__(
            resolution=resolution, background=(0, 0, 0), mouse_camera_interactions=False, render_offscreen=True
        )

    def update(self):
        rendered_image = super().update(return_image=True)
        ascii_image = image_to_ascii_art(rendered_image, self._resolution)

        clear_console = "clear" if os.name == "posix" else "CLS"
        os.system(clear_console)
        print(ascii_image)

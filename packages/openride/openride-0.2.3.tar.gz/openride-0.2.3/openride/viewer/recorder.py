from typing import Optional, Tuple
from openride.viewer.viewer import get_last_rendered_image
from openride import Viewer
import cv2
import skvideo.io


class Recorder:
    def __init__(self, viewer: Viewer, output_file: str, fps: int = 60, resolution: Optional[Tuple[int, int]] = None):

        self.viewer = viewer
        self.viewer.set_callback(self.update)
        self.resolution = resolution

        self.video_writer = skvideo.io.FFmpegWriter(
            output_file, inputdict={"-r": str(fps)}, outputdict={"-r": str(fps)}
        )

    def update(self):

        image = get_last_rendered_image(self.viewer)

        if not self.resolution:
            self.resolution = (image.shape[0], image.shape[1])

        if (image.shape[0], image.shape[1]) != self.resolution:
            image = cv2.resize(image, self.resolution)

        self.video_writer.writeFrame(image)

    def close(self):
        self.video_writer.close()

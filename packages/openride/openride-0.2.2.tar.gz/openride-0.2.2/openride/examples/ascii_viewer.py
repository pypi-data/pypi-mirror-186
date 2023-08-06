from openride import AsciiViewer, BoundingBox, Point


if __name__ == "__main__":

    box = BoundingBox()

    v = AsciiViewer()

    v.camera.set_position(Point(-8, 0, 2))

    while True:

        box.rotation.yaw += 0.01

        v.draw_bounding_box(box)

        v.update()

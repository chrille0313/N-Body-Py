from Controller.App import App
from Model.Space import Space
from Model.Camera import Camera
from View.SpaceView import SpaceView
from View.CameraView import CameraView

from config import WIDTH, HEIGHT

# TODO: Add typhints (camera) and docstrings

if __name__ == '__main__':
    camera_model = Camera((0, 0))
    camera_view = CameraView(WIDTH, HEIGHT, camera_model)
    space_model = Space(WIDTH, HEIGHT, 10)
    space_view = SpaceView(space_model)
    
    app = App(space_model, space_view, camera_view)
    app.run()

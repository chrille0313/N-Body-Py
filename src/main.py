from Camera import Camera
from Controller.App import App
from Model.Space import Space
from View.SpaceView import SpaceView

from config import WIDTH, HEIGHT

# TODO: Add typhints (camera) and docstrings

if __name__ == '__main__':
    camera = Camera(WIDTH, HEIGHT, (0, 0))
    space_model = Space(WIDTH, HEIGHT, 10)
    space_view = SpaceView(space_model)
    
    app = App(space_model, space_view, camera)
    app.run()
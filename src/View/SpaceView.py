from Model.Space import Space
from View.BodyView import BodyView


class SpaceView:
    def __init__(self, space_model: Space):
        self.space_model = space_model

    def render(self, camera):
        for body in self.space_model.bodies:
            BodyView.render(camera, body)
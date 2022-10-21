from Model.Space import Space
from View.BodyView import BodyView
from Event.EventManager import EventManager
from Event.Event import Event


class SpaceView:
    """
        A view of the game world. Responsible for rendering all objects.
    """

    def __init__(self, space_model: Space):
        self.space_model = space_model

        EventManager.add_listener(Event.EventType.RENDER, self)

    def on_event(self, event):
        camera, camera_view = event.args

        # Render each body
        for body in self.space_model.bodies:
            BodyView.render(camera_view, camera, self.space_model.max_mass, body)

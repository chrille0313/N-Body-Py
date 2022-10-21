import pygame
from Event.Event import Event
from Event.EventManager import EventManager
from pygame.time import Clock


class App:
    """
        The main controller of an app. Owner of the models and views.
    """

    def __init__(self, model, view, camera):
        self.running = False
        self.model = model
        self.view = view
        self.camera = camera

        self.keys = {}
        self.clock = Clock()
        self.target_fps = 144
        self.dt = 1 / self.target_fps  # Time between updates, used to make physics speed independent of fps

    def quit(self):
        self.running = False
    
    def get_input(self):
        self.keys = pygame.key.get_pressed()

    def handle_input(self):
        if self.keys[pygame.K_ESCAPE]:
            self.quit()

        if self.keys[pygame.K_w]:
            EventManager.post(Event(Event.EventType.MOVE_UP, self.dt))
        if self.keys[pygame.K_s]:
            EventManager.post(Event(Event.EventType.MOVE_DOWN, self.dt))
        if self.keys[pygame.K_d]:
            EventManager.post(Event(Event.EventType.MOVE_RIGHT, self.dt))
        if self.keys[pygame.K_a]:
            EventManager.post(Event(Event.EventType.MOVE_LEFT, self.dt))
        if self.keys[pygame.K_q]:
            EventManager.post(Event(Event.EventType.ZOOM_IN, self.dt))
        if self.keys[pygame.K_e]:
            EventManager.post(Event(Event.EventType.ZOOM_OUT, self.dt))

    def handle_app_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def events(self):
        # Handle user input
        self.handle_app_events()
        self.get_input()
        self.handle_input()

    def update(self):
        self.model.update(self.dt)

    def run(self):
        self.running = True

        # The main loop
        while self.running:
            self.dt = self.clock.tick(self.target_fps) / 1000  # Attempts to normalize the time between game loops

            self.events()

            self.update()

            EventManager.post(Event(Event.EventType.APP_UPDATE))

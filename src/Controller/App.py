import pygame
from Event.Event import Event
from Event.EventManager import EventManager


class App:

    def __init__(self, model, view, camera):
        self.running = False
        self.model = model
        self.view = view
        self.camera = camera

        self.keys = self.get_input()

    def quit(self):
        self.running = False
    
    def get_input(self):
        self.keys = pygame.key.get_pressed()

    def handle_input(self):
        if self.keys[pygame.K_ESCAPE]:
            self.quit()

        if self.keys[pygame.K_w]:
            EventManager.post(Event(Event.EventType.MOVE_UP))
        if self.keys[pygame.K_s]:
            EventManager.post(Event(Event.EventType.MOVE_DOWN))
        if self.keys[pygame.K_d]:
            EventManager.post(Event(Event.EventType.MOVE_RIGHT))
        if self.keys[pygame.K_a]:
            EventManager.post(Event(Event.EventType.MOVE_LEFT))
        if self.keys[pygame.K_q]:
            EventManager.post(Event(Event.EventType.ZOOM_IN))
        if self.keys[pygame.K_e]:
            EventManager.post(Event(Event.EventType.ZOOM_OUT))

    def handle_app_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def events(self):
        self.handle_app_events()
        self.get_input()
        self.handle_input()

    def update(self):
        self.model.update()

    def run(self):
        self.running = True

        while self.running:
            self.events()

            self.update()

            EventManager.post(Event(Event.EventType.APP_UPDATE))

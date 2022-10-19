from Event import Event, EventManager


class App:
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True

        while self.running:
            EventManager.post(Event.EventType.GAME_UPDATE)

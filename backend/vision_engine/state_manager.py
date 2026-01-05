import time

class StateManager:
    """
    Ensures state stability using temporal smoothing
    """

    def __init__(self, stable_time=2.5):
        self.stable_time = stable_time
        self.current_state = None
        self.state_start = None

    def update(self, new_state):
        now = time.time()

        if new_state != self.current_state:
            self.current_state = new_state
            self.state_start = now
            return None

        if now - self.state_start >= self.stable_time:
            return self.current_state

        return None

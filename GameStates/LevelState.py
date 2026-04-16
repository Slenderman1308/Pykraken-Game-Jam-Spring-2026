from GameStates.FSM import FSM, StateType
import pykraken as kn

class LevelState(StateType):
    def __init__(self) -> None:
        super().__init__()
        
    def handle_event(self, event: kn.Event) -> None:
        # If the player presses ESCAPE...
        if event.type == kn.KEY_DOWN and event.key == kn.K_ESC:
            # Remove this state from the list
            FSM.exit_state()

    def update(self):
        # Draw a green background for the level
        kn.renderer.clear(kn.Color.GREEN)
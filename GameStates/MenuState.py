from FSM import FSM, StateType
import pykraken as kn

class MenuState(StateType):
	def __init__(self) -> None:
		super().__init__()

	def handle_event(self, event: kn.Event) -> None:
		# If the player presses the ENTER (RETURN) key ...
		if event.type == kn.KEY_DOWN and event.key == kn.K_RETURN:
			# Push the level state on top of the stack
			FSM.enter_state("level")

	def update(self):
		# Draw a blue background for the menu
		kn.renderer.clear(kn.Color.BLUE)
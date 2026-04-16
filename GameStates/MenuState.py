from GameStates.FSM import FSM, StateType
from Assets.Constants import WIN_SIZE
import pykraken as kn

WIN_SIZE = kn.Vec2(*WIN_SIZE)

class MenuState(StateType):
	def __init__(self) -> None:
		super().__init__()

		# Font
		self.font = kn.Font(r"Assets/Fonts/28 Days Later.ttf", 128)

		# Text object
		self.label = kn.Text(self.font, "GAME NAME HERE")

		# Shadow setup (black, soft, offset)
		self.label.shadow_color = kn.Color(0, 0, 0, 40)
		self.label.shadow_offset = kn.Vec2(8, 8)

	def handle_event(self, event: kn.Event) -> None:
		# If the player presses the ENTER (RETURN) key ...
		if event.type == kn.KEY_DOWN and event.key == kn.K_RETURN:
			# Push the level state on top of the stack
			FSM.enter_state("level")

	def update(self):
		# Draw a blue background for the menu
		kn.renderer.clear(kn.Color.BLUE)

		pos = kn.Vec2(WIN_SIZE.x / 2, 60)

		# 1. BLACK OUTLINE LAYER
		self.font.outline = 1
		self.label.color = kn.Color.BLACK
		self.label.draw(pos, kn.Anchor.TOP_MID)

		# 2. WHITE MAIN TEXT
		self.font.outline = 0
		self.label.color = kn.Color.WHITE
		self.label.draw(pos, kn.Anchor.TOP_MID)
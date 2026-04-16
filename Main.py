from GameStates.FSM import FSM
from GameStates.LevelState import LevelState
from GameStates.MenuState import MenuState
from Assets.Constants import WIN_WIDTH, WIN_HEIGHT
import pykraken as kn

class Root:
    def __init__(self) -> None:
        kn.window.create("Game", WIN_WIDTH, WIN_HEIGHT)
        kn.time.set_target(60)

        # 1. Teach the FSM what "level" and "menu" mean
        FSM.register_state("level", lambda: LevelState())
        FSM.register_state("menu", lambda: MenuState())

        # 2. Put the Menu at the bottom of the stack to start the game
        FSM.enter_state("menu")

    def run(self) -> None:
        while kn.window.is_open():
            # 3. Ask the FSM: "Who is at the top of the list?"
            state = FSM.get_current_state()

            if state:
                # 4. Pass inputs to whoever is on top
                for e in kn.event.poll():
                    state.handle_event(e)

                # 5. Tell whoever is on top to draw/update
                state.update()

            kn.renderer.present()

if __name__ == '__main__':
    kn.init(debug=True)
    Root().run()
    kn.quit()
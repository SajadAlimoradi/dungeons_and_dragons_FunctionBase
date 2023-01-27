import asyncio
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from playsound import playsound


def banner() -> None:
    """
    this function run the banner of the game.
    """
    def update_screen(end_time, loop, screen):
        """

        Parameters
        ----------
        end_time : the time of stopping the banner

        loop : define the loop of animation

        screen : define dimension of the game


        Returns
        -------
        this function return nothing
        """
        screen.draw_next_frame()
        if loop.time() < end_time:
            loop.call_later(0.05, update_screen, end_time, loop, screen)
        else:
            loop.stop()

    # Define the scene that you'd like to play.
    screen = Screen.open()
    effects = [
        Cycle(
            screen,
            FigletText("Dungeon  And  Dragon", font='big', width=110),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText(" ", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.set_scenes([Scene(effects, 500)])

    # Schedule the first call to display_date()
    loop = asyncio.new_event_loop()
    end_time = loop.time() + 2.0
    loop.call_soon(update_screen, end_time, loop, screen)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    playsound("D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\winning.mp3")
    loop.close()
    screen.close()

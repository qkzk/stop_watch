"""
Simple stopwatch made using Chat GPT. 
Use pygame zero for interaction.

```sh
$ pip install pgzero
```
"""

import pgzrun
import time

# Window size and title
WIDTH = 400
HEIGHT = 200
TITLE = "Simple Stopwatch - Press SPACE to Start/Pause"


class Stopwatch:
    def __init__(self):
        """Initializes a stopwatch that is not running and has no elapsed time."""
        self.start_time = None
        self.running = False
        self.elapsed_time = 0

    def start(self) -> None:
        """Starts the stopwatch. If already paused, it resumes from where it left off."""
        if not self.running:
            self.running = True
            if self.start_time is None:
                # Initial start
                self.start_time = time.time()
            else:
                # Resume from paused state
                self.start_time = time.time() - self.elapsed_time

    def pause(self) -> None:
        """Pauses the stopwatch and freezes the elapsed time."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def draw(self) -> None:
        """Draws the time on the screen. Running time is white, paused time is grey."""
        hours, minutes, seconds = self.time_in_hms()
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        color = "white" if self.running else "grey"

        # Draw the time in the middle of the screen
        screen.clear()
        screen.fill((0, 0, 0))
        screen.draw.text(
            time_str, center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color=color
        )

    def update_time(self) -> None:
        """Updates the elapsed time if the stopwatch is running."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time

    def time_in_hms(self) -> tuple[int, int, int]:
        """Returns the elapsed time in hours, minutes, and seconds."""
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return hours, minutes, seconds


# Create an instance of the Stopwatch class
stopwatch = Stopwatch()


def draw():
    """Calls the draw method from the Stopwatch class."""
    stopwatch.draw()


def update():
    """Updates the elapsed time if the stopwatch is running."""
    stopwatch.update_time()


def on_key_down(key):
    """Handles the SPACE key press to start/pause the stopwatch."""
    if key == keys.SPACE:
        if stopwatch.running:
            stopwatch.pause()
        else:
            stopwatch.start()
    if key == keys.ESCAPE:
        exit()


# Run the game loop
pgzrun.go()

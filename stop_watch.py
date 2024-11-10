import tkinter as tk
import time


class Stopwatch:
    """
    The stopwatch, which handle the elapsed time since it's running and its reset.
    """

    def __init__(self, label: tk.Label):
        """Initializes a stopwatch that is not running and has no elapsed time."""
        self.label = label
        self.start_time: float | None
        self.elapsed_time: float
        self.running: bool
        self.reset()

    def reset(self) -> None:
        """Reset the stopwatch to its initial values and update the display."""
        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        self.update_display()

    def start(self) -> None:
        """Starts the stopwatch. If already paused, it resumes from where it left off."""
        if not self.running:
            self.running = True
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time = time.time() - self.elapsed_time
                self.running = True
            self.update_time()

    def pause(self) -> None:
        """Pauses the stopwatch and freezes the elapsed time."""
        if self.running and self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            self.update_display()

    def update_time(self) -> None:
        """Updates the elapsed time if the stopwatch is running and refreshes display."""
        if self.running and self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time
            self.update_display()
            self.label.after(50, self.update_time)

    def update_display(self) -> None:
        """Updates the label with the current elapsed time in HH:MM:SS format."""
        hours, minutes, seconds = self.time_in_hms()
        text = f"{hours:02}:{minutes:02}:{seconds:02}"
        fg = "white" if self.running else "grey"
        self.label.config(text=text, fg=fg)

    def time_in_hms(self) -> tuple[int, int, int]:
        """Returns the elapsed time in hours, minutes, and seconds."""
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return hours, minutes, seconds


class Ui:
    """Main tkinter application"""

    def __init__(self):
        self.root = self.build_root()
        self.time_label = self.built_timelabel()
        self.reset_button = self.build_reset_button()
        self.toggle_text = self.build_toggle_text()
        self.toggle_button = self.build_toggle_button()
        self.create_keybinds()

        self.stopwatch = Stopwatch(self.time_label)

    def build_root(self) -> tk.Tk:
        """Returns the main window with title & geometry set."""
        root = tk.Tk()
        root.title("stopwatch")
        root.geometry("250x250")
        return root

    def built_timelabel(self) -> tk.Label:
        """Builds the timelabel which will be updated by the stopwatch itself."""
        time_label = tk.Label(self.root, text="00:00:00", font=("Vera", 42), fg="grey")
        time_label.pack(pady=20)
        return time_label

    def build_reset_button(self) -> tk.Button:
        """Builds a button which will restart the stop watch"""
        reset_button = tk.Button(
            self.root, text="Reset", command=self.reset_stopwatch, font=("Vera", 14)
        )
        reset_button.pack(padx=25, side=tk.LEFT)
        return reset_button

    def build_toggle_text(self) -> tk.StringVar:
        """
        Builds the toggle text string variable which will be updated
        every time the start/pause button is pressed.
        """
        toggle_text = tk.StringVar()
        toggle_text.set("Start")
        return toggle_text

    def build_toggle_button(self) -> tk.Button:
        """Builds the toggle button."""
        toggle_button = tk.Button(
            self.root,
            textvariable=self.toggle_text,
            command=self.toggle_stopwatch,
            font=("Vera", 14),
        )
        toggle_button.pack(padx=25, side=tk.LEFT)
        return toggle_button

    def create_keybinds(self) -> None:
        """Binds the keys to actions"""
        self.root.bind("<space>", self.handle_keypress)
        self.root.bind("<Escape>", self.handle_keypress)
        self.root.bind("<q>", self.handle_keypress)

    def handle_keypress(self, event) -> None:
        """Handle keyboard shortcuts for toggling and exiting."""
        if event.keysym == "space":
            self.toggle_stopwatch()
        elif event.keysym in ("Escape", "q"):
            self.root.quit()

    def toggle_stopwatch(self):
        """Start or pause the stopwatch on button click."""
        if self.stopwatch.running:
            self.stopwatch.pause()
            self.toggle_text.set("Restart")
        else:
            self.stopwatch.start()
            self.toggle_text.set("Pause")

    def reset_stopwatch(self):
        """Reset the stopwatch"""
        self.stopwatch.reset()
        self.toggle_text.set("Start")


ui = Ui()
ui.root.mainloop()

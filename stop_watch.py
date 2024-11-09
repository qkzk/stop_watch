import tkinter as tk
import time


class Stopwatch:
    def __init__(self, label: tk.Label):
        """Initializes a stopwatch that is not running and has no elapsed time."""
        self.label = label
        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        self.update_display()

    def start(self):
        """Starts the stopwatch. If already paused, it resumes from where it left off."""
        if not self.running:
            self.running = True
            if self.start_time is None:
                # Initial start
                self.start_time = time.time()
            else:
                # Resume from paused state
                self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def pause(self):
        """Pauses the stopwatch and freezes the elapsed time."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def update_time(self):
        """Updates the elapsed time if the stopwatch is running and refreshes display."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.update_display()
            # Schedule the next update
            self.label.after(50, self.update_time)

    def update_display(self):
        """Updates the label with the current elapsed time in HH:MM:SS format."""
        hours, minutes, seconds = self.time_in_hms()
        text = f"{hours:02}:{minutes:02}:{seconds:02}"
        fg = "white" if self.running else "grey"
        self.label.config(text=text, fg=fg)

    def time_in_hms(self):
        """Returns the elapsed time in hours, minutes, and seconds."""
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return hours, minutes, seconds


# Initialize the main tkinter window
root = tk.Tk()
root.title("stop_watch")

# Create a label to display the time
time_label = tk.Label(root, text="00:00:00", font=("Vera", 42), fg="grey")
time_label.pack(pady=20)

# Create an instance of the Stopwatch class
stopwatch = Stopwatch(time_label)


def toggle_stopwatch():
    """Start or pause the stopwatch on button click."""
    if stopwatch.running:
        stopwatch.pause()
    else:
        stopwatch.start()


def handle_keypress(event):
    """Handle keyboard shortcuts for toggling and exiting."""
    if event.keysym == "space":
        toggle_stopwatch()
    elif event.keysym in ("Escape", "q"):
        root.quit()


# Add a button to control the stopwatch
toggle_button = tk.Button(
    root, text="Start / Pause", command=toggle_stopwatch, font=("Helvetica", 14)
)
toggle_button.pack(pady=10)

# Bind the keyboard shortcuts
root.bind("<space>", handle_keypress)
root.bind("<Escape>", handle_keypress)
root.bind("<q>", handle_keypress)

# Start the tkinter main loop
root.mainloop()

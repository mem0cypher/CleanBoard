from pystray import MenuItem, Icon
from PIL import Image, ImageDraw

def create_image(color1, color2):
    """Creates a 64x64 icon."""
    image = Image.new('RGB', (64, 64), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (32, 0, 64, 64),
        fill=color2)
    return image

class TrayIcon:
    """Manages the system tray icon."""

    def __init__(self, keyboard_handler):
        self.keyboard_handler = keyboard_handler
        self.icon = None

        self.icon_locked = create_image('red', 'red')
        self.icon_unlocked = create_image('green', 'green')

    def _setup_icon(self):
        """Sets up the tray icon and menu."""
        menu = (
            MenuItem('Toggle Lock', self._on_toggle_lock),
            MenuItem('Exit', self._on_exit)
        )
        self.icon = Icon("CleanBoard", self.icon_unlocked, "CleanBoard", menu)

    def _on_toggle_lock(self, icon, item):
        """Callback for the 'Toggle Lock' menu item."""
        self.keyboard_handler.toggle_lock()

    def _on_exit(self, icon, item):
        """Callback for the 'Exit' menu item."""
        self.keyboard_handler.unlock()
        self.icon.stop()

    def update_icon(self):
        """Updates the tray icon to reflect the lock state."""
        if self.keyboard_handler.is_locked:
            self.icon.icon = self.icon_locked
        else:
            self.icon.icon = self.icon_unlocked

    def run(self):
        """Runs the tray icon."""
        self._setup_icon()
        self.icon.run() 
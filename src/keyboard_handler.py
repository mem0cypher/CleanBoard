import keyboard
import logging

class KeyboardHandler:
    """Handles keyboard locking and unlocking."""

    def __init__(self):
        self.is_locked = False
        self._hook = None
        self.tray_icon = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    def set_tray_icon(self, tray_icon):
        """Sets the tray icon instance."""
        self.tray_icon = tray_icon

    def lock(self):
        """Locks the keyboard."""
        if not self.is_locked:
            # Block all keys
            self._hook = keyboard.hook(lambda e: False, suppress=True)
            self.is_locked = True
            logging.info("Keyboard locked.")
            if self.tray_icon:
                self.tray_icon.update_icon()

    def unlock(self):
        """Unlocks the keyboard."""
        if self.is_locked:
            keyboard.unhook_all()
            self._hook = None
            self.is_locked = False
            logging.info("Keyboard unlocked.")
            if self.tray_icon:
                self.tray_icon.update_icon()

    def toggle_lock(self):
        """Toggles the keyboard lock state."""
        if self.is_locked:
            self.unlock()
        else:
            self.lock() 
import keyboard
import logging
from .keyboard_handler import KeyboardHandler
from .tray_icon import TrayIcon

def main():
    """Main function to run the application."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Application starting...")
    kh = KeyboardHandler()
    ti = TrayIcon(kh)
    kh.set_tray_icon(ti)

    # Set up the global hotkey
    keyboard.add_hotkey('ctrl+alt+l', kh.toggle_lock)

    # Run the tray icon
    ti.run()
    logging.info("Application shutting down.")

if __name__ == "__main__":
    main() 
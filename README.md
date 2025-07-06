# CleanBoard

A simple Windows utility to quickly lock and unlock your keyboard with a global hotkey, managed from your system tray.

![CleanBoard Demo](https://i.imgur.com/your-demo-image.gif) <!-- Replace with a real GIF if you make one! -->

## Features

- **System Tray Icon**: Easily see the keyboard's lock status at a glance.
  - **Green Icon**: Keyboard is unlocked.
  - **Red Icon**: Keyboard is locked.
- **Global Hotkey**: Press `Ctrl+Alt+L` anywhere in Windows to instantly toggle the keyboard lock.
- **Right-Click Menu**: Use the tray icon menu to toggle the lock or exit the application.
- **Lightweight**: Uses minimal system resources.

## Getting Started

There are two ways to use CleanBoard: by running the source code directly or by downloading the pre-built executable.

### Option 1: For Users (Easy)

You can download the latest `CleanBoard.exe` from the **[Releases](https://github.com/your-username/your-repo-name/releases)** page.

No installation is needed. Just download the file and run it.

### Option 2: For Developers (From Source)

If you have Python on your system, you can run the project from its source code.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```sh
    python run.py
    ```

## Building the Executable (Optional)

If you want to build the `.exe` from the source code yourself, you can use PyInstaller.

1.  **Make sure you have installed the requirements:**
    ```sh
    pip install -r requirements.txt
    pip install pyinstaller
    ```

2.  **Run the build command:**
    ```sh
    pyinstaller --onefile --windowed --name CleanBoard run.py
    ```

3.  The final `CleanBoard.exe` will be located in the `dist` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
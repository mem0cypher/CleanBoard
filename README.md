# CleanBoard

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mem0cypher/CleanBoard/blob/main/LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/mem0cypher/CleanBoard)](https://github.com/mem0cypher/CleanBoard/releases/latest)

A simple and lightweight Windows utility to quickly lock and unlock your keyboard with a global hotkey, managed entirely from your system tray.

![CleanBoard Demo](https://i.imgur.com/your-demo-image.gif) <!-- It's highly recommended to replace this with a real GIF of your application in action! -->

## Why CleanBoard?

Ever need to clean your keyboard without unplugging it? Or keep a cat from walking across your desk and typing a novel? CleanBoard is a hassle-free solution. It runs quietly in the background, giving you an instant and reliable way to disable your keyboard without interrupting your workflow.

## Features

- **Instant Keyboard Lock**: Use the global hotkey `Ctrl+Alt+L` to lock or unlock your keyboard at any time.
- **System Tray Management**: The application lives in your system tray for easy access.
  - 🟢 **Green Icon**: Keyboard is unlocked and ready to use.
  - 🔴 **Red Icon**: Keyboard is locked and all input is blocked.
- **Simple Menu**: Right-click the tray icon to toggle the lock or safely exit the application.
- **Extremely Lightweight**: Designed to use minimal CPU and memory resources.
- **Portable**: No installation required. Just run the `.exe` file.

## Getting Started

### For Most Users (Recommended)

1.  Go to the **[Releases](https://github.com/mem0cypher/CleanBoard/releases)** page.
2.  Download the `CleanBoard.exe` file from the latest release.
3.  Run it. That's it!

### For Developers

If you want to run the application from the source code:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/mem0cypher/CleanBoard.git
    cd CleanBoard
    ```

2.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```sh
    python run.py
    ```

## Building From Source

Want to create your own `CleanBoard.exe`?

1.  **Ensure all dependencies are installed, including PyInstaller:**
    ```sh
    pip install -r requirements.txt
    pip install pyinstaller
    ```

2.  **Run the PyInstaller build command:**
    ```sh
    pyinstaller --onefile --windowed --name CleanBoard run.py
    ```

3.  Your new executable will be ready in the `dist` folder.

## Contributing

Contributions are welcome! If you have ideas for new features or have found a bug, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
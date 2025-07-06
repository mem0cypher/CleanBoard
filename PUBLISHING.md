# Publishing to GitHub

This document provides instructions on how to publish the CleanBoard application to GitHub.

## 1. Initialize a Git Repository

If you haven't already, initialize a Git repository in your project folder:
```sh
git init
git add .
git commit -m "Initial commit"
```

## 2. Create a Repository on GitHub

1.  Go to [GitHub](https://github.com) and log in to your account.
2.  Click the **+** icon in the top-right corner and select **New repository**.
3.  Fill in the repository details:
    -   **Repository name:** `CleanBoard`
    -   **Description:** A simple utility to temporarily lock your keyboard for cleaning.
    -   Choose **Public** or **Private**.
4.  Click **Create repository**.

## 3. Push to GitHub

Once you've created the repository on GitHub, you'll see instructions on how to push your local repository.

```sh
# Replace 'your-username' with your GitHub username
git remote add origin https://github.com/your-username/CleanBoard.git
git branch -M main
git push -u origin main
```

## 4. Create a Release

After you have built the application using PyInstaller, you can create a release on GitHub to share the executable with others.

1.  Go to your repository on GitHub.
2.  Click on the **Releases** tab on the right side.
3.  Click **Create a new release** or **Draft a new release**.
4.  Enter a tag version (e.g., `v1.0.0`).
5.  Enter a release title and description.
6.  In the **Attach binaries** section, upload the `CleanBoard` folder (or a zip of it) from the `dist` directory.
7.  Click **Publish release**. 
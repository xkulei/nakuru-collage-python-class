# Student guide: Understanding a Python video downloader

This guide explains the code shown in class, line by line. The program asks for a video URL in the terminal, opens a folder selection window, chooses a downloadable MP4 video stream, and saves it to that folder. Use an instructor-provided video that you are permitted to download for practice.

## Learning goals

After this lesson, you should be able to:

1. Explain the difference between a module, package, library, and Python's standard library.
2. Read three common forms of `import`.
3. Trace data from `input()` through functions to a downloaded file.
4. Explain `try`/`except`, `if`, `return`, and the `__main__` guard.
5. Identify what happens when the user cancels the folder dialog or no suitable stream is found.

## 1. Modules, packages, and libraries

A **module** is usually one Python file containing reusable code. A **package** is a collection of related modules, commonly organized in a folder. A **library** is the broader everyday term for reusable code; it may contain one module or many packages. The **standard library** is the collection that comes with Python. A **third-party package** is installed separately, commonly with `pip`. Python's own documentation describes modules and packages in more detail: [Python tutorial: Modules](https://docs.python.org/3/tutorial/modules.html).

| Name in this program | What it is | Why the program uses it | Installation |
| --- | --- | --- | --- |
| `pytube` | Third-party Python package/library | Accesses video information, available streams, and download methods | Install separately with `pip` |
| `YouTube` | Class imported from `pytube` | Creates an object representing one video URL | Comes from `pytube` |
| `tkinter` | Python GUI package in the standard library | Creates the hidden root window needed for the dialog | Usually included with a Python installation that has Tcl/Tk support |
| `filedialog` | Module within `tkinter` | Opens a folder picker | Comes with `tkinter` |

**Do not mix up these ideas:** `import` makes code available to your program; `pip install` puts a third-party package into a Python environment. You install `pytube` once for an environment, then import it in each program that needs it. You do not use `pip install` for `tkinter` in a normal Python installation.

### The three import lines

```python
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
```

- `from pytube import YouTube` brings the name `YouTube` directly into this file. We can write `YouTube(url)` instead of `pytube.YouTube(url)`.
- `import tkinter as tk` imports the package and gives it the shorter local name `tk`. We then write `tk.Tk()`.
- `from tkinter import filedialog` brings in the dialog module under its own name. We then write `filedialog.askdirectory()`.

`as tk` changes only the name used in this file; it does not rename or modify the installed package.

## 2. Setup and running the program

On Windows, open a terminal in your project folder and run:

```powershell
py -m pip install pytube
py -c "import pytube; import tkinter; print('Imports work')"
py youtube_downloader_example.py
```

On macOS/Linux, the command is usually `python3` instead of `py`. If the import check fails, make sure `pip` installed the package into the same Python interpreter that runs the file. You can test Tkinter separately with `py -m tkinter`; Python documents this as a way to check that Tkinter is installed correctly: [Tkinter documentation](https://docs.python.org/3/library/tkinter.html).

The downloader needs a graphical desktop for the folder picker and a network connection for the video. Installing `pytube` does not guarantee that every video will be accessible; online video services and library behavior can change.

## 3. The code we are studying

The companion file [youtube_downloader_example.py](youtube_downloader_example.py) matches the screenshot. The line numbers below match both the screenshot and that file. Blank lines separate sections and do not change the result.

```python
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
```

## 4. Line-by-line explanation

### Imports and the download function

| Line | Code | What it does |
| --- | --- | --- |
| 1 | `from pytube import YouTube` | Gets the `YouTube` class from the third-party `pytube` package. If the package is not installed in the active environment, the program stops here with `ModuleNotFoundError`. |
| 2 | `import tkinter as tk` | Loads Tkinter under the short name `tk`. |
| 3 | `from tkinter import filedialog` | Makes Tkinter's dialog module available as `filedialog`. |
| 5 | `def download_video(url, save_path):` | Defines a function with two parameters. `url` will receive the text entered by the user. `save_path` will receive the chosen folder path. Defining the function does not run its body yet. |
| 6 | `try:` | Begins a block of code that might raise an exception. If a caught exception occurs within this block, execution jumps to line 12. |
| 7 | `yt = YouTube(url)` | Constructs a `YouTube` object for the supplied URL and stores it in `yt`. An **object** bundles data and operations related to one thing. |
| 8 | `streams = yt.streams.filter(progressive=True, file_extension="mp4")` | Gets the video's available streams, then keeps only **progressive** streams in MP4 format. A stream is one available version of the video. `progressive=True` means one stream contains both video and audio. The filtered result is stored in `streams`. |
| 9 | `highest_res_stream = streams.get_highest_resolution()` | Selects the highest-resolution stream **from the filtered choices**. It does not promise the highest resolution shown on the video website. If there are no matching streams, the result may be `None`. |
| 10 | `highest_res_stream.download(output_path=save_path)` | Calls the selected stream's `download()` method. `output_path=save_path` is a **keyword argument** telling `pytube` which directory to save into. The library chooses a filename unless one is supplied. |
| 11 | `print("Video downloaded successfully!")` | Runs after `download()` returns without raising an exception. It prints to the terminal. |
| 12 | `except Exception as e:` | Catches many errors raised in the `try` block and gives the error object the temporary name `e`. It also catches an error if line 9 returned `None` and line 10 tries to call `.download()` on it. |
| 13 | `print(e)` | Displays the error message in the terminal. This helps with diagnosis, but beginners may need more context to understand it. |

**Important quality note:** The filter in line 8 asks for a video-and-audio MP4 in one file. The [pytube stream guide](https://github.com/pytube/pytube/blob/master/docs/user/streams.rst) explains that these progressive choices can be lower resolution than separate video and audio streams. Selecting the “highest” stream here means highest among the matching progressive MP4 options. The [pytube query source](https://github.com/pytube/pytube/blob/master/pytube/query.py) also shows that `get_highest_resolution()` can return `None`.

### The folder picker function

| Line | Code | What it does |
| --- | --- | --- |
| 15 | `def open_file_dialog():` | Defines a second function. Despite its name, this function chooses a **folder**, not a file. |
| 16 | `folder = filedialog.askdirectory()` | Opens a graphical folder picker. If the user selects a folder, `folder` is its path as a string; if the user cancels, it is an empty string. See [Python's dialog documentation](https://docs.python.org/3/library/dialog.html). |
| 17 | `if folder:` | Checks whether `folder` is non-empty. An empty string is treated as false in an `if` statement. |
| 18 | `print(f"Selected folder: {folder}")` | Prints the path selected by the user. The `f` makes this an **f-string**; `{folder}` is replaced with the variable's value. |
| 20 | `return folder` | Sends the folder path back to the code that called the function. If the user cancelled, it returns the empty string. `return` is different from `print`: it supplies a value that other code can use. |

### The part that runs when the script starts

| Line | Code | What it does |
| --- | --- | --- |
| 22 | `if __name__ == "__main__":` | Runs the following indented block only when this file is executed directly. When another Python file imports it, the functions are available but the prompts do not start automatically. This is called the **main guard**. See [Python's modules tutorial](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts). |
| 23 | `root = tk.Tk()` | Creates Tkinter's root window and initializes the GUI toolkit. |
| 24 | `root.withdraw()` | Hides that main window, leaving the folder dialog as the visible GUI. The root still exists until the program ends or it is destroyed. See [Tkinter's `withdraw()` documentation](https://docs.python.org/3/library/tkinter.html#tkinter.Tk.withdraw). |
| 26 | `video_url = input("Please enter a YouTube url: ")` | Displays a prompt in the terminal and stores the entered URL as a string. This part is **not** a graphical text box. |
| 27 | `save_dir = open_file_dialog()` | Calls the folder picker function and stores its returned path (or empty string) in `save_dir`. |
| 29 | `if save_dir:` | Continues only if a folder was selected. |
| 30 | `print("Started download...")` | Tells the user the download is starting. It does not confirm that a file has been saved. |
| 31 | `download_video(video_url, save_dir)` | Calls the first function. The entered URL becomes `url`, and the chosen folder becomes `save_path`. |
| 32 | `else:` | Starts the alternative path when no folder was selected. |
| 33 | `print("Invalid save location.")` | Prints this message when the folder picker was cancelled or returned an empty path. It does not check whether a non-empty path is writable. |

## 5. Trace the data through the program

```text
Terminal input: video URL ──> video_url ──> download_video(url, save_path)
Folder dialog: directory ──> save_dir ───────┘
                                            │
                                            ▼
                              YouTube object → available streams
                                            │
                                            ▼
                            progressive MP4 stream → saved file
```

There are **two kinds of input**: the URL is typed in the terminal, while the directory is picked in a graphical window. The output is also in two places: messages in the terminal and a video file in the selected directory.

### Example walkthrough (illustrative, not a recorded run)

Suppose the URL entered is `https://www.youtube.com/watch?v=EXAMPLE` and the chosen folder is `C:\Users\Student\Videos`.

1. `video_url` becomes the URL string.
2. `open_file_dialog()` returns the folder path, so `save_dir` becomes `C:\Users\Student\Videos`.
3. Because `save_dir` is not empty, line 31 calls `download_video()`.
4. Inside that function, `url` refers to the URL and `save_path` refers to the folder.
5. If the library finds a matching stream and downloads it, the terminal prints `Video downloaded successfully!`.

The example URL is a placeholder; it is not a real video to download.

## 6. What can happen when you run it?

| Situation | What this code does | Why |
| --- | --- | --- |
| User chooses a folder and download works | Prints the selected folder, `Started download...`, and a success message | The `if save_dir` branch and the `try` block complete |
| User cancels the folder picker | Prints `Invalid save location.` | `askdirectory()` returns an empty string |
| `pytube` is missing | Stops at line 1 with `ModuleNotFoundError` | Imports happen before the functions run |
| URL is wrong or video is unavailable | Usually prints an exception message | The library may raise an error while fetching information or downloading |
| No progressive MP4 stream is available | The selected stream may be `None`, then line 10 raises an error | The filter found no matching choice |
| Network drops or folder cannot be written | Usually prints an exception message | The download cannot finish |

The program's `except Exception` is a broad safety net. It shows the error but does not distinguish the different causes. Also, the `try` block covers only the download function; it does **not** cover errors in the import lines, Tkinter setup, or folder dialog.

## 7. Key Python ideas in this program

- **Function:** `download_video` and `open_file_dialog` are reusable named blocks.
- **Parameter versus argument:** In `def download_video(url, save_path)`, `url` and `save_path` are parameters. In `download_video(video_url, save_dir)`, `video_url` and `save_dir` are the arguments passed to them.
- **Object and method:** `yt` is an object. `.filter()`, `.get_highest_resolution()`, and `.download()` are methods called on objects.
- **Variable assignment:** `=` stores a value, as in `save_dir = open_file_dialog()`.
- **Comparison:** `==` compares values, as in `__name__ == "__main__"`.
- **Conditional:** `if` chooses a path based on a condition; `else` is the other path.
- **Exception:** An error that interrupts normal execution; `try`/`except` can catch it.
- **Indentation:** All lines indented under `def`, `try`, `if`, and `else` belong to those blocks. Python uses indentation as part of its syntax.

## 8. Small improvements to discuss after students understand the original

These are teaching extensions, not changes to the screenshot's code:

1. **Check for no stream:** After line 9, test `if highest_res_stream is None:` and show `No suitable MP4 stream found.` before trying `.download()`.
2. **Show where the file went:** `download()` returns a path. Store it with `file_path = highest_res_stream.download(output_path=save_path)` and print `file_path`.
3. **Clean up Tkinter:** After the folder dialog finishes, call `root.destroy()` to close the hidden root window explicitly.
4. **Handle user input:** Use `.strip()` on the URL to remove accidental spaces at either end.
5. **Improve error messages:** Show a short friendly message and the exception text rather than only `print(e)`.

## 9. Practice questions

1. Is `pytube` part of the standard library? How do you make it available?
2. What does `as tk` do in the import statement?
3. Does `root.withdraw()` delete the Tkinter window?
4. Why does the program use `if save_dir:` before calling `download_video()`?
5. Which line chooses the highest resolution, and highest among **which** streams?
6. If line 9 returns `None`, what goes wrong on the next line?
7. What is the difference between `print(folder)` and `return folder`?
8. Why is the URL entered in the terminal even though `tkinter` is imported?
9. What does the `__main__` condition prevent when this file is imported elsewhere?
10. How would you print the exact path of the saved file after a successful download?

### Answer key

1. No. Install it into the Python environment with `python -m pip install pytube`, then import it.
2. It gives `tkinter` a shorter name in this file.
3. No. It hides the window; `destroy()` would remove it.
4. A cancelled picker returns an empty string, so there is no folder to save into.
5. Line 9. It chooses from the progressive MP4 streams filtered on line 8.
6. `None` has no `.download()` method, so an exception is raised and caught at line 12.
7. `print` displays text; `return` sends a value back to the caller.
8. The code uses `input()` for the URL; Tkinter is used only for selecting the destination folder.
9. It prevents the interactive prompts and download workflow from starting on import.
10. Store the return value of `download()` in a variable and print that variable.

## References

- [Python: Modules and packages](https://docs.python.org/3/tutorial/modules.html)
- [Python: Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python: Tkinter dialogs](https://docs.python.org/3/library/dialog.html)
- [pytube stream guide](https://github.com/pytube/pytube/blob/master/docs/user/streams.rst)
- [pytube project README](https://github.com/pytube/pytube)

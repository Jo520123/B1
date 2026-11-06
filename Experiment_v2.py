from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import pandas as pd

WATCH_Folder = "watchdog-folder"

class fileHandler(FileSystemEventHandler):
    def on_created(self, event):

        if not event.is_directory:

            time.sleep(1)

            filename = os.path.basename(event.src_path)

            print(f"Detected file: {filename}")



if __name__ == "__main__":
    os.makedirs(WATCH_Folder, exist_ok=True)

    observer = Observer()
    observer.schedule(fileHandler(), WATCH_Folder, recursive=False)

    observer.start()

    print(f" Watching folder: {WATCH_Folder}")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

        print("Stop the Observer !")

        observer.join()

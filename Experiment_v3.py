
import time
import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WatchDirectory = "CSV"


class CSVHandler(FileSystemEventHandler):



    def on_created(self, event):

        if not event.is_directory and event.src_path.endswith(".csv"):

            time.sleep(1)

            #file_path = os.path.basename(event.src_path)

            file_path = event.src_path

            print(f"\n[Detected] New CSV file arrived: {file_path}")

            time.sleep(1)

            try:
                self.process_csv(file_path)

            except Exception as e:
                print(f"[Error] Failed to process {file_path}: {e}")


    def process_csv(self, file_path):


        print(f"[Processing] Running logic on: {file_path}")


        df = pd.read_csv(file_path)

        print(f"Raw count: {len(df)}")

        print(f"data:", df.head())

        print(f"[Complete] Finished processing {os.path.basename(file_path)}")





if __name__ == "__main__":

    """
    if not os.path.exists(WatchDirectory):
        os.makedirs(WatchDirectory)
        print(f"Created Directory : {WatchDirectory}")
    """

    os.makedirs(WatchDirectory, exist_ok=True)


    #eventHandler = CSVHandler()
    observer = Observer()

    observer.schedule(CSVHandler(), WatchDirectory, recursive= False)

    print(f"Starting file watcher on directory: {os.path.abspath(WatchDirectory)}")
    print("Drop a CSV file into the folder to test. Ctrl + C to stop.")

    print(f"Watching Folder: {WatchDirectory}")

    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

        print("\nStopping file watcher...")

    observer.join()


    print("eeeeeeeeee")

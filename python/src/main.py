from typing import Union
from fastapi import FastAPI
import shutil
from time import gmtime, strftime
import os
import json


app = FastAPI()

# mount path
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mnt')


@app.get("/")
def read_root():

    print(dest)

    timestamp = strftime("%m%d%H%M%S", gmtime())

    response = {"time": timestamp}

    with open(f'{dest}/{timestamp}.json', 'w') as file:
        json.dump(response, file, indent=4)

    return response


@app.get('/files')
def read_files():

    def list_files_in_directory(path):
        try:
            return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        except FileNotFoundError:
            print("Directory not found.")
            return []
        except NotADirectoryError:
            print("The path provided is not a directory.")
            return []

    # Example usage
    files = list_files_in_directory(dest)

    return {"files": files}


@app.get("/health", status_code=200)
def health():
    print('health checked')
    return {}

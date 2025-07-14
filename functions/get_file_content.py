import os
from functions.config import *

def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    if not path.startswith(working_directory):
        return f'Error: Cannot read "{path}" as it is outside the permitted working directory'
    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{path}"'
    
    try:
        with open(os.path.abspath(path), "r") as f:
            file_content_string = f.read(MAX_CHARS)
            extra = f.read(1)
            if extra != '':
                return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
    

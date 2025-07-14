import os
from functions.get_file_content import get_file_content

def write_file(working_directory, file_path, content):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        dirname = os.path.dirname(abs_file_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
            return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    

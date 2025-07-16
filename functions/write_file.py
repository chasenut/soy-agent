import os
from functions.get_file_content import get_file_content
from google.genai import types

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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a new content to a file (and makes the file if it doesn't exist) overwritting the old one.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to a file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The whole new content of a file",
            ),
        },
    ),
)


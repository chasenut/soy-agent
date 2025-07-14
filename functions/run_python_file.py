import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process = subprocess.run(["python3", str(abs_file_path)], timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       
        output = []
        output.append(f"STDOUT:{process.stdout}")
        output.append(f"STDERR:{process.stderr}")
        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")
        if process.stdout == None:
            return "No output produced"
        output = "\n".join(output)
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

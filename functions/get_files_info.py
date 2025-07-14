import os

def get_files_info(working_directory, directory=None):
    if directory:
        path = os.path.join(working_directory, directory) 
    else: 
        path = working_directory
    if not path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    contents = []
    try:
        for element in os.listdir(path):
            entry = os.path.join(path, element)
            size = os.path.getsize(entry)
            is_dir = os.path.isdir(entry)
            str = f"- {element}: file_size={size} bytes, is_dir={is_dir}"
            contents.append(str)
    except Exception as e:
        return f"Error: {e}"
    return "\n".join(contents)

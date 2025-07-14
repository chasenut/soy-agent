import os

def get_files_info(working_directory, directory=None):
    if directory:
        abs_dir_path = os.path.abspath(os.path.join(working_directory, directory)) 
    else: 
        abs_dir_path = os.path.abspath(working_directory)
    if not abs_dir_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_dir_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = []
    try:
        for element in os.listdir(abs_dir_path):
            entry = os.path.join(abs_dir_path, element)
            size = os.path.getsize(entry)
            is_dir = os.path.isdir(entry)
            str = f"- {element}: file_size={size} bytes, is_dir={is_dir}"
            contents.append(str)
    except Exception as e:
        return f"Error: {e}"
    return "\n".join(contents)

import os


def list_all_files(folder_path: str):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(os.path.join(root, file), folder_path)
            all_files.append([full_file_path, relative_file_path])
    return all_files

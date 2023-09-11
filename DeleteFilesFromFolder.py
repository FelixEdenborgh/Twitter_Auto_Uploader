import os

def delete_all_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


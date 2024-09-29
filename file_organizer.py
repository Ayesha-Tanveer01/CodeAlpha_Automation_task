import os
import shutil

folder_to_sort = r'E:\Users\PMLS\Music\sorting_folder_for_python' 

file_extensions = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Word_documents' : ['.docx'],
    'Text_files' : ['.txt'],
    'PDF' : ['.pdf'],
    'Excel_sheets' : ['.xlsx'],
    'Presentations' : ['.pptx'],
    'Videos': ['.mp4'],
    'Audio': ['.opus'],
    'Archives': ['.zip', '.rar'],
    'Applications': ['.exe', '.msi']
}

for folders in file_extensions.keys():
    folder_path = os.path.join(folder_to_sort, folders) # to complete the folder path by adding the names of sub-folders to the path of main folder
    if not os.path.exists(folder_path): # creating a sub-folder if it does not exist
        os.mkdir(folder_path)


def organize_files():
    for file_name in os.listdir(folder_to_sort): # it will iterate over each file in the main folder
        file_ext = os.path.splitext(file_name)[1].lower()    # to get extensions of files
        file_path = os.path.join(folder_to_sort, file_name)   # to complete the file path by adding the names of files to the path of main folder
        if os.path.isfile(file_path):      # check if the provided path contains a file or a folder
            moved = False
            # Move the file based on its extension
            for folder_name, extensions in file_extensions.items():
                if file_ext in extensions:
                    destination_folder = os.path.join(folder_to_sort, folder_name)
                    shutil.move(file_path, os.path.join(destination_folder, file_name))
                    print(f'Moved: {file_name} to {folder_name}')
                    moved = True
                    break

            # If the file doesn't match any extension, move it to 'Others'
            if not moved:
                others_folder = os.path.join(folder_to_sort, 'Others')
                if not os.path.exists(others_folder):
                    os.mkdir(others_folder)
                shutil.move(file_path, os.path.join(others_folder, file_name))
                print(f'Moved: {file_name} to Others')

# Run the file organization
organize_files()

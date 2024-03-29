import os
import shutil

from_dir = "./Downloads" 
to_dir = "./Document_Files"

# Get list of files in the source directory
list_of_files = os.listdir(from_dir)

# Print the list of files
print("List of files in the source directory:")
print(list_of_files)

# Traverse through the list of files
for file_name in list_of_files:
    # Split file name and extension
    name, extension = os.path.splitext(file_name)
    
    # Skip if extension is blank
    if not extension:
        continue
    
    # Check if the extension is in the list of allowed extensions
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    if extension.lower() in allowed_extensions:
        # Define paths
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)
        
        # Check if destination directory exists, if not, create it
        if not os.path.exists(path2):
            os.makedirs(path2)
        
        # Move the file
        shutil.move(path1, path3)
        
        # Print message
        print(f"Moved {file_name} to {path3}")

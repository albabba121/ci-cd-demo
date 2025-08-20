import os

# Set the folder path and the line to append
folder_path = "ENTER FOLDER"
line_to_append = ", 3D render"
# Loop through all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "a") as f:
            f.write(line_to_append)
        print(f"Appended to: {filename}")

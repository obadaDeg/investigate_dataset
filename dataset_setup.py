import kagglehub
import shutil
import os

# Download latest version
def setup():
    path = kagglehub.dataset_download("joniarroba/noshowappointments")

    # Define the destination directory
    destination_path = r"C:\Users\obada\Desktop\investigate_dataset"


    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    # Move the dataset files to the new location
    for file_name in os.listdir(path):
        shutil.move(os.path.join(path, file_name), destination_path)

    print("Dataset moved to:", destination_path)


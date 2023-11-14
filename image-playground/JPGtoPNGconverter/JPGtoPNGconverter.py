from os.path import isdir, isfile, join
import sys
import os
from PIL import Image

def is_valid_directory(source_dir):
    source = os.path.join(os.getcwd(),source_dir)

    if os.path.isdir(source):
        source_contents = os.listdir(source)
        if not source_contents:
            print("Provided source directory is empty.")
            return False
        jpg_files = [f for f in source_contents if isfile(join(source,f)) and f.lower().endswith('.jpg')]
        if not jpg_files:
            print("Source directory doesn't contain any image file with 'jpg' extension")
            return False
        return True
    else:
        print("Source is not a directory")
        return False

if len(sys.argv) >= 3:
    script_name = sys.argv[0] # the first argument is always python file we're executing
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    

    if is_valid_directory(source_dir):
    # Ensure the destination directory exists
        destination = os.path.join(os.getcwd(), destination_dir)
        os.makedirs(destination, exist_ok=True)

    # Get a list of JPEG files in the source directory
        jpg_files = [f for f in os.listdir(source_dir) if isfile(join(source_dir, f)) and f.lower().endswith('.jpg')]

        for jpg_file in jpg_files:
        # Open the JPEG image
            jpg_path = os.path.join(source_dir, jpg_file)
            with Image.open(jpg_path) as img:
            # Convert the image to PNG
                png_path = os.path.join(destination, os.path.splitext(jpg_file)[0] + '.png')
                img.save(png_path, 'PNG')
                print(f"Converted {jpg_file} to {os.path.basename(png_path)}")

    else:
    # Handle the case where the source directory is not valid
        print("Source directory is not valid. Cannot proceed with conversion.")


else:
    print("Please provide 2 directories as arguments \n 1. Source directory \n 2. Destination directory")


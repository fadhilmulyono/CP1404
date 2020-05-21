"""
CP1404/CP5632 Practical
Sort Files 1.0
"""
import os


def main():
    """Sort files to folders based on extension"""

    # Specify directory
    os.chdir('FilesToSort')

    for filenames in os.listdir('.'):
        # Check if there are any files in directory
        if os.path.isdir(filenames):
            continue

        # Split the filename between the file name and extension
        extension = filenames.split('.')[-1]
        # If folder does not exist in directory, create the folder
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        # Move the files to the folders that were just created
        os.rename(filenames, "{}/{}".format(extension, filenames))
        print()

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains files:", filenames)


main()

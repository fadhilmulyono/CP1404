"""
CP1404/CP5632 Practical
Sort Files 2.0
"""
import os

# List/dictionary for files and their extensions
EXTENSIONS = {'doc': 'Docs',
              'docx': 'Docs',
              'txt': 'Docs',
              'png': 'Images',
              'gif': 'Images',
              'jpg': 'Images',
              'xls': 'Spreadsheets',
              'xlsx': 'Spreadsheets'}


def main():
    """Sort files to folders based on user input, depending on file extensions"""
    extension_to_category = {}

    # Specify directory
    os.chdir('FilesToSort')

    for filenames in os.listdir('.'):
        # Check if there are any files in directory
        if os.path.isdir(filenames):
            continue

        # Split the filename between the file name and extension
        extension = filenames.split('.')[-1]

        # If there are no files in the root folder, skip
        if extension not in extension_to_category:
            # Prompt for user input to create folder to store all files based on given extension
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            # If folder does not exist in directory, create the folder
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        # Move the files to the folders that were just created
        os.rename(filenames, "{}/{}".format(extension_to_category[extension], filenames))
        print()

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains files:", filenames)


main()

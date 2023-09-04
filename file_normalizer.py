# In this program we will normalize the file names in the given directory

import os
import re
import unicodedata


def normalize_filename(filename):
    # remove the extension and keep it in a variable
    extension = os.path.splitext(filename)[1]
    # remove the extension from the filename
    filename = os.path.splitext(filename)[0]
    # remove all the spaces and replace with underscore
    filename = filename.replace(" ", "_")
    # remove accent characters and replace with normal characters
    filename = unicodedata.normalize('NFKD', filename).encode(
        'ascii', 'ignore').decode('utf-8', 'ignore')
    # replace multiple underscores with single underscore and - by _
    filename = re.sub(r'[-_]+', '_', filename)
    # remove all the special characters excluding the . and _
    filename = re.sub(r'[^\w\.\_]', '', filename)
    #remove underscore from the start and end of the filename
    filename = filename.strip("_")
    # put all the characters in lower case
    filename = filename.lower()
    # add the extension to the filename
    filename = filename + extension
    return filename


def rename_files_in_directory(path):
    if not os.path.exists(path):
        print("folder doesn't exist")
        return
    for filename in os.listdir(path):
        # normalize the filename and raise an exception if the file already exist
        try:
            normalized_filename = normalize_filename(filename)
            if normalized_filename != filename:
                os.rename(os.path.join(path, filename),
                        os.path.join(path, normalized_filename))
                print(f"{filename} -> {normalized_filename}")
        except FileExistsError:
            # add a number to the filename if the file already exist
            i = 1
            while True:
                try:
                    # add the number before the extension
                    normalized_filename = re.sub(
                        r'(?<=\.)', f'_{i}', normalized_filename)
                    if normalized_filename != filename:
                        os.rename(os.path.join(path, filename),
                                os.path.join(path, normalized_filename))
                        print(f"{filename} -> {normalized_filename}")
                        break
                except FileExistsError:
                    i += 1
                    continue


def main():
    # ask for the path of the directory
    path = input("Enter the path of the directory: ")
    # normalize the file names in the directory
    rename_files_in_directory(path)
    # ask if the user want to leave or if he wants to normalize another directory
    while True:
        choice = input("Do you want to normalize another directory? (y/n): ")
        if choice == "y":
            path = input("Enter the path of the directory: ")
            rename_files_in_directory(path)
        elif choice == "n":
            print("Thank you for using the program")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

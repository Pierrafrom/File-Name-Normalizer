# File Name Normalizer

This Python program is designed to normalize file names in a given directory. It helps in standardizing file names by removing spaces, special characters, and accents, and converting them to lowercase. This can be useful when managing files to ensure consistency and compatibility across different systems.

## How it works

The program performs the following operations on each file in the specified directory:

1. **Remove file extension:** It separates the file extension from the filename.

2. **Remove spaces:** Spaces in the filename are replaced with underscores.

3. **Remove accent characters:** Accented characters are converted to their closest non-accented counterparts (e.g., é becomes e).

4. **Replace special characters:** Special characters (excluding periods and underscores) are removed from the filename.

5. **Consolidate underscores and hyphens:** Multiple consecutive underscores or hyphens are replaced with a single underscore.

6. **Trim underscores:** Underscores at the beginning and end of the filename are removed.

7. **Convert to lowercase:** The filename is converted to lowercase.

8. **Reattach file extension:** The file extension is reattached to the filename.

## Usage

1. **Clone the repository:** Clone this GitHub repository to your local machine.

2. **Navigate to the directory:** Open your terminal and navigate to the directory containing the script.

3. **Run the script:** Execute the script by running the following command:

   ```shell
   python normalize_filenames.py
   ```

4. **Enter the directory path:** You will be prompted to enter the path of the directory containing the files you want to normalize.

5. **Normalization:** The program will process each file in the directory, and you will see the original filenames and their normalized counterparts displayed in the terminal.

6. **Continue or exit:** After the normalization is complete, you can choose to normalize another directory by entering 'y' or exit the program by entering 'n'.

**Note:** If a file with a normalized name already exists in the directory, a numeric suffix will be added to the filename to avoid overwriting existing files.

## Example

Here's an example of how the program works:

```
Enter the path of the directory: /path/to/your/directory
File 1.txt -> file_1.txt
File-with-Special-Chars.txt -> file_with_special_chars.txt
Another File.txt -> another_file.txt
...
Do you want to normalize another directory? (y/n): y
Enter the path of the directory: /path/to/another/directory
...
Do you want to normalize another directory? (y/n): n
Thank you for using the program.
```

## Disclaimer

Please use this program with caution, and make sure to back up your files before running it on important directories. The program will modify file names, which could affect their accessibility and compatibility with other software.

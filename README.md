# Directory Structure to Markdown Script

This Python script generates a Markdown file that represents the directory structure of a specified folder. It can include the content of the files or just the structure, depending on the user's choice.

## Features

- Converts a directory structure to a Markdown file
- Option to include or exclude file contents
- Handles file reading errors gracefully
- Generates a summary of processed directories and files
- Allows custom naming of the output file
- Provides options to create files with content, without content, or both

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```
   python script_name.py
   ```

2. Follow the prompts:
   - Enter the path of the folder to process
   - Enter the name of the output Markdown file (or leave blank for auto-naming)
   - Choose the output option:
     1. Create file with content
     2. Create file without content (structure only)
     3. Create both versions

## Functions

### `normalize_path(path)`
Normalizes the given path by removing surrounding quotes and using `os.path.normpath`.

### `files_to_markdown(folder_path, output_file, include_content=True)`
Generates the Markdown file based on the directory structure.

### `generate_output_filename(folder_path, include_content, user_filename='')`
Generates an appropriate output filename based on user input and processing options.

## Output

The script generates one or two Markdown files (depending on the chosen option) in the same directory as the processed folder. The files include:

- A header with the name of the processed directory
- The date and time of generation
- A hierarchical representation of the directory structure
- File contents (if the option is selected)
- A summary of the total number of directories and files processed

## Error Handling

- The script checks if the specified folder exists
- It handles file reading errors and includes error messages in the output

## Note

This script may take a considerable amount of time to run for large directories, especially when including file contents.

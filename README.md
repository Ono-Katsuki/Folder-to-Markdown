# Folder to Markdown Converter

This Python script combines the contents of all files in a specified folder (including subfolders) into a single Markdown file.

## Features

- Recursively scans all files in the specified folder and its subfolders
- Creates a single Markdown file containing the contents of all scanned files
- Uses relative file paths as headers in the Markdown file
- Preserves Markdown formatting for .md files
- Wraps non-Markdown files in code blocks for better readability
- Adds separators between different files for improved organization

## Requirements

- Python 3.x
- markdown2 library (install with `pip install markdown2`)

## Usage

1. Run the script:
   ```
   python folder_to_markdown.py
   ```
2. When prompted, enter the path of the folder you want to process.
3. Enter the desired name for the output Markdown file.
4. The script will process all files and save the result in the specified output file.

## Example

```
Enter the path of the folder to process: /path/to/your/folder
Enter the name of the output Markdown file: combined_output.md
Processing complete. Results saved to combined_output.md.
```

## Notes

- This script is designed for text files. Processing folders with binary files may result in errors.
- Be cautious when processing folders with a large number of files or very large files, as it may consume significant memory.

## Customization

You can modify this script to suit your specific needs. Some potential modifications include:

- Filtering files based on extension
- Adding more sophisticated error handling
- Implementing file size limits
- Customizing the formatting of different file types

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/folder-to-markdown/issues) if you want to contribute.

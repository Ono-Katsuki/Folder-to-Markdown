import os
import datetime

def normalize_path(path):
    # Remove surrounding quotes if present
    path = path.strip('"\'')
    return os.path.normpath(path)

def files_to_markdown(folder_path, output_file, include_content=True):
    folder_path = normalize_path(folder_path)
    if not os.path.exists(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return

    with open(output_file, 'w', encoding='utf-8') as outfile:
        file_count = 0
        dir_count = 0
        outfile.write(f"# Directory Structure of {os.path.basename(folder_path)}\n\n")
        outfile.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for root, dirs, files in os.walk(folder_path):
            level = len(os.path.relpath(root, folder_path).split(os.sep))
            indent = ' ' * 4 * (level - 1)
            dir_name = os.path.basename(root)
            print(f"{indent}Processing directory: {dir_name} (depth: {level - 1})")
            dir_count += 1
            
            outfile.write(f"{'#' * (level + 1)} {dir_name}\n\n")
            
            subindent = ' ' * 4 * level
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                
                print(f"{subindent}Processing file: {file}")
                
                outfile.write(f"- {file}\n")
                
                if include_content:
                    outfile.write(f"\n```\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content)
                    except Exception as e:
                        error_message = f"Error reading file '{relative_path}': {str(e)}"
                        print(f"{subindent}Error: {error_message}")
                        outfile.write(f"Error: {error_message}\n")
                    outfile.write(f"\n```\n")
                
                file_count += 1
                print(f"{subindent}Successfully processed: {file}")
            
            outfile.write("\n")
            print(f"{indent}Finished processing directory: {dir_name}")
        
        outfile.write(f"\n## Summary\n")
        outfile.write(f"- Total directories processed: {dir_count}\n")
        outfile.write(f"- Total files processed: {file_count}\n")
        
        print(f"\nTotal directories processed: {dir_count}")
        print(f"Total files processed: {file_count}")

def generate_output_filename(folder_path, include_content, user_filename=''):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.basename(folder_path)
    content_indicator = "with_content" if include_content else "structure_only"
    
    if user_filename:
        name, ext = os.path.splitext(user_filename)
        output_file = f"{name}_{content_indicator}{ext}"
    else:
        output_file = f"{folder_name}_{content_indicator}_{timestamp}.md"
    
    return os.path.join(os.path.dirname(folder_path), output_file)

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to process: ").strip()
    folder_path = normalize_path(folder_path)
    
    output_file = input("Enter the name of the output Markdown file (leave blank for auto-naming): ").strip()
    
    print("\nChoose output option:")
    print("1. Create file with content")
    print("2. Create file without content (structure only)")
    print("3. Create both versions")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        output_file = generate_output_filename(folder_path, True, output_file)
        files_to_markdown(folder_path, output_file, True)
        print(f"\nProcessing complete. Results saved to {output_file}")
    elif choice == '2':
        output_file = generate_output_filename(folder_path, False, output_file)
        files_to_markdown(folder_path, output_file, False)
        print(f"\nProcessing complete. Results saved to {output_file}")
    elif choice == '3':
        output_file_with_content = generate_output_filename(folder_path, True, output_file)
        output_file_structure_only = generate_output_filename(folder_path, False, output_file)
        
        files_to_markdown(folder_path, output_file_with_content, True)
        files_to_markdown(folder_path, output_file_structure_only, False)
        
        print(f"\nProcessing complete.")
        print(f"File with content saved to: {output_file_with_content}")
        print(f"File without content saved to: {output_file_structure_only}")
    else:
        print("Invalid choice. Please run the script again and choose 1, 2, or 3.")

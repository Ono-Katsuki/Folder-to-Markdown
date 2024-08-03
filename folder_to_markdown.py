import os
import markdown2

def files_to_markdown(folder_path, output_file):
    if not os.path.exists(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return

    with open(output_file, 'w', encoding='utf-8') as outfile:
        file_count = 0
        dir_count = 0
        for root, dirs, files in os.walk(folder_path):
            level = root.replace(folder_path, '').count(os.sep)
            indent = ' ' * 4 * level
            dir_name = os.path.basename(root)
            print(f"{indent}Processing directory: {dir_name} (depth: {level})")
            dir_count += 1
            
            outfile.write(f"{'#' * (level + 1)} {dir_name}\n\n")
            
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                
                print(f"{subindent}Processing file: {file}")
                
                outfile.write(f"{'#' * (level + 2)} {file}\n\n")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                        if file.endswith('.md'):
                            outfile.write(content)
                        else:
                            outfile.write(f"```\n{content}\n```\n")
                        
                        file_count += 1
                        print(f"{subindent}Successfully processed: {file}")
                except Exception as e:
                    error_message = f"Error processing file '{relative_path}': {str(e)}"
                    print(f"{subindent}Error: {error_message}")
                    outfile.write(f"Error: {error_message}\n")
                
                outfile.write("\n---\n\n")
            
            print(f"{indent}Finished processing directory: {dir_name}")
        
        print(f"\nTotal directories processed: {dir_count}")
        print(f"Total files processed: {file_count}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to process: ").strip()
    output_file = input("Enter the name of the output Markdown file (leave blank for auto-naming): ").strip()
    
    if not output_file:
        # Auto-generate the output file name based on the input folder name
        folder_name = os.path.basename(os.path.normpath(folder_path))
        output_file = f"{folder_name}.md"
        print(f"Output file name auto-generated: {output_file}")
    
    # Ensure the output file has a .md extension
    if not output_file.lower().endswith('.md'):
        output_file += '.md'
    
    print(f"\nProcessing folder: {folder_path}")
    print(f"Output file: {output_file}\n")
    
    files_to_markdown(folder_path, output_file)
    print(f"\nProcessing complete. Results saved to {output_file}.")

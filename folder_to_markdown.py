import os
import markdown2

def files_to_markdown(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                
                outfile.write(f"# {relative_path}\n\n")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                        # Write Markdown files as-is, others as code blocks
                        if file.endswith('.md'):
                            outfile.write(content)
                        else:
                            outfile.write(f"```\n{content}\n```\n")
                except Exception as e:
                    outfile.write(f"Error: Failed to read file - {str(e)}\n")
                
                outfile.write("\n---\n\n")  # Separator between files

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to process: ")
    output_file = input("Enter the name of the output Markdown file: ")
    
    files_to_markdown(folder_path, output_file)
    print(f"Processing complete. Results saved to {output_file}.")

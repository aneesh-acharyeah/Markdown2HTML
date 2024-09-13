import markdown
import os


def convert_markdown_to_html(md_file_path, html_file_path):
    # Validate file paths
    if not os.path.exists(md_file_path) or not os.path.isfile(md_file_path):
        print(f"Error: The file '{md_file_path}' does not exist or is not a valid file.")
        return

    if not md_file_path.endswith('.md'):
        print("Error: Please provide a valid Markdown file with the extension '.md'.")
        return

    if not html_file_path.endswith('.html'):
        print("Warning: Output file does not have an '.html' extension. Adding '.html'.")
        html_file_path += '.html'

    if os.path.exists(html_file_path):
        overwrite = input(f"The file '{html_file_path}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation cancelled.")
            return

    try:
        # Read the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        if not markdown_content.strip():
            print("Error: The Markdown file is empty.")
            return

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Add basic CSS styling
        style = """
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #2c3e50;
            }
            p {
                color: #34495e;
            }
        </style>
        """
        html_content = style + html_content

        # Write the HTML content to an output file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Markdown successfully converted to HTML and saved as '{html_file_path}'")

    except UnicodeDecodeError:
        print(f"Error: Could not decode file '{md_file_path}'. Ensure it is encoded as UTF-8.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input Markdown file and output HTML file paths
    md_file = input("Enter the Markdown file path: ")
    html_file = input("Enter the output HTML file path: ")

    # Convert the file
    convert_markdown_to_html(md_file, html_file)

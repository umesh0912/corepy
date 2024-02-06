

import os
import platform


def create_symlink_old(current_file_path, archive_directory, symlink_name):
    symlink_path = os.path.join(archive_directory, symlink_name)

    try:
        if platform.system() == 'Windows':
            # On Windows, use the os.symlink function
            os.symlink(current_file_path, symlink_path)
        elif platform.system() == 'Linux':
            # On Linux, use the os.symlink function
            os.symlink(current_file_path, symlink_path)
        else:
            print(f"Unsupported operating system: {platform.system()}")
            return

        print(f"Symbolic link '{symlink_name}' created successfully.")
    except OSError as e:
        print(f"Error creating symbolic link: {e}")

def create_symlink(output_file: str, symlink_file_path: str) -> None:
    try:
        if os.path.islink(symlink_file_path):
            os.remove(symlink_file_path)
            os.symlink(output_file, symlink_file_path)
    except Exception:
        print("got error")



def generate_txt_file(filename, content):
  """Generates a text file with the given filename and content.

  Args:
    filename: The name of the text file to generate.
    content: The content of the text file.
  """

  with open(filename, "w") as f:
    f.write(content)

# Example usage:

def main():
    print("hi")
    # Get the absolute path to the current file
    current_file_path = os.path.abspath(__file__)
    current_dir = os.getcwd()

    generate_txt_file("myfile.txt", "This is the content of my text file.")

    file_path = os.path.join(os.getcwd(), "myfile.txt")
    log_dir_path = os.path.join(current_dir, "log")
    os.makedirs(log_dir_path, exist_ok=True)
    log_archive_path = os.path.join(log_dir_path, "archive")
    os.makedirs(log_archive_path, exist_ok=True)
    symlink_path = os.path.join(log_dir_path, "mytext.log")

    create_symlink(file_path, symlink_path)

    # Specify the path to the archive directory and the desired symlink name
    archive_directory = 'archive'
    symlink_name = 'symlink_name_1'
    #Get-Item
    #Get-Item -LiteralPath "D:\python\corepy\src\symlink_demo\archive\symlink_name" | Format-List


    # Call the function to create the symbolic link
    #create_symlink_old(current_file_path, archive_directory, symlink_name)





if __name__ == "__main__":
    main()
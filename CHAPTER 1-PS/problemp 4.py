import os

def print_directory_contents(directory_path):
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory_path)
        
        # Print each entry
        for entry in entries:
            print(entry)
    
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path of the directory
directory_path = '.'  # Use '.' for the current directory or specify another directory path

print_directory_contents(directory_path)

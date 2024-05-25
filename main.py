import tempfile
import os

# Maintain a list to track temporary directories
temp_dirs = []

# Flag to control cleanup behavior
cleanup_enabled = True

# Get the current working directory
cwd = os.getcwd()

# Create temporary directories with custom prefixes and add them to the list
for i in range(3):
    prefix = f'temp_prefix_{i}_'
    # Pass cleanup_enabled to delete parameter
    temp_dir = tempfile.TemporaryDirectory(prefix=prefix, dir=cwd, delete=cleanup_enabled)
    temp_dirs.append(temp_dir)
    print("Temporary directory created:", temp_dir.name)
    
    # Perform operations within the temporary directory
    with open(os.path.join(temp_dir.name, 'example.txt'), 'w') as file:
        file.write("Hello, Temporary World!")

# Temporary directories and their contents are automatically cleaned up if cleanup_enabled is True
print("Temporary directories no longer exist:", not any(os.path.exists(temp_dir.name) for temp_dir in temp_dirs))

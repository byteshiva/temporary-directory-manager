import tempfile
import os

# Maintain a list to track temporary directories
temp_dirs = []

# Flag to control cleanup behavior
cleanup_enabled = False

# Get the current working directory
cwd = os.getcwd()


OverRideCleanUP = True

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

# Check if temporary directories exist based on the value of cleanup_enabled
temp_dirs_exist = any(os.path.exists(temp_dir.name) for temp_dir in temp_dirs) if cleanup_enabled else all(os.path.exists(temp_dir.name) for temp_dir in temp_dirs)

# Function to handle cleanup based on cleanup_enabled
def handle_cleanup():
    if cleanup_enabled:
        temp_dirs_exist = any(os.path.exists(temp_dir.name) for temp_dir in temp_dirs)
        # Print the appropriate message based on temp_dirs_exist
        print("Temporary directories no longer exist:" if cleanup_enabled else "Temporary directories still exist")
    else:
        print("Explicit cleanup performed.")
        for temp_dir in temp_dirs:
            temp_dir.cleanup()

# Override cleanup behavior if OverRideCleanUP is True
if 'OverRideCleanUP' in globals() and OverRideCleanUP:
    cleanup_enabled = False
    # Call the cleanup function again after potentially overriding cleanup behavior
    handle_cleanup()

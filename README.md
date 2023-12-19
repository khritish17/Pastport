# Pastport Initialization Module
The **'prt_init'** class is part of the Pastport system, which provides a mechanism for tracking changes to files within a specified directory. The primary purpose of this class is to initialize Pastport within a given location and set up the necessary files and directories for tracking.

## File: prt_init.py | Class: prt_init
### Constructor
```
def __init__(self, location: str = "") -> None:
```
### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport should be initialized. If not provided, the current working directory will be used.

### Description
- Initializes Pastport within the specified location.
- Obtains the absolute path of the provided location.
- Extracts the directory name from the path.
- Scans the files and subdirectories in the specified location, tracking only files.
- Creates the "prt" directory within the location for Pastport tracking.
- Creates a tracking file named **'{directory_name.lower()}.track'** within the "prt" directory.
#### Example
```
import prt_init

# Initialize Pastport in a specified location
init = prt_init(location=r'D:\Codes\Projects\Pastport\test_folder')
```
### Method: 'create_tracking_file'
```
def create_tracking_file(self) -> None:
```
### Description
- Creates a tracking file within the "prt" directory.
- The tracking file contains information about the files in the directory, with each line representing a file and its tracking status.

#### Example
```
init.create_tracking_file()
```
### Notes
- The Pastport system is designed to track changes to files within the specified directory.
- If Pastport initialization has already been completed in the provided location, a message will be displayed to notify the user.

Note: Ensure that the terminal_output and os modules are properly imported before using the prt_init class.

# Pastport Initialization Module
The **prt_init class** in the **terminal_output** module facilitates the initialization of the Pastport version control system within a specified directory. Pastport is designed to manage file versions using commit files and tracking files. This class creates the necessary directory structure, including the Pastport directory and the tracking file, and initializes the version control system for the provided location.

## Class: prt_init
## Constructor
```
def __init__(self, location="") -> None:
    pass
```
Parameters
- **location** (str): The absolute path to the directory where Pastport is to be initialized. If not provided, the current working directory is used.
## Methods
**__init__(self, location="") -> None**
- Initializes the prt_init object.
- Sets the absolute path to the specified location.
- Identifies the directory name.
- Scans files and subdirectories in the specified location.
- Creates the Pastport directory (**prt**).
- Creates the tracking file within the Pastport directory.

**create_tracking_file(self)**
- Creates the tracking file within the Pastport directory.
- Initializes the tracking file with commit number 0 and a list of files in the directory.

### Example
```
from terminal_output import prt_init

# Example usage:
init_instance = prt_init(location=r'D:\Codes\Projects\Pastport\test_folder')
```
## Dependencies
- This module depends on the terminal_output module, assumed to be available in the same directory or accessible through the Python path.

## Error Handling
- If Pastport has already been initialized in the specified directory, a message is printed to the terminal using the **output** function from the **terminal_output** module.
- If an error occurs during directory creation or file writing, an exception is raised.

## Notes
- The module assumes that Pastport will manage files within the specified directory.
- The Pastport directory structure includes a **prt** directory for Pastport-specific files.
- The tracking file (**track**) is used to keep track of files and their versions.
- Commit numbers start from **0** for the initial commit.
- The **create_tracking_file** method initializes the tracking file with the initial commit number (**0**) and a list of files in the directory.
Caution: Ensure that Pastport has not been initialized in the specified directory before running this module, as it can lead to unintended consequences. Use this module only in a clean environment or after ensuring that no Pastport-related files exist in the specified directory.

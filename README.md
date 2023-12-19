# Pastport Initialization Module
The **prt_init class** in the **terminal_output** module facilitates the initialization of the Pastport version control system within a specified directory. Pastport is designed to manage file versions using commit files and tracking files. This class creates the necessary directory structure, including the Pastport directory and the tracking file, and initializes the version control system for the provided location.

## File: prt_init.py
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

**Caution**: Ensure that Pastport has not been initialized in the specified directory before running this module, as it can lead to unintended consequences. Use this module only in a clean environment or after ensuring that no Pastport-related files exist in the specified directory.

# Pastport Commit Module
The **prt_commit** class in the **diff_algorithm**, **file_translator**, and **reconstructor** modules provides functionality for creating commits in the Pastport version control system. This module automates the process of generating commit data, handling both regular commits for tracked files and cold commits for untracked files.

## File: prt_commit.py
## Class: prt_commit
Constructor
```
def __init__(self, location="", message="Untitled Commit") -> None:
    pass
```
Parameters
- **location** (str): The absolute path to the directory where Pastport is initialized. If not provided, the current working directory is used.
- **message** (str): The commit message associated with the commit. Default is "Untitled Commit."
## Methods
**__init__(self, location="", message="Untitled Commit") -> None**
- Initializes the prt_commit object.
- Sets the absolute path to the specified location.
- Identifies the directory name.
- Checks if Pastport has been initialized in the specified directory.
- Reads the tracking file to identify the latest commit number and tracked files.
- Performs a cold start commit if Pastport has not been previously initialized.
- Performs normal commits for tracked files and cold commits for untracked files if Pastport has been initialized.

**commit(self, file, commit_number)**
- Creates a commit for a tracked file.
- Generates the old file, sends it to the diff algorithm along with the new file, and obtains commit data.
- Writes the commit data to the commit file.

**cold_commit(self, file, commit_number)**
- Creates a cold start commit for an untracked file.
- Generates the old file, sends it to the diff algorithm along with the new file, and obtains commit data.
- Writes the commit data to the commit file.

### Example
```
from diff_algorithm import diff_algorithm
from file_translator import prt_commit

# Example usage:
commit_instance = prt_commit(location=r'D:\Codes\Projects\Pastport\test_folder', message="Initial Commit")
```
## Dependencies
- This module depends on the **diff_algorithm**, **file_translator**, and **reconstructor** modules, assumed to be available in the same directory or accessible through the Python path.

## Error Handling
If Pastport has not been initialized in the specified directory, the program exits with a message indicating that Pastport has not been initialized.

## Notes
- The module assumes that Pastport has been initialized in the specified directory and follows the Pastport directory structure.
- Cold start commits are initiated when Pastport has not been previously initialized or if there are no tracked files.
- Regular commits are performed for tracked files.
- Cold commits are performed for untracked files.
- The commit message is associated with each commit and is stored in the commit log file (**log**).
- Commit data is generated using the diff algorithm and stored in commit files (**commit**).
- The current commit number is updated in the **.curcommit** file.
- Cold commits are considered as initial commits, and their commit messages are set to "Initial commit."

**Caution**: Ensure that Pastport has been initialized before using this module, and use it with caution as it involves file manipulation and potential overwriting of commit data. Use this module in conjunction with the Pastport initialization module for a complete version control workflow.

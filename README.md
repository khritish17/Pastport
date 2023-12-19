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

> &#x26A0; Ensure that the terminal_output and os modules are properly imported before using the prt_init class.



# Pastport Commit Module
The **'prt_commit'** class is a crucial component of the Pastport system, responsible for creating commits within a specified location. It utilizes a diff algorithm to generate commit data and reconstructs old files for comparison. This documentation provides an overview of the **'prt_commit'** class and its methods.

## File: prt_commit.py | Class: prt_commit
### Constructor
```
def __init__(self, location: str = "", message: str = "Untitled Commit") -> None:
```
### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport commits should be created. If not provided, the current working directory will be used.
- **'message'** (str, optional): A custom commit message. If not provided, the default message is "Untitled Commit."

### Description
- Initializes the prt_commit class with the specified location and commit message.
- Reads the tracking file to determine the current state of tracked files.
- Performs a cold start commit if Pastport has not been initialized.
- Initiates either a normal commit or a cold commit based on the tracking information.
- Updates the tracking file, current commit number, and commit log.
#### Example
```
from pastport import prt_commit

# Create a Pastport commit in a specified location with a custom message
cmt = prt_commit(location=r'D:\Codes\Projects\Pastport\test_folder', message="Initial Commit")
```
### Method: 'commit'
```
def commit(self, file: str, commit_number: int) -> None:
```
### Parameters
- **'file'** (str): The name of the file to be committed.
- **'commit_number'** (int): The commit number for the current commit.

### Description
- Generates the old file from the initial commit data.
- Uses the diff algorithm to compare the old file with the new file and obtain commit data.
- Writes the commit data to the commit file.

#### Example
```
cmt.commit(file="example.txt", commit_number=1)
```
### Method: cold_commit
```
def cold_commit(self, file: str, commit_number: int) -> None:
```
### Parameters
- **'file'** (str): The name of the file for the cold commit.
- **'commit_number'** (int): The commit number for the current commit.

### Description
- Creates a cold commit for untracked files.
- Uses the diff algorithm to generate commit data for the initial commit.
- Writes the commit data to the commit file.

### Example
```
cmt.cold_commit(file="new_file.txt", commit_number=1)
```
### Notes
- The **'prt_commit'** class is responsible for managing the commit process within the Pastport system.
- Cold start commits are initiated when Pastport is initialized or when new files are detected.
- Normal commits are performed for tracked files based on the tracking information from the previous commit.
- Commit data is stored in commit files within the "prt" directory.

> &#x26A0; Ensure that the required modules (os, diff_algorithm, file_translator, and reconstructor) are properly imported before using the prt_commit class.



# Pastport Checkout Module
The **'prt_checkout'** class is a critical component of the Pastport system, allowing users to retrieve and apply the changes from a specific commit. This documentation provides an overview of the **'prt_checkout'** class and its methods.

## File: pt_checkout.py | Class: prt_checkout
### Constructor
```
def __init__(self, commit_number: int, location: str = "") -> None:
```
### Parameters
- **'commit_number'** (int): The commit number to checkout.
- **'location'** (str, optional): The absolute path to the directory where Pastport is initialized. If not provided, the current working directory will be used.

### Description
- Initializes the **'prt_checkout'** class with the specified commit number and location.
- Validates Pastport initialization and retrieves the directory name.
- Reads the tracking file to determine the files associated with the specified commit.
- Reconstructs and replaces the files according to the commit number and commit data.
- Updates the current commit number in the .curcommit file.
#### Example
```
from pastport import prt_checkout

# Checkout commit number 3 in a specified location
CO = prt_checkout(commit_number=3, location=r'D:\Codes\Projects\Pastport\test_folder')
```

### Notes
- The **'prt_checkout'** class facilitates the retrieval and application of changes from a specific commit within the Pastport system.
- Files associated with the specified commit are reconstructed and replaced.
- Uncommitted files are removed from the directory.

> &#x26A0; Ensure that the required modules (os, file_translator, and reconstructor) are properly imported before using the prt_checkout class.

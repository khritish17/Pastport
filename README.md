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








# Pastport Status Module
The **'prt_status'** class provides a mechanism for determining the status of files within a Pastport-enabled directory. It categorizes files into modified, untracked, and deleted based on the differences between the current state and the last committed state.

## File: prt_status.py | Class: prt_status
### Constructor
```
def __init__(self, location: str = "") -> None:
```
### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport is initialized. If not provided, the current working directory will be used.

### Description
- Initializes the prt_status class with the specified location.
- Retrieves the directory name and the last commit number.
- Reads the tracking file to obtain the list of tracked files.
- Lists the current files in the directory.
- Calls methods to check for modified, untracked, and deleted files.
#### Example
```
from pastport import prt_status

# Check the status of files in a specified location
st = prt_status(location=r'D:\Codes\Projects\Pastport\test_folder')
modified, untracked, deleted = st.get_status()
print("Modified: {}".format(modified))
print("Untracked: {}".format(untracked))
print("Deleted: {}".format(deleted))
```
### Method: check_modified
```
def check_modified(self, last_commit_number: int) -> None:
```
### Parameters
- **'last_commit_number'** (int): The last commit number to use as a reference.

### Description
- Reconstructs common files based on the last commit number.
- Compares the reconstructed files with the current files to identify modifications.
- Appends modified files to the modified list.

### Method: check_untracked
```
def check_untracked(self) -> None:
```
### Description
- Identifies untracked files by comparing the current files with tracked files.
- Appends untracked files to the untracked list.
### Method: check_deleted
```
def check_deleted(self) -> None:
```
### Description
- Identifies deleted files by comparing tracked files with current files.
- Appends deleted files to the deleted list.
- Appends common files to the common_files list.
### Method: get_status
```
def get_status(self) -> Tuple[List[str], List[str], List[str]]:
```
### Returns
- **'Tuple[List[str], List[str], List[str]]'**: A tuple containing lists of modified, untracked, and deleted files.
### Description
- Returns the lists of modified, untracked, and deleted files.
### Notes
- The **'prt_status'** class is designed to provide a snapshot of file status within a Pastport-enabled directory.
- The status is determined based on the differences between the current state and the last committed state.

> &#x26A0; Ensure that the required modules (**'os'**, **'file_translator'**, and **'reconstructor'**) are properly imported before using the prt_status class.

# INTRODUCTION
The Pastport system represents a basic iteration of a **Version Control System (VCS)**, designed to comprehend the fundamental principles of VCS operation. It aims to illustrate how data structures, algorithms, and general programming enable the development of valuable applications.

The nomenclature **"Pastport"** is indicative of the system's visualization in terms of nodes and edges, where each commit in the process represents a node. Nodes are sometimes referred to as **"ports"** and in the context of a VCS, revisiting old commits inspired the name "Pastport."

# Commit Node Structure
The Pastport VCS system follows a **linear-direct sequential** structure, as depicted in the accompanying diagram. 

Each node in the diagram signifies a commit made, preserving essential data. This data enables the regeneration of files committed at that specific point in time. The initial commit, designated as **'Commit 0'** saves entire files in their original state. Subsequent commits, starting from **'Commit 1'** and onwards, are built upon the foundation of "Commit 0."
The commit node structure, illustrated in the aforementioned image, comprises four commits: **'Commit 0'**, **'Commit 1'**, **'Commit 2'**, and **'Commit 3'**. Commit 0 holds particular significance as the starting point, storing complete files precisely as they were during the initial commit. Reverting back to a prior commit, such as Commit 1 from Commit 3, involves retracing the steps back to Commit 0. From there, files are regenerated using the data from Commit 1.

The structure of the commit node system is delineated as follows (please refer to the image above): there are four commits denoted as commit 0, commit 1, commit 2, and commit 3. Commit 0 holds a distinct status as the initial point, preserving complete files in their original form (the method of data storage will be elaborated upon as we progress). Subsequent commits are all derived from commit 0.

> Consider the scenario where the system is presently at commit 3, and there is a desire to revert back to commit 1. To achieve this, one simply needs to return to commit 0, where the original data from the initial commit is stored. From this point, the files can be regenerated utilizing the data from commit 1.

# Commit Data Structure
The critical question arises: what information should each node store? Specifically, what constitutes the contents of commit data? 
## Example: OT(Old Text) and NT(New Text) Transformation
This can be elucidated through an example involving **old text (OT)** and **new text (NT)** transformation. 
Let's say
<div align="center">
    
**OT**: "Hello I am Khritish,"\
**NT**: "Hello I Romen" 
</div>

The transformation involves deleting ["am", "Khritish"] from OT and inserting ["Romen"] 
The common part, "Hello I," remains untouched.

To extract deletion and insertion information, a straightforward approach is employed. 
Firstly, identify the common part ("Hello, I"). 
Anything in OT remaining after removing the common part necessitates deletion, as it does not exist in NT. 
Conversely, anything in NT after removing the common part requires insertion. 

For the provided example:\
**Common part**: "Hello, I"\
**Deletion**: OT - common part = "am," "Khritish"\
**Insertion**: NT - common part = "Romen"
<div align="center">
    
**New Text = (Old Text - deletions) + insertions**
</div>

Consequently, within each commit, the data stored in a node comprises the necessary insertion and deletion information. These details delineate the modifications required on commit 0 to generate the new text.

# Longest Common Subsequences (LCS)
Indeed, it is evident that identifying the common elements between two texts is crucial. To achieve this, we employ a ‘difference algorithm’, specifically the **Longest Common Subsequence (LCS)** algorithm. LCS determines the length of the longest sequence shared by both texts. This method employs Dynamic Programming and backtracking. A slight modification involves utilizing sequences of words instead of individual letters.

Allow me to illustrate this process using an example:

Consider the following texts:
<div align="center">
    
**Old Text (OT)**: "How are you doing"\
**New Text (NT)**: "How you doin’"
</div>

### Step 1: Tokenize the sentences
<div align="center">

**Tokenized Old Text (TOT)**: ["How", "are", "you", "doing"]\
**Tokenized New Text (TNT)**: ["How", "you", "doin’"]
</div>

### Step 2: Set up the DP matrix
Create a DP matrix of size **len(TOT) + 2  ✕  len(TNT) + 2**, filling it with **0**'s, where TOT represents Tokenized Old Text and TNT represents Tokenized New Text.
|       | Ø  | How | you | doin |
|-------|----|-----|-----|------|
| Ø     | 0  | 0   | 0   | 0    |
| How   | 0  | 0   | 0   | 0    |
| are   | 0  | 0   | 0   | 0    |
| you   | 0  | 0   | 0   | 0    |
| doing | 0  | 0   | 0   | 0    |

### Step 3: Populate the DP matrix using the algorithm below
```
For i : 1 to length(TOT) - 1 (Inclusive range)
    For j : 1 to length(TNT) - 1 (Inclusive range)
        If TOT[i] == TNT[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        Else:
	        DP[i][j] = max(DP[i][j-1], DP[i-1][j])
```
This algorithm sets up the DP matrix to extract the longest common subsequence.
|       | Ø  | How | you | doin |
|-------|----|-----|-----|------|
| Ø     | 0  | 0   | 0   | 0    |
| How   | 0  | 1   | 1   | 1    |
| are   | 0  | 1   | 1   | 1    |
| you   | 0  | 1   | 2   | 2    |
| doing | 0  | 1   | 2   | 2    |


### Step 4: Backtrack the DP matrix to obtain the longest common words using the following algorithm
```
Initialize an empty list LCS  = []
i = length(DP) - 1, j = length(DP[0]) - 1
While i != 0 and j != 0:
	If TOT[i] == TNT[j]:
		LCS = [TOT[i], i, j] + LCS
	Else : 
		If DP[i][j - 1] >= DP[i - 1][j]:
			j = j - 1
		Else if DP[i][j - 1] < DP[i - 1][j]:
			i = i – 1
```
In the resulting LCS list, each element is a tuple containing the common word, the index corresponding to the old text (index_old), and the index corresponding to the new text (index_new).
<div align="center">
    
**LCS = [common word, old_index, new_index]**
</div>

**Old_index**: Refers to the index of the word in the Tokenized Old Text (TOT), indicating its position within the original text.

**New_index**: Denotes the index of the word in the Tokenized New Text (TNT), representing its location within the modified or new text.


> Note\
If **TNT** is empty, new_index is set to “None”.\
If **TOT** is empty, old_index is set to “None”.



# Generating the Commit Data
Using the Longest Common Subsequences (LCS) method, the process involves identifying common words and determining **insertions** and **deletions**, incorporating index values for precision. Allow me to elucidate this process with an example:

Let's consider:
<div align="center">
    
**TOT** = ["Hello", "I", "am", "Khritish"]\
**TNT** = ["Hello", "I", "Romen"]
</div>

### Step 1: Generate the Longest Common Subsequence, LCS
<div align="center">
    
**LCS** = [("Hello", 0, 0), ("I", 1, 1)]
</div>
Here, the LCS tuple ("Hello", 0, 0) signifies that the common word "Hello" appears at index 0 in both TOT and TNT.
("Hello", Index in TNT, Index in TOT)

### Step 2: Obtain the Deletion Data
<div align="center">
 
**Deletion** = TOT - LCS\
**Deletion** = ["Hello", "I", "am", "Khritish"] - [("Hello", 0, 0), ("I", 1, 1)]\
**Deletion** = [("am", 2), ("Khritish", 3)]
</div>
In the deletion data, each tuple contains the word to be deleted and its corresponding index in TOT.

### Step 3: Extract the Insertion Data
<div align="center">
 
**Insertion** = TNT - LCS\
**Insertion** = ["Hello", "I", "Romen"] - [("Hello", 0, 0), ("I", 1, 1)]\
**Insertion** = [("Romen", 2)]
</div>

Similarly, in the insertion data, each tuple contains the word to be inserted and its corresponding index in TNT.

Commit Data Format:
The final data stored in each commit is represented as a hashmap, where the key denotes the line number, and the corresponding value is a tuple containing insertion and deletion data.

<div align="center">
 
**Commit Data** = {Line number: (Insertion, Deletion)}
</div>

>Where:\
Insertion = [(word to be inserted, corresponding index in TNT)]\
Deletion = [(word to be deleted, corresponding index in TOT)]

This structured approach ensures precise recording of insertion and deletion operations, facilitating accurate reconstruction of texts during version control operations.




# Reconstruction Mechanism

The reconstruction process involves building files for a specified commit using the initial or 0th commit, leveraging commit data. As previously outlined, commit data encapsulates structured information facilitating the transformation of an old text file into a new text file.

To illustrate, consider the task of constructing a file, say "new.txt," from commit 3. This can be accomplished by using the initial version of "new.txt" (old.txt) found in commit 0, along with the commit data stored in commit 3. Each line in "old.txt" is converted to its corresponding line in "new.txt."

Here is a step-by-step breakdown of the reconstruction process:

- Create an empty list/array of length L, where L is given by the formula
> L = length( old_line ) + Li − Ld\
Li = length ( insertion_array_in_commit_data)\
Ld=length(deletion_array_in_commit_data)
This list represents the corresponding lines in "new.txt."
- Since the newly generated list mirrors the lines in the new file, insert the insertion word at the new file index (available in the commit data) to avoid word collisions.
- Delete the word from the old file line based on the deletion word (available in the commit data) at the old file index.
- After deletion, insert the remaining words from the old line in a first-come-first-serve basis at the empty places in the generated list. This completes the generation of the final new line.

**For example:**

**Old line**: "Words are good but not bad"\
**New line**: "Words will be good sword"

**OLD (Tokenized)**: ["Words", "are", "good", "but", "not", "bad"]\
**NEW (Tokenized)**: ["Words", "will", "be", "good", "sword"]


Corresponding commit data for the conversion from OLD to NEW:
<div align="center">
 
**Commit data**: ( [(will, 1), (be, 2), (sword, 4)], [(are, 1), (but, 3), (not, 4), (bad, 5)] )
</div>
Here,

Insertion array: [(will, 1), (be, 2), (sword, 4)]\
> Li = length(Insertion array) = 3

Deletion array: [(are, 1), (but, 3), (not, 4), (bad, 5)]\
> Ld = length(Deletion array) = 4

L = length(OLD) + Li − Ld = 6+3−4=5

### Step 1: Empty list of length L, ARR
<div align="center">
 
ARR = [ Ø , Ø , Ø, Ø, Ø]
</div>
> (Ø represents an empty place)

### Step 2: Insert the word into ARR
<div align="center">
 
ARR = [Ø , will, be, Ø, sword]
</div>

### Step 3: Deletion of words from OLD
<div align="center">
 
OLD = ["Words", "are", "good", "but", "not", "bad"]\
OLD = ["Words", "good"]
</div>

### Step 4: Insert the leftover words in OLD in a first-come-first-insert basis into the empty slots of ARR
<div align="center">
 
ARR = ["Words", "will", "be", "good", "sword"]
</div>
This reconstruction process successfully transforms the new line from the old line with the aid of commit data.










# Pastport Initialization Module
The **'prt_init'** class is part of the Pastport system, which provides a mechanism for tracking changes to files within a specified directory. The primary purpose of this class is to initialize Pastport within a given location and set up the necessary files and directories for tracking.

## File: prt_init.py | Class: prt_init
### Constructor
```
def __init__(self, location: str = "") -> None:
```
#### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport should be initialized. If not provided, the current working directory will be used.

#### Description
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
#### Description
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
#### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport commits should be created. If not provided, the current working directory will be used.
- **'message'** (str, optional): A custom commit message. If not provided, the default message is "Untitled Commit."

#### Description
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
#### Parameters
- **'file'** (str): The name of the file to be committed.
- **'commit_number'** (int): The commit number for the current commit.

#### Description
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
#### Parameters
- **'file'** (str): The name of the file for the cold commit.
- **'commit_number'** (int): The commit number for the current commit.

#### Description
- Creates a cold commit for untracked files.
- Uses the diff algorithm to generate commit data for the initial commit.
- Writes the commit data to the commit file.

#### Example
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
#### Parameters
- **'commit_number'** (int): The commit number to checkout.
- **'location'** (str, optional): The absolute path to the directory where Pastport is initialized. If not provided, the current working directory will be used.

#### Description
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
#### Parameters
- **'location'** (str, optional): The absolute path to the directory where Pastport is initialized. If not provided, the current working directory will be used.

#### Description
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
#### Parameters
- **'last_commit_number'** (int): The last commit number to use as a reference.

#### Description
- Reconstructs common files based on the last commit number.
- Compares the reconstructed files with the current files to identify modifications.
- Appends modified files to the modified list.

### Method: check_untracked
```
def check_untracked(self) -> None:
```
#### Description
- Identifies untracked files by comparing the current files with tracked files.
- Appends untracked files to the untracked list.
### Method: check_deleted
```
def check_deleted(self) -> None:
```
#### Description
- Identifies deleted files by comparing tracked files with current files.
- Appends deleted files to the deleted list.
- Appends common files to the common_files list.
### Method: get_status
```
def get_status(self) -> Tuple[List[str], List[str], List[str]]:
```
#### Returns
- **'Tuple[List[str], List[str], List[str]]'**: A tuple containing lists of modified, untracked, and deleted files.
#### Description
- Returns the lists of modified, untracked, and deleted files.
### Notes
- The **'prt_status'** class is designed to provide a snapshot of file status within a Pastport-enabled directory.
- The status is determined based on the differences between the current state and the last committed state.

> &#x26A0; Ensure that the required modules (**'os'**, **'file_translator'**, and **'reconstructor'**) are properly imported before using the prt_status class.










# Diff Algorithm Module (Longest Common Subsequence)
The **'diff_algorithm'** module provides functions for comparing two text files and generating commit data based on the differences between them.

# File: diff_algorithm.py
### Function: generate_commit_data
```
def generate_commit_data(old_text: List[str], new_text: List[str], lcs: List[Tuple[str, int, int]]) -> Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]:
```
#### Parameters
- **'old_text'** (List[str]): List of words from the old text.
- **'new_text'** (List[str]): List of words from the new text.
- **'lcs'** (List[Tuple[str, int, int]]): List of tuples representing the Longest Common Subsequence.
#### Returns
- **'Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]'**: A tuple containing lists of insertions and deletions.
#### Description
- Generates commit data based on the Longest Common Subsequence (LCS) of the old and new texts.
- Returns a tuple containing lists of insertions and deletions.
### Function: backtracking
```
def backtracking(old_text: List[str], new_text: List[str], dp: List[List[int]]) -> Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]:
```
#### Parameters
- **'old_text'** (List[str]): List of words from the old text.
- **'new_text'** (List[str]): List of words from the new text.
- **'dp'** (List[List[int]]): Dynamic Programming table.

#### Returns
- **'Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]'**: A tuple containing lists of insertions and deletions.

#### Description
- Implements backtracking to determine the Longest Common Subsequence (LCS) of the old and new texts.
- Calls generate_commit_data to generate commit data based on the LCS.
- Returns a tuple containing lists of insertions and deletions.
### Function: longest_common_subsequence
```
def longest_common_subsequence(old_text: str, new_text: str) -> Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]:
```
#### Parameters
- **'old_text'** (str): A line from the old text.
- **'new_text'** (str): A line from the new text.
#### Returns
- **'Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]'**: A tuple containing lists of insertions and deletions.

#### Description
- Converts the input lines into lists of words.
- Uses Dynamic Programming to find the Longest Common Subsequence (LCS).
- Calls backtracking to generate commit data based on the LCS.
- Returns a tuple containing lists of insertions and deletions.
### Function: diff_algorithm
```
def diff_algorithm(old_file: str, new_file: str) -> Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]:
```
#### Parameters
- **'old_file'** (str): The path to the old text file.
- **'new_file'** (str): The path to the new text file.
#### Returns
- **'Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]'**: A dictionary where keys are line numbers and values are tuples containing lists of insertions and deletions.
#### Description
- Reads the content of the old and new text files.
- Calls longest_common_subsequence to generate commit data for each line.
- Returns a dictionary where keys are line numbers, and values are tuples containing lists of insertions and deletions.
#### Example
```
from diff_algorithm import diff_algorithm

# Compare two text files and generate commit data
commit_data = diff_algorithm('file_old.txt', 'file_new.txt')
print(commit_data)
```
### Notes
- The **'diff_algorithm'** module is designed to find the differences between two text files and generate commit data.
- The commit data includes information about insertions and deletions for each line.
- The algorithm uses Dynamic Programming and Longest Common Subsequence (LCS) to identify changes.






# Commit Data I/O Module
The **'write_commit'** and **'read_commit'** functions provide mechanisms for writing and reading commit data to and from a file in Pastport.

# File: file_translator.py
### Function: write_commit
```
def write_commit(commit_data_file_location: str, commit_data: Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]], commit_number: int, commit_message: str) -> None:
```
#### Parameters
- **'commit_data_file_location'** (str): The path to the commit data file.
- **'commit_data'** (Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]): A dictionary containing commit data, where keys are line numbers, and values are tuples containing lists of insertions and deletions.
- **'commit_number'** (int): The commit number associated with the commit data.
- **'commit_message'** (str): The commit message.
#### Description
- Appends commit data to the specified commit data file.
- Uses a pilcrow symbol (**'\u00b6'**) as a delimiter.
- The commit data includes information about line numbers, insertions, deletions, and the commit message.
### Function: read_commit
```
def read_commit(commit_data_file_location: str, commit_number: int) -> Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]:
```
#### Parameters
- **'commit_data_file_location'** (str): The path to the commit data file.
- **'commit_number'** (int): The commit number to retrieve.
#### Returns
- **'Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]'**: A dictionary containing commit data, where keys are line numbers, and values are tuples containing lists of insertions and deletions.
#### Description
- Reads commit data from the specified commit data file.
- Searches for the commit with the specified commit number.
- Returns a dictionary containing commit data.

### Notes
- The functions are designed to handle the writing and reading of commit data in the Pastport system.
- The commit data file uses a pilcrow symbol (\u00b6) as a delimiter to separate different components of the commit data.

> &#x26A0; Ensure that the required modules are properly imported before using the functions.





# Reconstruction Module
The **'reconstruction'** function is designed to reconstruct an old text file based on commit data generated by the **'diff_algorithm module'**. This process involves applying insertions and deletions to the original text to create a new version of the file.
## File: reconstuctor.py
### Function: reconstruction
```
def reconstruction(old_file_location: str, commit_data: Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]], outfile_location: str = 'temp_old.txt') -> None:
```
#### Parameters
- **'old_file_location'** (str): The path to the original text file.
- **'commit_data'** (Dict[int, Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]]): A dictionary containing commit data, where keys are line numbers, and values are tuples containing lists of insertions and deletions.
- **'outfile_location'** (str, optional): The path to the reconstructed output file. Defaults to 'temp_old.txt'.

#### Description
- Reads the content of the original text file.
- Applies insertions and deletions based on commit data to reconstruct the original text.
- Writes the reconstructed text to the specified output file.

### Notes
- The function ensures that insertions and deletions are appropriately applied to the original text to reconstruct a new version of the file.
- The reconstructed text is written to the specified output file.








# PASTPORT Command Line Interface (PRT CLI)
The PASTPORT Command Line Interface (PRT CLI) provides a user-friendly interface for interacting with the PASTPORT version control system. The CLI supports various commands for initializing, committing, checking out, and checking the status of the PASTPORT system.

## File: cli.py
### Modules
1. **'terminal_output'** Module
The **'terminal_output'** module is responsible for formatting and displaying output messages in the terminal with different colors.

2. **'prt_init'** Module
The **'prt_init'** module handles the initialization of the PASTPORT system. It creates the necessary directory structure and tracking files for version control.

3. **'prt_commit'** Module
The **'prt_commit'** module manages the commit process in the PASTPORT system. It reconstructs old files, generates commit data, and updates the tracking files.

4. **'prt_checkout'** Module
The **'prt_checkout'** module handles the checkout process, allowing users to revert to a specific commit by reconstructing the files based on commit data.

5. **'prt_status'** Module
The **'prt_status'** module provides functionality to check the status of the working directory, identifying modified, untracked, and deleted files.

### Boot-up Sequence Function: 'boot_up_sequence'
```
def boot_up_sequence() -> str:
```
#### Returns
- **'str'**: The absolute path of the directory chosen by the user during the boot-up sequence.

#### Description
- Displays the PASTPORT banner and prompts the user to enter the directory location.
- Validates the entered location and returns the absolute path.

### Main Program
```
location = boot_up_sequence()
while True:
    command = input("pastport >> ").lower().split(" ")
    # ... Command handling logic ...
```
#### Description
- The main program prompts the user for commands and executes the corresponding functionality based on user input.
### Supported Commands
1. Initialization Command: init
```
import prt_init as pi
pi.prt_init(location=location)
```
- Initializes the PASTPORT system in the specified directory.
2. Committing Command: commit
```
import prt_commit as pc
pc.prt_commit(location, message)
```
- Commits changes to the PASTPORT system with an optional commit message.
3. Checkout Command: checkout
```
import prt_commit as pck
pck.prt_checkout(commit_number, location)
```
- Checks out a specific commit, reverting the working directory to that commit.
4. Status Command: status
```
import prt_status as ps
status = ps.prt_status(location)
modified, untracked, deleted = status.get_status()
```
- Checks the status of the working directory, displaying modified, untracked, and deleted files.
5. Log Command: log
```
log_file = open(location + "/prt/{}.log".format(directory_name.lower()), 'r')
log_lines = log_file.readlines()
log_file.close()
```
- Displays a log of commit details, including commit numbers, files, and commit messages.
6. Quit Command: quit or q
- Exits the PASTPORT CLI.

### Example Usage
```
# Execute the PASTPORT CLI
python cli.py
```
### Notes
- The PRT CLI is designed to be intuitive and user-friendly, providing a simple interface for version control with PASTPORT.







# Terminal Output Module
The **'output'** function is a simple utility function designed to format and display colored text messages in the terminal. It enhances the visual representation of messages by allowing the user to specify different colors for the text.
## File: terminal_output.py
### Function Signature
```
def output(message, color=""):
```
#### Parameters
- **'message'** (str): The text message to be displayed in the terminal.
- **'color'** (str, optional): The color code or name for the text. Default is an empty string (**'""'**). Available color options are "red" (**'r'**), "green" (**'g'**), "amber" (**'a'**), "blue" (**'b'**), "pink" (**'p'**), "cyan" (**'c'**), or an empty string for the default color.

#### Description
- The **'output'** function prints the specified **'message'** in the terminal with the specified color. If no color is provided or an invalid color is given, the function defaults to the terminal's default text color.

#### Example Usage
```
# Print a message in red color
output("Error: Something went wrong", color="red")

# Print a message in green color (default color if not specified)
output("Operation successful", color="g")

# Print a message in amber color
output("Warning: Proceed with caution", color="a")
```
### Notes
- The function uses ANSI escape codes to set the text color in the terminal.
- It is a utility function and can be used to enhance the visual presentation of messages in command-line interfaces.

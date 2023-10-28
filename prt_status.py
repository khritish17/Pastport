'''
    Returns an list status = [[list of all modified files], [list of all untracked files], [list of all deleted files]]
'''

import os 
import file_translator as ft
import reconstructor as re

class prt_status:
    def __init__(self, location = "") -> None:
        self.location = os.path.abspath(location)
        self.modified = []
        self.untracked = []
        self.deleted = []
        self.common_files = []
        self.tracked_files = []
        self.current_files = []
        
        # get the directory name 
        self.directory_name = self.location.split("\\")[-1]
     
        cur_commit_file = open(self.location + "\prt\{}.curcommit".format(self.directory_name))
        last_commit_number = int(cur_commit_file.readline())
        cur_commit_file.close()

        tracking_file_location = self.location + "/prt/{}.track".format(self.directory_name.lower())
        tracking_file = open(tracking_file_location, 'r')
        
        tracking_recent_line = tracking_file.readlines()[last_commit_number]
        self.tracked_files = tracking_recent_line.split('\u00b6')[-1].rstrip('\n').split(',')
        

        file_list = os.listdir(self.location)
        for file_dir in file_list:
            if os.path.isfile(self.location + "\{}".format(file_dir)):
                self.current_files.append(file_dir)
        
        self.check_deleted()
        self.check_untracked()
        self.check_modified(last_commit_number)
        

    def check_modified(self, last_commit_number):
        # reconstruct the common files based on the last commit number
        # for each reconstructed file compare line by line
        for common_file in self.common_files:
            common_file_name = common_file.split('.')[0]
            commit_data = ft.read_commit(self.location + "/prt/{}.commit".format(common_file_name), last_commit_number)
            re.reconstuction(self.location + "/{}".format(common_file), commit_data, self.location + "/{}.reconstructed".format(common_file_name))

            file = open(self.location + "/{}".format(common_file), 'r')
            file_lines = file.readlines()
            file.close()

            reconst_file = open(self.location + "/{}.reconstructed".format(common_file_name), 'r')
            reconst_file_lines = reconst_file.readlines()
            reconst_file.close()
            
            if len(file_lines) != len(reconst_file_lines):
                self.modified.append(common_file)
                continue

            for i in range(len(file_lines)):
                if file_lines[i] != reconst_file_lines[i]:
                    self.modified.append(common_file)
                    break
            
            os.remove(self.location + "/{}.reconstructed".format(common_file_name))
    
    def check_untracked(self):
        for current_file in self.current_files:
            if current_file not in self.tracked_files:
                self.untracked.append(current_file)

    def check_deleted(self):
        for tracked_file in self.tracked_files:
            if tracked_file not in self.current_files:
                self.deleted.append(tracked_file)
            else:
                self.common_files.append(tracked_file)

    def get_status(self):
        return self.modified, self.untracked, self.deleted
# st = prt_status(location= r'D:\Codes\Projects\Pastport\test_folder')
# modified, untracked, deleted = st.get_status()
# print("Modified: {}".format(modified))
# print("Untracked: {}".format(untracked))
# print("Deleted: {}".format(deleted))
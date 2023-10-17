import os
import diff_algorithm as da
class prt_commit:
    def __init__(self, file, location = "") -> None:
        # the work of the commit file is to reconstructs the old file 
        # and sends it along the new file to diff_algo for commit data creation
        self.location = self.location = os.path.abspath(location)
        self.file = file
        # get the directory name 
        self.directory_name = self.location.split("\\")[-1]

        # tracking file location 
        self.tracking_file_location  = self.location + "/prt/{}.track".format(self.directory_name.lower())
        try:
            directory_list = os.listdir(self.location + "/prt/")
        except:
            print("Pastport not been initialized")
            exit()
        
        # first read the lines in tracking file
        tracking_file = open(self.tracking_file_location, 'r')
        tracking_lines = tracking_file.readlines()
        if len(tracking_lines) == 0:
            # Initiate cold start commit
            self.cold_commit()
        else:
            self.commit()
    
    def write_commit(self):
        commit_data_file = open(self.location + "/prt/{}.commit".format(self.file_name), "a")
        commit_data_file.close()
        pass
    
    def read_commit(self):
        pass

    def commit(self):
        # generate the old file, 
        # send it to diff_algorithm along with new file, get the commit data 
        # store in the commit file
        pass
    
    def cold_commit(self):
        self.file_name = self.file.split('.')[0]
        old_file = open(self.location + "/{}.old".format(self.file_name), 'w')
        old_file.close()
        commit_data = da.diff_algorithm(self.location + "/{}.old".format(self.file_name), self.location +"/{}".format(self.file) )
        print(commit_data)
        # create the commit data file
        commit_data_file = open(self.location + "/prt/{}.commit".format(self.file_name), "w")
        commit_data_file.close()
        os.remove(self.location + "/{}.old".format(self.file_name))

        pass
cmt = prt_commit('old.txt')
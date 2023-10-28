import os
import diff_algorithm as da
import file_translator as ft 
import reconstructor as rc
class prt_commit:
    def __init__(self, location = "", message = "Untitled Commit") -> None:
        # the work of the commit file is to reconstructs the old file 
        # and sends it along the new file to diff_algo for commit data creation
        self.location = os.path.abspath(location)
        self.message = message
        # get the directory name 
        self.directory_name = self.location.split("\\")[-1]

        # tracking file location 
        self.tracking_file_location  = self.location + "/prt/{}.track".format(self.directory_name.lower())
        try:
            os.listdir(self.location + "/prt/")
        except:
            print("Pastport not been initialized")
            exit()
        
        # first read the lines in tracking file
        tracking_file = open(self.tracking_file_location, 'r')
        tracking_lines = tracking_file.readlines()
        tracking_file.close()
        # self.commit('old.txt')

        directory_list = os.listdir(self.location)
        file_list = []
        for file_dir in directory_list:
            if os.path.isfile(self.location + "/{}".format(file_dir)):
                file_list.append(file_dir)

        if len(tracking_lines) == 0:
            # Initiate cold start commit
            tracking_file = open(self.tracking_file_location, 'w')
            tracking_file.write("0\u00b6")

            for i in range(len(file_list)):
                file = file_list[i]
                self.cold_commit(file= file, commit_number= 0)
                if i != len(file_list) - 1:
                    tracking_file.write("{},".format(file))
                else:
                    tracking_file.write("{}\n".format(file))
            tracking_file.close()
            # --
            # writing the current commit number to .curcommit file
            cur_commit_file = open(self.location + "/prt/{}.curcommit".format(self.directory_name.lower()), 'w')
            cur_commit_file.write('0')
            cur_commit_file.close()
            # --
        else:
            # Initiate normal commit for tracked files and cold commit for untracked files
            tracking_file = open(self.tracking_file_location, 'r')
            tracking_lines = tracking_file.readlines()
            latest_tracking_entry = tracking_lines[-1].split('\u00b6')
            commit_number = int(latest_tracking_entry[0])
            tracked_files = latest_tracking_entry[1].rstrip('\n').split(",")
            tracking_file.close()
            
            tracking_file = open(self.tracking_file_location, 'a')
            tracking_file.write("{}\u00b6".format(commit_number + 1))
            for i in range(len(file_list)):
                file = file_list[i]
                
                if file in tracked_files:
                    self.commit(file= file, commit_number= commit_number + 1)
                else:
                    self.cold_commit(file= file, commit_number= commit_number + 1)
                if i != len(file_list) - 1:
                    tracking_file.write("{},".format(file))
                else:
                    tracking_file.write("{}\n".format(file))
            tracking_file.close()

            # --
            # writing the current commit number to .curcommit file
            cur_commit_file = open(self.location + "/prt/{}.curcommit".format(self.directory_name.lower()), 'w')
            cur_commit_file.write(str(commit_number))
            cur_commit_file.close()
            # --

            


    def commit(self, file, commit_number):
        file_name = file.split('.')[0]
        # generate the old file, 
        initial_commit_data = ft.read_commit(self.location + "/prt/{}.commit".format(file_name), 0)
        old_file = open(self.location + "/{}.temp".format(file_name), 'w')
        old_file.close()
        rc.reconstuction(self.location + "/{}.temp".format(file_name), initial_commit_data, self.location + "/{}.old".format(file_name))
        os.remove(self.location + "/{}.temp".format(file_name))
        
        # send it to diff_algorithm along with new file, get the commit data 
        commit_data = da.diff_algorithm(self.location + "/{}.old".format(file_name), self.location + "/{}".format(file))
        os.remove(self.location + "/{}.old".format(file_name))
        
        ft.write_commit(self.location + "/prt/{}.commit".format(file_name), commit_data, commit_number, self.message)
    
    def cold_commit(self, file, commit_number):
        file_name = file.split('.')[0]
        old_file = open(self.location + "/{}.old".format(file_name), 'w')
        old_file.close()
        commit_data = da.diff_algorithm(self.location + "/{}.old".format(file_name), self.location +"/{}".format(file) )
        # create the commit data file
        commit_data_file = open(self.location + "/prt/{}.commit".format(file_name), "w")
        commit_data_file.close()
        os.remove(self.location + "/{}.old".format(file_name))
        
        ft.write_commit(self.location + "/prt/{}.commit".format(file_name), commit_data, commit_number, "Initial commit")

cmt = prt_commit(location= r'D:\Codes\Projects\Pastport\test_folder')
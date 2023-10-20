import os
import file_translator as ft
import reconstructor as rc

class prt_checkout:
    def __init__(self, commit_number, location = "") -> None:
        self.location = os.path.abspath(location) 
        self.commit_number = int(commit_number)
        # a sanity check whether passport is already initialized or not 
        try:
            os.listdir(self.location + "/prt/")
        except:
            print("Pastport not been initialized")
            exit()
        # get the directory name 
        self.directory_name = self.location.split("\\")[-1]
        
        tracking_file_location = self.location + "/prt/{}.track".format(self.directory_name.lower())
        tracking_file = open(tracking_file_location, 'r')
        tracking_lines = tracking_file.readlines()
        try:
            checkout_files = tracking_lines[commit_number].split('\u00b6')[1].rstrip('\n').split(',')
        except:
            print("Invalid commit id")
            exit()
        
        for file in checkout_files:
            # print(file)
            file_name = file.split('.')[0]
            
            # reconstructing the old/initial file or the initial commit
            if commit_number != 0:
                initial_commit_file = open(self.location + "/{}.temp".format(file_name), 'w')
                initial_commit_file.close()
                initial_commit_data = ft.read_commit(self.location + "/prt/{}.commit".format(file_name), 0)
                rc.reconstuction(self.location + "/{}.temp".format(file_name), initial_commit_data, self.location + "/{}.old".format(file_name))
                os.remove(self.location + "/{}.temp".format(file_name))
            else:
                initial_commit_file = open(self.location + "/{}.old".format(file_name), 'w')
                initial_commit_file.close()
            # break

            # retrieve the commit data for the checkout commit number
            commit_data = ft.read_commit(self.location + "/prt/{}.commit".format(file_name), commit_number)
            # reconstruct the file according to the commit number and commit data
            rc.reconstuction(self.location + "/{}.old".format(file_name), commit_data, self.location + "/{}.new".format(file_name))
            os.remove(self.location + "/{}.old".format(file_name))
            # continue

            # file manipulation
            # now first delete the original file
            os.remove(self.location + "/{}".format(file))
            # and rename the .new file to original name 
            os.rename(self.location + "/{}.new".format(file_name), self.location + "/{}".format(file))
            
CO = prt_checkout(2, location= r'D:\Codes\Projects\Pastport\test_folder')

import os

class prt_init:
    def __init__(self, location = "") -> None:
        self.location = os.path.abspath(location)

        # get the directory name 
        self.directory_name = self.location.split("\\")[-1]
        
        # go to the location and scane the files and sub directories
        # the dir_list contains both files and sub dir
        # but we will track only files
        directory_list = os.listdir(self.location)
        self.file_list = []
        for file_dir in directory_list:
            if os.path.isfile(file_dir):
                self.file_list.append(file_dir)
        # create the pastport directory 
        try:
            os.mkdir(self.location + "/prt")
            self.create_tracking_file()
        except:
            print("Unexpected Error, contact at khritish.official@gmail.com")
            exit()
    
    def create_tracking_file(self):
        tracking_file = open(self.location + "/prt/{}.track".format(self.directory_name.lower()),'w')
        tracking_file.write("0\\")
        for i in range(len(self.file_list)):
            file = self.file_list[i]
            if i != len(self.file_list) - 1:
                tracking_file.write("{},".format(file))
            else:
                tracking_file.write("{}\n".format(file))
        


init = prt_init()
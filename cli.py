import terminal_output as to
import os
import time
import prt_init as pi
import prt_commit as pc
import prt_checkout as pck
import prt_status as ps
def boot_up_sequence():
    to.output("PASTPORT COMMAND LINE INTERFACE (PRT CLI)\n---Authored by Khritish Kumar Behera---", "g")
    time.sleep(1)
    to.output("Boot up the PASTPORT application by specifying the directory location.")
    location = ""
    while True:
        location = input("LOCATION >> ")

        if not os.path.exists(location):
            to.output(" Invalid location detected!! A valid path is required for booting the PASTPORT system", "r")
        else:
            break
    return location


location = boot_up_sequence()
while True:
    command = input("pastport >> ").lower().split(" ")
    if command[0] == "quit" or command[0] == "q":
        break
    
    # Initialization command
    elif command[0] == "init":
        pi.prt_init(location= location)
        to.output("Intialization Successful", "g")
    
    # Commiting command
    elif command[0] == "commit":
        # try:
        #     message = " ".join(command[1:])
        # except:
        #     message = "Untitled Message"
        message = " ".join(command[1:])
        if not message:
            message = "Untitled Message"
        pc.prt_commit(location, message)
        to.output("Commit Successful", "g")
    
    # Checkout command
    elif command[0] == "checkout":
        try:
            commit_number = int(command[1])
            pck.prt_checkout(commit_number, location)
            to.output("Checkout Successful", "g")
        except:
            to.output("Checkout process requries the commit number", "r")
        
    # Status command
    elif command[0] == "status":
        status = ps.prt_status(location)
        modified, untracked, deleted = status.get_status()
        if modified:
            files = " ".join(modified)
            to.output("Modified:\t{}".format(files), "p")
        else:
            to.output("Modified:\t<NIL>", "g")
        if untracked:
            files = " ".join(untracked)
            to.output("Untracked:\t{}".format(files), "g")
        else:
            to.output("Untracked:\t<NIL>", "g")
        if deleted:
            files = " ".join(deleted)
            to.output("Deleted:\t{}".format(files), "r")
        else:
            to.output("Deleted:\t<NIL>", "g")
        

    elif command[0] == "log":
        directory_name = location.split("\\")[-1]
        tracking_file = open(location + "/prt/{}.track".format(directory_name.lower()), 'r')
        tracking_lines = tracking_file.readlines()
        tracking_file.close()

        log_file = open(location + "/prt/{}.log".format(directory_name.lower()), 'r')
        log_lines = log_file.readlines()
        log_file.close()
        to.output("{}\t{}\t{}".format("commit_no", "file"," message"), "g")
        for i in range(len(log_lines)):
            file = tracking_lines[i].split('\u00b6')[-1].rstrip('\n').split(',')
            commit_no, message = log_lines[i].split('\u00b6')
            message = message.rstrip('\n')
            to.output("{}\t{}\t{}".format(commit_no, file, message), "b")



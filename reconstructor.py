import diff_algorithm as da

def reconstuction(old_file, commit_data, outfile = 'temp_old.txt'):
    old = open(old_file, 'r')
    old_lines = old.readlines()

    new = open(outfile, 'w')
    for i in range(max(len(old_lines), len(commit_data))):
        try:
            old_line = old_lines[i].split(' ')
        except:
            old_line = ""
        length = len(old_line) + len(commit_data[i][0]) - len(commit_data[i][1])
        new_line = [None]*length
        # process the insertion operation
        insertion = commit_data[i][0]
        for insert_word, insert_index in insertion:
            new_line[insert_index] = insert_word
        
        # process the deletion opeartaion
        deletion = commit_data[i][1]
        for delete_word, delete_index in deletion:
            old_line[delete_index] = None

        for i in range(len(new_line)):
            if new_line[i] == None:
                while old_line:
                    poped_word = old_line.pop(0)
                    if poped_word != None:
                        new_line[i] = poped_word
                        break
        new_line = ' '.join(new_line) + '\n'
        new.write(new_line)


# commit_data = da.diff_algorithm('old.txt', 'new.txt')
# # print(commit_data)
# reconstuction('old.txt', commit_data)

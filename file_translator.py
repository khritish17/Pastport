def write_commit(commit_data_file_location, commit_data, commit_number, commit_message):
    # delimeter used is Pilcrow symbol
    # print(commit_data)
    commit_data_file = open(commit_data_file_location, 'a')
    commit_data_file.write(str(commit_number)+"\u00b6")
    for line, commits in commit_data.items():
        insertion = commits[0]
        deletion = commits[1]
        commit_data_file.write("{}\u00b6{}\u00b6{}".format(line, len(insertion)*2, len(deletion)*2))
        for word, index in insertion:
            commit_data_file.write("\u00b6{}\u00b6{}".format(word, index))
        
        for word, index in deletion:
            commit_data_file.write("\u00b6{}\u00b6{}".format(word, index))
        commit_data_file.write("\u00b6")
    commit_data_file.write("{}\n".format(commit_message))

    commit_data_file.close()


def read_commit(commit_data_file_location, commit_number):
    commit_data_file = open(commit_data_file_location, 'r')
    commits = commit_data_file.readlines()
    if len(commits) == 0:
        print("No commits have been made yet! [-_-]")
        exit()
    commit_raw = commits[commit_number] # 0 indexed based as the initial commit is always zero
    commit_array = commit_raw.split('\u00b6')
    i = 1
    commit_data = {}
    # print(commit_array)
    while i < len(commit_array) - 1:
        line_number = commit_array[i]
        i += 1
        # print("-> {}".format(commit_array[i]))
        insertion_length = int(commit_array[i])
        i += 1
        deletion_length = int(commit_array[i])
        i += 1

        insertion = []
        for j in range(insertion_length):
            if j % 2 != 0:
                i += 1
                continue
            insertion.append( (commit_array[i], int(commit_array[i + 1])) )
            i += 1
        
        deletion = []
        for j in range(deletion_length):
            if j % 2 != 0:
                i += 1
                continue
            insertion.append( (commit_array[i], int(commit_array[i + 1])) )
            i += 1
        commit_data[int(line_number)] = (insertion, deletion)
    commit_data_file.close()
    return commit_data


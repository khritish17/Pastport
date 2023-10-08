
def generate_commit_data(old_text, new_text, lcs):
    # make sure to deal with old_text/new_text which are empty([]), becoz line 45, 47
    # old text, new text are arrays 
    old_index = []
    new_index = []
    for word, old_ind, new_ind in lcs:
        old_index.append(old_ind)
        new_index.append(new_ind)

    insertion = []
    for i in range(len(new_text)):
        if i not in new_index:
            insertion.append((new_text[i], i))

    deletion = []
    
    for i in range(len(old_text)):
        if i not in old_index:
            deletion.append((old_text[i], i))
    return insertion, deletion

def backtracking(old_text, new_text, dp):
    lcs = []
    if old_text and new_text:
        i, j = len(dp) - 1, len(dp[0]) - 1
        while i != 0 and j != 0:
            old_word = old_text[i - 1]
            new_word = new_text[j - 1]

            if old_word == new_word:
                i, j = i - 1, j - 1
                lcs = [(old_word, i, j)] + lcs
            else:
                # old word != new word
                if dp[i][j - 1] >= dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        
    return generate_commit_data(old_text, new_text, lcs)
    # write the insertion and deletion 

def longest_common_subsequence(old_text, new_text):
    # old_text and new_text are just single lines in text file
    old_text = old_text.rstrip("\n").split(" ")
    new_text = new_text.rstrip("\n").split(" ")
    dp = [[0 for j in range(len(new_text) + 1)] for i in range(len(old_text) + 1)]
    for i in range(1, len(old_text) + 1):
        for j in range(1, len(new_text) + 1):
            old_index, new_index = i - 1, j - 1
            old_word, new_word = old_text[old_index], new_text[new_index]
            if old_word == new_word:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    if old_text == ['']:
        old_text = []
    if new_text == ['']:
        new_text = []
    return backtracking(old_text, new_text, dp)
    
             

def diff_algorithm(old_file, new_file):
    # opening the old file in read mode 
    old = open(old_file, 'r')
    old_lines = old.readlines()
    old_length = len(old_lines)
    
    # opening the old file in read mode
    new = open(new_file, 'r')
    new_lines = new.readlines()
    new_length = len(new_lines)
    
    # closing the files, since we have scan the files
    # there is no need to keep the files open
    old.close()
    new.close()
    
    commit_data = {}
    for i in range(max(old_length, new_length)):
        try:
            old_line = old_lines[i]
        except:
            old_line  = ""
        
        try:
            new_line = new_lines[i]
        except:
            new_line = ""
        
        commit_data[i] = longest_common_subsequence(old_line, new_line)
    return commit_data
print(diff_algorithm('old.txt', 'new.txt'))
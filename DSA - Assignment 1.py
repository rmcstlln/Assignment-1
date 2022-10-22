letters = {
    'M': ['*     *', '**   **', '* * * *', '*  *  *', '*     *', '*     *', '*     *'],
    'A': [' ***** ', '*     *', '*     *', '*******', '*     *', '*     *', '*     *'],
    'R': ['****** ', '*     *', '*     *', '****** ', '*     *', '*     *', '*     *'],
    'K': ['*     *', '*    * ', '*  *   ', '***    ', '*   *  ', '*    * ', '*     *']
}

nickname = 'MARK'

#print(len(string))
for i in range(7):


    for word in range(len(nickname)):
        current_word = nickname[word].upper()
        if word == len(nickname)-1 :
            print(letters[current_word][i])
        else :
            print(letters[current_word][i],end='  ')

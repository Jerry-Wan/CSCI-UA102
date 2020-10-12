def vc(word, vowels, consonants,a):
    if a == len(word):
        return [vowels,consonants]
    elif(word[a]== 'a' or word[a] == 'e' or word[a] == 'i' or word[a] == 'o' or word[a] == 'u'
       or word[a] == 'A' or word[a] == 'E' or word[a] == 'I' or word[a] == 'O' or word[a] == 'U'):
        vowels = vowels + 1
        newA = a+1
        return vc(word, vowels, consonants,newA)
    else:
        consonants = consonants + 1
        newA = a+1
        return vc(word, vowels, consonants,newA)

def vc_count(word):
    """
    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!
    
    :param word: String -- the input string
    :return: List[Int] -- the first integer is the number of vowels, 
                          the second integer is the number of consonants.
    """
    vowels = 0
    consonants = 0
    a = 0
    return vc(word, vowels, consonants, a)

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()

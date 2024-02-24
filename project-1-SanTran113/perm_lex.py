from typing import List
# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []

def perm_gen_lex(str_in: str) -> List:
    count = 0
    # finalList = []
    l = []
    for p in perm_gen_lex_helper(str_in):
        l.append(''.join(p))
        # print(p)
        # print (l)
    return l
    # if str_in == '' or len(str_in) == 1:
    #    return [str_in]
    # return perm_gen_lex_helper(str_in[0] + str_in[1:], "", finalList, str_in, False)


def perm_gen_lex_helper(str_in: str) -> List:
    l = []

    if str_in == '':
        return []
    if len(str_in) == 1:
        return [str_in]
    # str_in = list(str_in)

    for i in range(len(str_in)):
        print(f"i: {i}")
        letter = str_in[i]
        remaning = str_in.replace(letter, '')
        # print(initialList)
        remaning = ''.join(remaning)
        # remaning = str_in[:i] + str_in[i+1:]
        # if len(remaning) <= 1:
        #    break;
        # print(f"l: {letter}")
        # print(f"r: {''.join(remaning)}")

        for p in perm_gen_lex_helper(remaning):
            # l.append([m] + p)
            l.append(letter + p)
            # print([letter] + p)
    return l


print(perm_gen_lex("abc"))

# why it switch?

# def perm_gen_lex(str_in: str) -> List:
#     count = 0
#     finalList = []
#     if str_in == '' or len(str_in) == 1:
#         return [str_in]
#     return perm_gen_lex_helper(str_in[0] + str_in[1:], finalList)
# def perm_gen_lex_helper(str_in: str) -> List:
#     initialList = [str_in]
#     count = 0
#     initialList = [*str_in]
#     print([*str_in])
#     for _ in initialList:
#         letter = initialList[0]
#         remaning = initialList[1:]
#         remaning = ''.join(remaning)
#         print(f"l: {letter}")
#         print(f"r: {remaning}")
#         result = perm_gen_lex_helper(remaning, finalList)
#         previous = remaning
#         print(f"previous: {previous}")
#     if len(result) == 1:
#         finalList = letter + remaning
#         print(f"finallist: {finalList}")
#         return finalList

    # if count < len(str_in) - 1:
    # for j in range(count, len(str_in)):
    #     str_in[count], str_in[j] = str_in[j], str_in[count]
    #     perm_gen_lex_helper(str_in, count + 1, l)
    #     str_in[count], str_in[j] = str_in[j], str_in[count]

    # if count < len(initialList):
    #     letter = initialList[0][count] #current letter
    #     next_letter = initialList[0][count + 1]
    #     templist.append(letter + next_letter) # adding first two numbers
    #     count += 1
    #     print(templist)
    #     return perm_gen_lex_helper(templist) #call the function again to see if count increased
    # if count > len(initialList):
    #     return perm_gen_lex_helper(str_in)


# if count == len(str_in) - 1:
#     l.append(''.join(str_in))
#


#     initialList = [str_in]
#     templist = []
#     count = 0

#
#     # tempList.append(letter + next_letter)
#     # tempList.append(next_letter + letter)
#     #
#     # finalList.append("c" + tempList[0])
#     # finalList.append("c" + tempList[1])
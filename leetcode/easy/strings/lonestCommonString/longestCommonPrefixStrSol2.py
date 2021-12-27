def longestCommonPrefix(strs) -> str:
    index = -1
    for i, s in enumerate(zip(*strs)):
        print(i,s)
        if len(set(s)) != 1:
            index = i-1
            break
    print(index)
    print(strs[0][:index])


longestCommonPrefix(["flower","flow","flower"])

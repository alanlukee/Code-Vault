def findlongSubstring(str):
    charSet=()
    l=0
    length = 0
    for r in range(len(str)):
        while str[r] in charSet:
            charSet.remove(str[l])
            l=l+1
        charSet.add(str[r])
        length = max(length, r-1 +1)
    return length



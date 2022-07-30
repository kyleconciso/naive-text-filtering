# Censors matching words in a string


words = ["cake"]
censor = "*"

def filter(str):
    out = ""

    for pos in range(len(str)):
        if pos>=len(out):

            found = False
            for target in words:
                check = str[pos:pos+len(target)]
                if check == target:
                    out += censor*len(target)
                    found = True

            if not found:
                out += str[pos]
        
    return out



filtered = filter(input("Filter this sentence: "))
print(filtered)


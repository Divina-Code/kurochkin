#!/usr/bin/env python3

st = "string word sentense"
print(st.split())    # split elements in string
print(st.split()[1])
st = "string, gh"
st = st.split(', ')
print(st)

print("sime words", ", **".join(st)) # glue elements from list

for g in st:  # print list elements
    print(g.title(), "- words index -", st.index(g))

for w in "sent":  # print letters from word
    print(w)

print(*range(10)) # * - print list like there is many elements
print(range(100))
print(*range(0 ,10, 2)) # [START:STOP:STEP]

for er in range(0, 10, 2):
    print(er)

lis = [12, 32, 245, 3425, 4, 9]

for g in range(len(lis)):
    if g > 0 and lis[g] > lis[g-1]:
        print("element", lis[g])
        lis.append(g-1)


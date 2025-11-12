with open('social_media.txt','r') as file:
    content=file.read()

import pandas as pd
import matplotlib.pyplot as pl

content=content.replace("the","")
content=content.replace("of","")
new=content.replace("and","")
print(new)

words=new.split()
freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

def count(item):
    return item[1]

sort=sorted(freq.items(), key=count, reverse=True)
top=sort[:10]
word_list=[item[0] for item in top]
count_list=[item[1] for item in top]

for word, count in sort[:10]:
    print(f"{word} : {count}")


pl.bar(word_list, count_list)
pl.xlabel("Words")
pl.ylabel("Count")
pl.title("Title")
pl.show()

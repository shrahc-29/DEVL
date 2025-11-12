with open('social_media.txt','r') as file:
  content=file.read()

words=content.split()
freq={}

for word in words:
  if word in freq:
    freq[word]+=1
  else:
  freq[word]=1

def count(item)
  return item[1]

sort=sorted(freq.items(), key=count, reverse=True)

for word, count in sort[:10]:
  print(f"{word} : {count}")

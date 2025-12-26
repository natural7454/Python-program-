text=input("Enter the sentence-:")

words=text.lower().split()

frequency={}

for word in words:
    if word in frequency:
        frequency[word]=frequency[word]+1
    else:
        frequency[word]=1
print("word Frequency-:")
for word,count in frequency.items():
    print(word,":",count)

















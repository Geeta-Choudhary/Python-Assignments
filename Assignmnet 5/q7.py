from collections import Counter
import re
fp=open('input.txt','r')
content=fp.read().lower()
# Split the content into words using regex to remove punctuation
words = re.findall(r'\w+', content)
word_count = Counter(words)
# Display the word frequencies in descending order
#for word, count in word_count.most_common():
for word, count in sorted(word_count.items(), key=lambda x: x[1],reverse=True):
        print(f"{word}: {count}")


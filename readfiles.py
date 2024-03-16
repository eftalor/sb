import sys 
from collections import Counter
import os
import glob


#file_list = sys.argv[1].split(',') 
#print("files to be processed:", )

txt_files = glob.glob('./*.txt')
txt_files.sort(key=os.path.getmtime, reverse=True)
file_list = txt_files[:4]
print("files to be processed:",file_list )

def filesfunc(file_list):
  words = []
  for file in file_list:
    with open(file, "r") as f:
      for line in f:
        words.extend(line.split())

    counts = Counter(words)  
    top5 = counts.most_common(5)
  
  #return top5
    print(f"Top 5 words for {file}:")
    print(top5)
    print()

filesfunc(file_list)

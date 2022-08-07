"""
Project - Sentiment Classifier
Number of Retweets, Number of Replies,
Positive Score , Negative Score , 
Net Score [p-n]
"""
#%%
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for i in punctuation_chars:
        if i in word:
            word = word.replace(i,"")
    return word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(s) : 
    words = s.split()
    p_word_count=0
    for word in words:
        if strip_punctuation(word).lower() in positive_words:
            p_word_count+=1
    return p_word_count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s):
    words = s.split()
    n_word_count=0
    for word in words:
        if strip_punctuation(word).lower() in negative_words:
            n_word_count+=1
    return n_word_count

with open("project_twitter_data.csv","r") as f1,open("resulting_data.csv","w") as f2:


    f2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    for line in f1.readlines()[1:]:
        line=line.strip().split(',')
        print(line)
        sentence,n_ret,n_rep=line
        p_score=get_pos(sentence)
        n_score=get_neg(sentence)
        net_score=p_score-n_score
        # print("Retweets",n_ret,
        # "Replies",n_rep,
        # "Positive Score",p_score,
        # "Negative Score",n_score,
        # "Net Score",net_score)
        row = f"\n{n_ret},{n_rep},{p_score},{n_score},{net_score}"
        f2.write(row)
    f2.write("\n")
# %%
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("resulting_data.csv")
x=df[" Net Score"]
y=df["Number of Retweets"]  
plt.scatter(x,y)
plt.ylabel('Number of Retweets',fontweight='bold')
plt.xlabel('Net Score',fontweight='bold')
plt.title("Number of Retweets VS Net Score",fontweight='bold')
plt.show()
# %%

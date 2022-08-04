#%%
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro=[]
for i in sent.split():
    if i not in stopwords:
        acro.append(i[0:2].upper())
acro='. '.join(acro)
print(acro)
# %%

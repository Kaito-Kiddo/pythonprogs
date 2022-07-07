#%%
# use these 2 objects for coursera assignment
# csv_file_location = '/home/student-03-7355c07eebe4/data/user_emails.csv'
# report_file = '/home/student-03-7355c07eebe4/data/updated_user_emails.csv'


import csv
import re

# with open(csv_file_location,"r") as f1, open(report_file,"w") as f2:
with open('email_domains.csv',"r") as f1, open("updated_email_domains.csv","w") as f2:
    for line in f1:
        print(line)
        line = re.sub(r"@(abc.edu)",r"@xyz.edu",line)
        # print(line)
        f2.write(line)
# %%

import os
for pg in range(1,20,2):
    os.system('python outsource4pj.py %d >> data.csv' % pg)
import datetime
import os
import random
import subprocess

#OMG PLZ SEND PULL REQUESTS WITH MORE AWESOME MSGS
messages = [
  "My kid's appointment at the pediatrician can wait, I need to get this commit in.",
  "Sorry honey, I need to keep my streak going - we'll have sex tomorrow!",
  "This commit brought to you by my privilege.",
  "My employer lets me use work time to contribute to open source."
  "The dog ate my commit."
]

rr = "Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you"

if not subprocess.check_output('git rev-parse --abbrev-ref HEAD', stderr=subprocess.STDOUT).strip() == 'master':
    raise Exception('plz run from master, kthx')
subprocess.check_output('git reset --hard refs/heads/master', stderr=subprocess.STDOUT)

print 'Traveling back in time to the founding of Github! (actually, just a year.)'
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now() + datetime.timedelta(days=1)

def daterange():
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

i = 0
for single_date in daterange():
    str = rr.split(' ')[i % 34]
    extra = "\n" if i % 34 == 0 else ' '
    if i != 0:
        str = extra << str

    with open('self_worth.txt', 'a') as f:
        f.write(str)

    with open('msg.txt', 'w') as f:
        f.write(random.choice(messages))

    t = (single_date - datetime.datetime.utcfromtimestamp(0)).total_seconds() + 14400 + random.randint(0,57600)
    subprocess.check_output('git filter-branch -f --env-filter \"GIT_COMMITTER_DATE=\'{:.2f}\';\"'.format(float(t)), stderr=subprocess.STDOUT)
    subprocess.check_output('git filter-branch -f --env-filter \"GIT_AUTHOR_DATE=\'{:.2f}\';\"'.format(float(t)), stderr=subprocess.STDOUT)
    print subprocess.check_output('git commit -q -F msg.txt -- self_worth.txt', stderr=subprocess.STDOUT)
    i += 1
    print "\r\nProving your worth with commits in " + d.strftime("%B, %Y") + "..."

os.remove("msg.txt")

print "\n\nNow show the world you are worth the physical space your body occupies - PUSH TO GITHUB! (`git push origin master`)"

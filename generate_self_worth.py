import datetime
import os
import random
import subprocess

messages = [
  ("My kid's appointment at the pediatrician can wait, I need to get this"
   " commit in."),
  "Sorry honey, I need to keep my streak going - we'll have sex tomorrow!",
  "This commit brought to you by my privilege.",
  "My employer lets me use work time to contribute to open source.",
  "The dog ate my commit."
]

rr = ("Never gonna give you up Never gonna let you down Never gonna run around"
      " and desert you Never gonna make you cry Never gonna say goodbye Never"
      " gonna tell a lie and hurt you")

if not subprocess.check_output('git rev-parse --abbrev-ref HEAD',
                               stderr=subprocess.STDOUT).strip() == 'master':
    raise Exception('Please run this from the master branch.')

print ("Traveling back in time to the founding of Github! (actually, just"
       " a year.)")
start_date = datetime.datetime.now() - datetime.timedelta(days=2)
end_date = datetime.datetime.now() + datetime.timedelta(days=1)

def daterange():
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def main():
    for i, single_date in enumerate(daterange()):
        strPart = rr.split(" ")[i % 34]
        extra = "\n" if i % 34 == 0 else " "
        if i != 0:
            strPart = extra + strPart

        with open("self_worth.txt", "a") as f:
            f.write(strPart)    

        t = ((single_date - datetime.datetime.utcfromtimestamp(0)).total_seconds()
             + 14400 + random.randint(0,57600))
        os.putenv("GIT_COMMITTER_DATE", "{:.2f}".format(float(t)))
        os.putenv("GIT_AUTHOR_DATE", "{:.2f}".format(float(t)))    
        subprocess.call("git add .", stderr=subprocess.STDOUT)
        subprocess.call("git commit -q -m \"" + random.choice(messages) + "\"",
                        stderr=subprocess.STDOUT)
        print ("\r\nProving your worth with commit on " +
               single_date.strftime("%B %d, %Y") + "...")

    print ("\r\nNow show the world you are worth the physical space your body"
           " occupies - PUSH TO GITHUB! (`git push origin master`)")

if __name__=='__main__':
	main()


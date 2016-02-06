import pynotify
import urllib2
import requests
from BeautifulSoup import BeautifulSoup


url = 'http://www.espncricinfo.com/ci/engine/match/index.html?view=live'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

header = soup.find('div', attrs={'class': 'match-section-head'})

print header

#scorecard = soup.find('section',attrs={'class':'default-match-block'})
#print scorecard.prettify()


''' libnotify needs some init value,
it really can be anything, it just uses it
to differentiate between the popups
'''

score = soup.find('section',attrs={'class':'default-match-block '})

print score

print "-----------------------"

pynotify.init("markup")

scoretodisplay=score.text

stringarr=scoretodisplay.split(",")

todisplay=""

score_text_arr = stringarr[2].split(")")

elemcounter = 0

for elem in score_text_arr:
    if elemcounter>0:
        todisplay=todisplay+"\n"+elem+")"
        todisplay=todisplay+"\n"

    todisplay=todisplay+"\n"
    elemcounter=elemcounter+1

mainhead = stringarr[1]

print todisplay
n = pynotify.Notification(mainhead,todisplay+"\t\t")

n.show()

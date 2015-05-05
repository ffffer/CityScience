#match tweets on the same day where there is a fire call
import glob
import json



calls = open("data1.txt")

goodWords = {'electrical', 'drills', 'alarm', 'caught on', 'shots', 'trucks', 'officials', 'on fire', 'call',
    'fighters', 'structure', 'vehicle', 'burning', 'sparking'}
badWords = {'bonfire', 'fireplace', 'campfire', 'Campfire', 'pit', 'be fired', 'get fired',
    'gets fired', 'my', 'firewood', 'fireball', 'fired up', 'firefly', 'sexy firemen', 'fireproof',
        'in the fire', 'just fired', 'just got fired', 'firework', 'flies', 'is fire', 'firewall',
            'be fire', 'got fired', 'backfire', 'Bonfire', 'Crossfire', 'are fire', 'ceasefire',
                'to fire', 'firecracker', 'island', 'fired for', 'bon', 'firee', 'ball','bon fire', 'shots fired'}

callDescs = []
callTimes = []
callDates = []
goodTweets = []
goodTimes = []
count = 0

for line in calls:
    info = line.split(" | ")
    time = str(info[1])+"-"+str(info[2])+"-"+str(info[3])+"-"+str(info[4])+"-"+str(info[5])
    date = str(info[3])+"-"+str(info[2])+"-"+str(info[1])
    callDescs.append(info[0])
    callTimes.append(time)
    callDates.append(date)

for x in range(26,52):
    filepath = "/p/twitter4/rochester/"+str(x)+"-2014/[0-9][0-9]-[0-9][0-9]-2014.json"
    filelist = glob.glob(filepath)
    for filename in filelist:
        name = filename.split("/")
        name2 = name[5].split(".")
        date = name2[0]
        if(date in callDates):
            print date
            file = open(filename)
            for line in file:
                object = json.loads(line)
                #somewhere string matches character sequence 'fire'
                tweet = object['text']
                timeOfTweet = object['datetime retrieved'].split(" ")
                hour = timeOfTweet[1].split(":")[0]
                tweet1 = tweet.lower()
                
                #look for character string 'fire' in a tweet
                if 'fire' in tweet1:
            
                #Append to list of good tweets if no words in badWords and at least one in goodWords is found
                    if not any(word in tweet1 for word in badWords) and any(word in tweet1 for word in goodWords):
                        count+=1
                        #print "\n***IMPORTANT\n"+tweet+"\n"+" Sent at: "+timeOfTweet+"\n"
                        goodTweets.append(tweet)
                        t = timeOfTweet.split(" ")
                        d = t[0].split("-")
                        time = t[1].split(":")
                        tweetTime = str(d[0])+"-"+str(d[1])+"-"+str(d[2])+"-"+str(time[0])+"-"+str(time[1])
                        goodTimes.append(tweetTime);

print count;


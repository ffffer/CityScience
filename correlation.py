# check if there is a correalation between large amount of fire calls to large amount of tweets about fire.

import glob
import json
import datetime

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
callDates1 = []
goodTweets = []
goodTimes = []

#get information about 911 calls
for line in calls:
    info = line.split(" | ")
    time = str(info[1])+"-"+str(info[2])+"-"+str(info[3])+"-"+str(info[4])+"-"+str(info[5])
    date1 = str(info[1])+"-"+str(info[2])+"-"+str(info[3])
    callDescs.append(info[0])
    callTimes.append(time)
    callDates1.append(date1)

#callTimes: sorted nonrepeated call date and time / callDate: reversed call date / callDate1: call date only
ct = list(set(callTimes))
ct.sort()

cd = list(set(callDates1))
cd.sort()

i = 0   #index for calltimes
j = 0   #index for file
filen = range(43,53)
for entry in cd:
    count = 0
    count1 = 0
    #get hours each call at
    hrs = []
    hours2 = []
    while i<len(ct) and entry in ct[i]:
        count1 = count1 + 1
        get = ct[i].split("-")
        hrs.append(get[3])
        i=i+1;
    #print hrs + ["***********"]
    hours1 = list(set(hrs))
    hours1.sort()

    for h in hours1:
        a = range(int(hours1[0])-1,int(hours1[-1])+2)
        hours2 = hours2 + a;
    hours = list(set(hours2))
    hours.sort()


#get the tweet file that match the call date
    l = entry.split("-")
    date = str(l[2])+"-"+str(l[1])+"-"+str(l[0])

    if(datetime.datetime.strptime(entry, "%Y-%m-%d") < datetime.datetime.strptime('2014-10-21', "%Y-%m-%d")):
        continue;
    
    flag = 0;
    while j<len(filen) and ("/p/twitter4/rochester/"+str(filen[j]).zfill(2)+"-2014/"+date+".json" not in glob.glob("/p/twitter4/rochester/"+str(filen[j]).zfill(2)+"-2014/[0-9][0-9]-[0-9][0-9]-2014.json")):
        filelist = glob.glob("/p/twitter4/rochester/"+str(filen[j]).zfill(2)+"-2014/[0-9][0-9]-[0-9][0-9]-2014.json")
        for filename in filelist:
            a = filename.split("/")[5].split(".")[0]
            #if month has passed or in the same month but the day has passed
            if datetime.datetime.strptime(date, "%d-%m-%Y") < datetime.datetime.strptime(a, "%d-%m-%Y"):
                print date
                flag = 1
                break;
        if flag:
            break;
        j=j+1;
    
    if flag:
        continue;
    if(j==len(filen)):
        break
    
    #print "/p/twitter4/rochester/"+str(filen[j]).zfill(2)+"-2014/"+date+".json"
    file = open("/p/twitter4/rochester/"+str(filen[j]).zfill(2)+"-2014/"+date+".json")
    #k = 1
    for line in file:
        try:
            object = json.loads(line)
            tweet = object['text']
            #print str(k) + "----------"
            #k += 1;
            timeOfTweet = object['datetime retrieved']
            ti = timeOfTweet.split(" ")
            ho = ti[1].split(":")
            hour = ho[0]
            tweet1 = tweet.lower()
        
            #get tweet that matches keywords and  matches call time with range of 2 hours
            if 'fire' in tweet1 and int(hour) in hours:
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
        except ValueError:
            print "json object load error";

    print entry + "         " + str(count1) + "              " + str(count);






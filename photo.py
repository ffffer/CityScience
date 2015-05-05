#print all good tweets that contains photo. print them out in tweet, photo, time format.


import glob
import json


goodWords = {'electrical', 'drills', 'alarm', 'caught on', 'shots', 'trucks', 'officials', 'on fire', 'call',
    'fighters', 'structure', 'vehicle', 'burning', 'sparking'}
badWords = {'bonfire', 'fireplace', 'campfire', 'Campfire', 'pit', 'be fired', 'get fired',
    'gets fired', 'my', 'firewood', 'fireball', 'fired up', 'firefly', 'sexy firemen', 'fireproof',
        'in the fire', 'just fired', 'just got fired', 'firework', 'flies', 'is fire', 'firewall',
            'be fire', 'got fired', 'backfire', 'Bonfire', 'Crossfire', 'are fire', 'ceasefire',
                'to fire', 'firecracker', 'island', 'fired for', 'bon', 'firee', 'ball','bon fire', 'shots fired'}

filen = range (26,53)
for num in filen:
    filelist = glob.glob("/p/twitter4/rochester/"+str(num).zfill(2)+"-2014/[0-9][0-9]-[0-9][0-9]-2014.json")
    for name in filelist:
        file = open(name)
        print name
        for line in file:
            try:
                object = json.loads(line)
                tweet = object['text']
                tweet1 = tweet.lower()
                if 'fire' in tweet1 and not any(word in tweet1 for word in badWords) and any(word in tweet1 for word in goodWords):
                    #print "***"
                    if 'entities' in object and 'media' in object['entities'] and 'type' in object['entities']['media'][0] and 'photo' == object['entities']['media'][0]['type']:
                        #print "$$$"
                        url =object['entities']['media'][0]['media_url']
                        print tweet+"\n"+url+"\n"+object['datetime retrieved']+"\n";
            except ValueError:
                print "json object load error";
import re, pprint, sys
import time
import tweepy
from tweepy import StreamListener
import spotipy
import spotipy.util as util
from tweepy import Stream

#token = util.prompt_for_user_token(username="leeu3581", client_id='XXXXXXXXXXXX',client_secret='XXXXXXXXXx',redirect_uri='http://127.0.0.1:8080/callback/q')


auth = tweepy.OAuthHandler('XXXXXXXXXXXXXXX','XXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXXXXXXX','XXXXXXXXXXXXXXXX')

twitter_api = tweepy.API(auth)

results = tweepy.Cursor(twitter_api.search, q="#hashthemusic").items(1)

#, geocode="51.5107,-0.1169,5km"
#print stream.filter(track=['nice'])
#results.replace("#hashthemusic", "")
#for testresult in testresults:
#    print testresult

finalsong = ''
for result in results:
    finalsong = result.text
    finalsong= re.sub('#hashthemusic', '', finalsong)
    print finalsong

    username = 'callooches'
    playlist_id = '2R3CBX8QjXz9ooMzRHrN6I'
    track_ids = '3A4Su2mc2azrtTt9uIVMwRlY'



scope = 'playlist-modify-public'XXXXXXXXXX',client_secret='XXXXXXXXXXX',redirect_uri='http://localhost:8888/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print results
else:
    print "Can't get token for", username

#while True:
#    try:
#      tweet = results.next()
#      finaltweet = tweet.text
#      finaltweet = re.sub('#hashthemusic', '', finaltweet)
#      print(finaltweet.text)

# except tweepy.error.TweepError:
#      print "Twitter rate limit, need to wait 15 min"
#      time.sleep(60 * 16)
#      continue
 # except StopIteration:
    #  break

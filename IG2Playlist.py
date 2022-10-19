import json
import discogs_client
from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
from youtubesearchpython import VideosSearch

## User set values
discog_token = 'YOUR_DISCOG_TOKEN' 
fb_appID = 'YOUR_APP_ID'
fb_appsecret = 'YOUR_APP_SECRET'
fb_appredirect = 'YOUR_APP_REDIRECT_URI'

user_profile = "bipoc_punk" # IG profile to scan
date = "10/18/2022"

num_songs = 1 #edit to set number of songs by artist in playlist
playlist_title = "@"+user_profile+ " " +date

#program wide values
playlist = {}
playlist_id = ''

## Authentification
d = discogs_client.Client('my_user_agent/1.0', user_token=discog_token)
ig = InstagramBasicDisplay(app_id=fb_appID, app_secret=fb_appsecret, redirect_url=fb_appredirect)
print(instagram_basic_display.get_login_url()) # Returns login URL you need to follow



#creates a playlist and stores id of created playlist
def playlist_creator():  
	request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlist_title,
            "description": "This is a playlist based on @"+ user_profile+" artist mentions. This playlist was created with IG2Playlist on "+date,
            "tags": [
              "IG2Playlist",
              "samplePlaylist"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
	)
	response = request.execute()   
	playlist_id = json.load(response)
	playlist_id = playlist_id['id']

# search Discogs for query
def artist_check(query: str):  
	try:
		artist_result = d.search(query, type='artist')
		if artist_result.page(1)[1][0] == query:
			return True
		else:
			return False
	except: 
		pass 

# search Youtube for artist_result, add to playlist
def video_search(artist_result:str,results = num_songs)
	request = youtube.search().list(
        part="snippet",
        maxResults=results,
        q=artist_result
    )
    response = request.execute()
    for i in response.items:
    	item = results.item[i]
    	playlist[item.snippet.title] = item.id.videoId

#input a list of video string, output playlist
def playlist_adder(playlist):
	for video in playlist: 
		request = youtube.playlistItems().insert(
        	part="snippet",body={
          	"snippet": {
            "playlistId": playlist_id,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": playlist[video]
            }
          }
        }
		response = request.execute()   
    )

#working on

# input profile, length to search; output list of string
def ig_crawl(profile = user_profile :str,start = begin_scan: int, end = end_scan:int):  # crawls IG, retrieves results
	if end_scan - begin_scan > 99:
		N = ((end_scan - begin_scan) // 99 ) + 1
	else:
		N = 1
	for i in range(N):
		media = instagram_basic_display.get_user_media(user_id=profile, limit: int = None, before: begin_scan, after: end_scan)
		content = json.loads(media)
		more_media = instagram_basic_display.pagination(media)
		content.update(json.loads(more_media))
	return content

 #input dictionary, output list of strings
def ig_parse(posts = content): # parses IG for actual data
	for i in posts #remove all data except caption
		if i != "caption":
			posts.pop(i)
	return posts

# input list or dictionary, output artist name
def ig_filter(posts = posts)
	for i i



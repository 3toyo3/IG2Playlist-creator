# IG2Playlist - creator
Analyze a instagram profile and create a youtube playlist of mentioned artists from a range of X posts. 
- Being tested with @bipoc_punk
- Uses python, Agile SW development
- Uses [Youtube API](https://developers.google.com/youtube/v3/guides/implementation/playlists), [Discogs API](https://www.discogs.com/developers/#page:home,header:home-faq), and [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api/).

### User Stories: 
- I follow this instagram account and they always posts artists they like. 
- I want to be able to listen to these artists. 
- I want to see all these artists in one place. 
- I want to see even the obscure artists (IE not available on spotify/apple music).

### Design Decisions: 
First, I needed to decide what API to use. I wanted to make sure that there are APIs that are capable of what I want. I decided to use Youtube for the playlist since it has a much bigger collection of music than *Spotify/Apple Music/Tidal* since *Youtube* is available to the public unlike the alternatives which is limited to what artists pay to be available. Looking at the API, I can retrieve captions and well as make a playlist with *Youtube* and *Instagram*. However, *Instagram* doesn't have a way to filter what the caption is saying. I originally planned on using the *Google Natural Language processing API* however, it only identifies artists with a wikipedia page(AKA widely known) OR it can identify music related objects. For the latter, this means in the event that the caption says something about a microphone, the playlist will add a videdo about a microphone, which is not an artist. I decided instead to use *Discogs* for the API since this is a database of many artists, including obscure ones. 

Another decision I made is how big to make the playlist and what kind of response the playlist has. The account I am referencing is 1.5K posts. [1] There is a limit of 5000 videos max in an youtube playlist[2]. However, in order for a playlist to be fully functional, the API says 200 videos. [3] Therefore, I decided to make it so the playlist is a one time sample and creates a playlist of 200 videos max. 

### Tests and Results: 
[results here]

### Final Product: 
[link to playlist here]

### References:
1. As of 10-18-2022
2. https://webapps.stackexchange.com/questions/77790/what-is-the-maximum-youtube-playlist-length
3. https://developers.google.com/youtube/v3/docs/playlists

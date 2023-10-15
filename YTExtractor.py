class YTExtractor:
    def get_channel_stats(youtube, channel_id):
        request = youtube.channels().list(
                part="snippet,contentDetails,statistics",
                id=channel_id
            )
        response = request.execute()

        data =dict(Channel_name = response['items'][0]['snippet']['title'],
                    Subscribers = response['items'][0]['statistics']['subscriberCount'],
                    Views = response['items'][0]['statistics']['viewCount'],
                    Total_videos = response['items'][0]['statistics']['videoCount'],
                    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])

        channel_stats = pd.DataFrame(data, index=[0])
        
        return channel_stats


    def get_video_ids(youtube, playlist_id):
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId = playlist_id,
            maxResults = 50
        )

        response = request.execute()

        video_ids = []

        for i in range(len(response['items'])):
            video_ids.append(response['items'][i]['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        more_pages = True

        while more_pages:
            if next_page_token is None:
            more_pages = False
            else:
            request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId = playlist_id,
            maxResults = 50,
            pageToken = next_page_token
            )
            response = request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token = response.get('nextPageToken')  


        #  return response
        return video_ids 

    def get_all_comments(video_ids):
        # Call the API to get comments  
        all_comments = []  
        for video_id in video_ids:

        try:

            results = youtube.commentThreads().list(  
                part = 'snippet',  
                videoId = video_id,  
                textFormat = 'plainText',  
                ).execute()  
            
            # Loop through each comment and append to comments list  
            while results:  
                for item in results['items']:  
                comment = dict(
                    video_id = item['snippet']['topLevelComment']['snippet']['videoId'],
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay'],
                    author_id = item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    published_date = item['snippet']['topLevelComment']['snippet']['publishedAt'])
                
                all_comments.append(comment)
                
                    
                # Check if there are more comments and continue iterating  
                if 'nextPageToken' in results:  
                    results = youtube.commentThreads().list(  
                        part = 'snippet',  
                        videoId = video_id,  
                        textFormat = 'plainText',  
                        pageToken = results['nextPageToken']  
                    ).execute()  
                else:  
                    break  

        except: 
            continue

        return all_comments
  



# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import googleapiclient.discovery
import pandas as pd

def process_comments(response):
    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        published_date = item['snippet']['topLevelComment']['snippet']['publishedAt']
        comments.append({'comment': comment, 'author': author, 'published_date': published_date})
    return comments

def run_youtube_comments_etl(developer_key,video_id):
    api_service_name = "youtube"
    api_version = "v3"
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = developer_key)

    page_token = None
    comments_list = []
    while True:

        request = youtube.commentThreads().list(
            part="id,snippet,replies",
            order="relevance",
            videoId=video_id,
            maxResults=100,
            pageToken = page_token

        )
        response = request.execute()
        page_token = response.get('nextPageToken')
        comments_list.extend(process_comments(response))

        if page_token is None:
            break

    df = pd.DataFrame(comments_list)
    df.to_csv('s3://irene-airflow-youtube-bucket/youtube_comments.csv', index=False)
    #print(df.head())
    #print(df.tail())

#run_youtube_comments_etl("N5vscPTWKOk")
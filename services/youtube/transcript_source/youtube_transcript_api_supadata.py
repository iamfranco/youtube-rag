from dotenv import load_dotenv

import os
import requests

from services.youtube.models.youtube_transcript import YouTubeTranscriptLine

load_dotenv()

def get_youtube_transcript(video_id: str) -> list[YouTubeTranscriptLine]:
  api_url = f'https://api.supadata.ai/v1/youtube/transcript?videoId={video_id}'
  headers = {'X-API-Key': os.getenv('SUPADATA_API_KEY')}
  print(f'Retrieving YouTube video transcript: {api_url}')
  response = requests.get(api_url, headers=headers)
  response.raise_for_status()
  data = response.json()

  content = data.get('content', [])
  return [YouTubeTranscriptLine(line['text'], line['offset']/1000) for line in content]
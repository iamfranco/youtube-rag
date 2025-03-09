from youtube_transcript_api import YouTubeTranscriptApi

from services.proxy.proxy_service import get_proxy
from services.youtube.models.youtube_transcript import YouTubeTranscriptLine

def get_youtube_transcript(video_id: str) -> list[YouTubeTranscriptLine]:
  max_attempt_number = 5
  for attempt_number in range(max_attempt_number):
    try:
      transcript = _try_get_youtube_transcript(video_id)
      return transcript
    except Exception as e:
      print(f"python youtube_transcript_api failed to download transcript for video id: {video_id} [{attempt_number + 1} / {max_attempt_number}]")
      print(f"error occurred: {e}")

  raise Exception(f"python python youtube_transcript_api failed to download transcript for video id: {video_id}")

def _try_get_youtube_transcript(video_id: str) -> list[YouTubeTranscriptLine]:
  transcript = YouTubeTranscriptApi.get_transcript(
    video_id=video_id,
    languages=['en', 'en-US'],
    proxies=get_proxy()
  )

  return [YouTubeTranscriptLine(line['text'], line['start']) for line in transcript]

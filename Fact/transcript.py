from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse

def extract_transcript(youtube_url):
   
    parsed_url = urlparse.urlparse(youtube_url)
    video_id = urlparse.parse_qs(parsed_url.query).get('v')
    if not video_id:
        print("Invalid YouTube URL.")
        return

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id[0])
        text = ''
        for segment in transcript:
            text += segment['text'] + ' '
        return text, video_id
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    youtube_url = input()
    transcript = extract_transcript(youtube_url)
    if transcript:
        print("Transcript:")
        print(transcript)
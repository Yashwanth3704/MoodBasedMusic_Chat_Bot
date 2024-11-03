import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
nltk.download('vader_lexicon')

def pridictMood(message):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    scores = sentiment_analyzer.polarity_scores(message)
    if scores['compound'] >= 0.5:
        return 'happy'
    elif scores['compound'] <= -0.5:
        return 'sad'
    else:
        return 'neutral'
    
def songpridict(mood):
    song_recomendation = {
            'happy': [
                {"title": "Happy - Pharrell Williams link : https://www.youtube.com/watch?v=ZbZSe6N_BX"},
                {"title": "Can't Stop the Feeling - Justin Timberlake  link : https://www.youtube.com/watch?v=ru0K8uYEZW"}
            ],
            'sad': [
                {"title": "Someone Like You - Adele  link : https://www.youtube.com/watch?v=hLQl3WQQo"},
                {"title": "Let Her Go - Passenger   link : https://www.youtube.com/watch?v=RBumgq5yV"}
            ],
            'neutral': [
                {"title": "Counting Stars - OneRepublic  link : https://www.youtube.com/watch?v=hT_nvWreIhg "},
                {"title": "Wake Me Up - Avicii   link : https://www.youtube.com/watch?v=IcrbM1l_BoI"}
            ]
        }
    song =random.choice(song_recomendation[mood])
    print(song)
    return song

def getSongsuggest(message):
    mood = pridictMood(message)
    song = songpridict(mood)
    return mood , song



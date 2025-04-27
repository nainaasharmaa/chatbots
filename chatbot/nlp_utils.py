import spacy # type: ignore
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(user_input):
    doc = nlp(user_input)
    activities = []
    season = None
    budget = None

    # Extract budget
    match = re.search(r'\d+', user_input)
    if match:
        budget = int(match.group())

    # Extract season
    for token in doc:
        if token.text.lower() in ['spring', 'summer', 'autumn', 'fall', 'winter']:
            season = token.text.lower()

    # Extract activities from keywords (can expand this)
    keywords = ['mountaineering', 'trekking', 'beach', 'surfing', 'adventure', 'sightseeing', 'hiking']
    for token in doc:
        if token.lemma_.lower() in keywords:
            activities.append(token.lemma_.lower())

    return {
        "budget": budget,
        "season": season,
        "activities": activities
    }

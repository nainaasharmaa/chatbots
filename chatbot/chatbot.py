from nlp_utils import extract_entities
import pandas as pd

df = pd.read_csv("TravelPreference (1).csv")
df.columns = df.columns.str.strip()
df['Max Budget'] = df['Max Budget'].replace('[\₹,]', '', regex=True).astype(int)

def get_response(user_input):
    info = extract_entities(user_input)
    budget = info['budget']
    season = info['season']
    activities = info['activities']

    filtered = df.copy()

    if budget:
        filtered = filtered[filtered['Max Budget'] <= budget]

    if season:
        filtered = filtered[
            filtered['Preferred Time of Year']
            .str.lower()
            .str.contains(season, na=False)
        ]

    # Use OR matching for any of the listed activities
    for activity in activities:
        filtered = filtered[
            filtered['Preferred Activities']
            .str.lower()
            .str.contains(activity, na=False)
        ]

    if not filtered.empty:
        return "Suggested destinations:\n" + '\n'.join(filtered['Countries Visited'].tolist())
    else:
        return "Sorry, I couldn't find any destination matching your preferences."

''' My pseudo sentiment analyzer implementation for use with the Flask web app
    in this practice project. THis is Not a real sentiment analyzer but a place
    holder for educational purposes only. '''
import json

def sentiment_analyzer(text_to_analyse):
    response_text = r'{"documentSentiment":{"score":0.98, "label":"SENT_POSITIVE", "mixed":false}}'

    formatted_response = json.loads(response_text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}

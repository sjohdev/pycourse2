''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app :
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Get user text and call sentiment analyzer:
    text_to_analyze = str(request.args.get('textToAnalyze'))
    result_dict = sentiment_analyzer(text_to_analyze)
    label = result_dict['label']
    score = result_dict['score']

    # Make sure output is not invalid:
    if label is None:
        output_str = "Invalid input! Try again."
    else:
        # format output:
        output_str = "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
    return output_str

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

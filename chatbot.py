import nltk, time, re, random
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.chat.util import Chat, reflections

sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

def generate_response(sentiment):
    responses = {
        "positive": ["That's great to hear!", "I'm glad you're feeling positive.", "Tell me more about what's making you feel positive."],
        "negative": ["I'm sorry to hear that. Can I help you with anything?", "I understand it can be tough and you can talk to me.", "Is there anything specific that's bothering you?"],
        "neutral": ["I see. Is there anything on your mind that you'd like to discuss?", "I'm here to chat. What's on your mind today?", "Understood, tell me more about it."]
    }
    return responses[sentiment]

def chatbot():
    introduce = True
    print("Hello! I'm your sentiment analysis chatbot. \nYou can end our conversation anytime by typing 'exit'")
    print("What's your name?")


    more_phrases = [
        [
            r"hi|hello|hey",
            ["Hello!", "Hi there!", "How can I help you today?"]
        ],
        [
            r"what is your name|who are you|how can I call you",
            ["I'm a chatbot.", "You can call me Chatbot."]
        ],
        [
            r"how are you|what's up",
            ["I'm just a computer program, so I don't have feelings, but I'm here to assist you.", "I'm here to help you."]
        ]
    ]
    
    while True:
        if introduce:
            name = input()
            if name.lower() == "exit":
                break
            else:
                print(f"Nice to meet you {name}!")
                introduce = False
    
        user_input = input(name + ": ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            time.sleep(2)
            break
        
        matched = False
        for pattern, responses in more_phrases:
            if re.match(pattern, user_input, re.IGNORECASE):
                print("Chatbot:", random.choice(responses))
                matched = True
                break
        
        if not matched:
            sentiment = analyze_sentiment(user_input)
            response = generate_response(sentiment)

            print(f"Sentiment: {sentiment.capitalize()} - more info: {sid.polarity_scores(user_input)}")
            print(f"Chatbot: {random.choice(response)}")

if __name__ == "__main__":
    chatbot()
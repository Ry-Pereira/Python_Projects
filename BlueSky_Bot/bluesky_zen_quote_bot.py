# bluesky_zen_quote_bot.py
from atproto import Client
# Importing the random module to select random quotes.
from random import *


# A dictionary of Zen quotes categorized by their authors.
zen_quotes = {
    "Buddha" : ["The mind is everything. What you think you become.", "Do not dwell in the past, do not dream of the future", "Peace comes from within. Do not seek it without."],
    "Lao Tzu" : ["The journey of a thousand miles begins with one step.", "When I let go of what I am, I become what I might be."],
    "Confucius" : ["It does not matter how slowly you go as long as you do not stop.", "Our greatest glory is not in never falling, but in rising every time we fall."],
    "Rumi" : ["The wound is the place where the Light enters you.", "Let yourself be silently drawn by the strange pull of what you really love."],
    "Taoist Saying": ["Nature does not hurry, yet everything is accomplished.", "A good traveler has no fixed plans and is not intent on arriving."],
    "Shunryu Suzuki": ["In the beginner's mind there are many possibilities, but in the expert's mind there are few."]
}

# An empty dictionary to hold the quotes that were already posted.
zen_quotes_bin = {
    "Buddha" : [],
    "Lao Tzu" : [],
    "Confucius" : [],
    "Rumi" : [],
    "Taoist Saying": [],
    "Shunryu Suzuki": []
}

# Select a random list of quotes from the dictionary.
zen_quote_to_post = random.choice(list(zen_quotes.values()))




# Example usage of the Atproto Client to post a message.
client = Client()
# Replace 'handle.example.com' and 'hunter2' with actual credentials.
client.login('handle.example.com', 'hunter2')
# Send a simple post.
post = client.send_post('Hello world! I posted this via the Python SDK.')
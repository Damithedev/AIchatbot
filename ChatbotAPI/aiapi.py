def dummy_chatbot_response(message):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you?": "I'm just a bot, but I'm here to assist you! How can I help?",
        "what's your name?": "I'm ChatBot, your virtual assistant.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "bye": "Goodbye! Have a great day!",
    }

    # Default response if the message is not recognized
    default_response = "I'm not sure how to respond to that. Can you please ask something else?"

    # Normalize the message to lower case to make matching case-insensitive
    normalized_message = message.lower()

    # Get the response from the dictionary if available, else use the default response
    return responses.get(normalized_message, default_response)



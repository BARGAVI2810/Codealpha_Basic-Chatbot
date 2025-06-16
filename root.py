def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined greetings and queries.
    The chatbot will continue to interact until the user types 'bye'.
    """
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

    # Start an infinite loop for continuous interaction
    while True:
        user_input = input("You: ").lower() # Get user input and convert to lowercase for easier matching

        # Check for predefined inputs and provide corresponding responses
        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thank you for asking!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break # Exit the loop if the user says 'bye'
        else:
            # Default response for unrecognized input
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase or try 'hello', 'how are you', or 'bye'?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()

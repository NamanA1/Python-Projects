import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for Children Shelter chatbot
pairs = [
    (r"hi|hello|hey", ["Hello! Welcome to Children Shelter, an orphanage in Faridabad. How can I assist you today?", "Hi there! How can I help you support our children?"]),
    (r"(.*)donate(.*)", ["Thank you for your kindness! You can contribute by donating money, books, or food for our children. Would you like more details on how to donate?"]),
    (r"(.*)how can I help(.*)", ["You can help by donating money, books, food, or volunteering your time. Every contribution makes a difference in a child's life."]),
    (r"(.*)volunteer(.*)", ["We appreciate volunteers! You can help by teaching, playing, or organizing activities for the children. Would you like to sign up?"]),
    (r"(.*)location(.*)", ["Children Shelter is based in Faridabad. Would you like directions to visit us?"]),
    (r"(.*)about(.*)children shelter(.*)", ["Children Shelter is an orphanage in Faridabad dedicated to providing love, care, and education to orphaned and underprivileged children."]),
    (r"(.*)visit(.*)", ["You are always welcome to visit! Our visiting hours are from 10 AM to 5 PM. Let us know if you need directions."]),
    (r"(.*)contact(.*)", ["You can reach us at our helpline +91-XXXXXXXXXX or email us at info@childrenshelter.org"]),
    (r"(.*)adopt(.*)", ["We appreciate your interest in adoption. Please visit us for detailed guidance on the adoption process."]),
    (r"(.*)events(.*)", ["We organize events for children's welfare, education, and fun activities. Would you like to participate or sponsor an event?"]),
    (r"(.*)fundraising(.*)", ["We conduct fundraising activities to support the children's needs. Would you like to contribute or organize a fundraiser?"]),
    (r"(.*)sponsor(.*)", ["You can sponsor a child's education, meals, or healthcare. Let us know if you’d like more details."]),
    (r"(.*)facilities(.*)", ["Our facilities include a library, classrooms, dormitories, and a playground for the children."]),
    (r"bye|goodbye", ["Goodbye! Thank you for supporting Children Shelter. Have a wonderful day!"])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response():
    print("Hello! I'm the Children Shelter assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Thank you for your support!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot_response()
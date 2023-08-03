import random

# define a list of greetings
greetings = ["Hello", "Hi", "Hey", "Greetings", "Welcome"]

# define a list of questions the bot can answer
questions = ["What services do you offer?", "What is your address?", "Do you have any available appointments?", "What is the phone number for the hospital?"]

# define a list of possible responses to each question
services_responses = ["We offer a range of medical services including general consultations, surgery, radiology, and emergency care.", "Our hospital provides comprehensive medical services including diagnostic, treatment and surgical services."]
address_responses = ["Our hospital is located at shivaji Nagar Pune.", "Our address is Shivaji Nagar Pune.", "We are located at Shivaji Nagar Pune."]
appointment_responses = ["Yes, we have several available appointments over the next few days.", "I'm sorry, all of our appointments are currently booked.", "We have limited availability for appointments this week."]
doctor_responses = ["Dr. Piyush Rao", "Dr. Samidha Rao"]
phone_responses = ["You can reach our hospital at 555-1234.", "Our phone number is 555-5678.", "Please call us at 555-9012."]

# define a list of goodbye messages
goodbyes = ["Goodbye", "Thanks for chatting", "Take care", "Bye", "Have a nice day"]

# define a function to generate a response to a user's input
def generate_response(user_input):
    # check if the user input is a greeting
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(greetings) + ", how can I assist you today?"

    # check if the user input is a question about services
    for word in user_input.split():
        if word.lower() in ["services", "service", "medical"]:
            return random.choice(services_responses)

    # check if the user input is a question about the hospital's address
    for word in user_input.split():
        if word.lower() in ["address", "location"]:
            return random.choice(address_responses)

    
    # check if the user input is a question about appointment availability
    for word in user_input.split():
        if word.lower() in ["appointments"]:
            return random.choice(appointment_responses)

    for word in user_input.split():
        if word.lower() in ["doctors", "available doctor"]:
            return random.choice(doctor_responses)


    # check if the user input is a question about the hospital's phone number
    for word in user_input.split():
        if word.lower() in ["phone", "number"]:
            return random.choice(phone_responses)

    # if the user input is none of the above, provide a default response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# start the chatbot
print("Welcome to the hospital chatbot. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit", "goodbye"]:
        print(random.choice(goodbyes))
        break
    else:
        response = generate_response(user_input)
        print(response)

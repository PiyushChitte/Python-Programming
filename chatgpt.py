import random

greetings = ["Hello", "Hi", "Hey", "Greetings", "Welcome"]

questions = ["Which bikes are good?", "can you suggest good bikes?"]

bikecompany_responses = ["Honda, Hero, TVS, Suzuki, BMW, Bajaj"]
Honda_responses = ["Shine, SP125, Unicorn, Hornet, Livo"]
Hero_responses = ["Splendor, Glamour, Passion Pro, HF Deluxe"]
TVS_responses = ["Apache, Raider, Sport, Radeon"]
Bajaj_responses = ["Discover125, Pulsar, Platina, CT100"]
Shine_responses = ["Bike Name: Honda Shine, Power: 125 cc, Weight: 100 kg, Overall : Good choice to purchase"]
Splendor_responses = ["Bike Name : Hero Splendor, Power: 110 cc, Weight: 95 kg, Overall : Good choice to purchase"]
apache_responses = ["Bike Name: TVS Apache, Power: 200 cc, Weight: 140 kg, Overall : Good choice to purchase"]
pulsar_responses = ["Bike Name: Bujaj Pulsar, Power: 200 cc, Weight: 125 kg, Overall : Good choice to purchase"]

goodbyes = ["Goodbye", "Thanks for Using Me", "Take Care", "Bye"]

def generate_response(user_input):

    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(greetings) + ", how can I assist you today?"

    for word in user_input.split():
        if word.lower() in ["can you suggest good bikes", "bikes"]:
            return (bikecompany_responses)

    for word in user_input.split():
        if word.lower() in ["honda"]:
            return (Honda_responses)

    for word in user_input.split():
        if word.lower() in ["hero"]:
            return (Hero_responses)

    for word in user_input.split():
        if word.lower() in ["tvs"]:
            return (TVS_responses)

    for word in user_input.split():
        if word.lower() in ["bajaj"]:
            return (Bajaj_responses)

    for word in user_input.split():
        if word.lower() in ["apache"]:
            return (apache_responses)

    for word in user_input.split():
        if word.lower() in ["pulsar"]:
            return (pulsar_responses)

    for word in user_input.split():
        if word.lower() in ["shine"]:
            return (Shine_responses)

    for word in user_input.split():
        if word.lower() in ["splendor"]:
            return (Splendor_responses)


    return "I'm sorry, I don't understand. Can you please rephrase your question?"

print("Welcome to the chatgpt. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit", "goodbye"]:
        print(random.choice(goodbyes))
        break
    else:
        response = generate_response(user_input)
        print(response)


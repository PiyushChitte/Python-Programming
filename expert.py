# Define the knowledge base
knowledge_base = {
    "symptom_1": ["Cough", "Fever"],
    "symptom_2": ["test_3", "test_4"],
    "symptom_3": ["test_5", "test_6"]
}

# Define the inference engine
def recommend_tests(symptoms):
    tests = []
    for symptom in symptoms:
        if symptom in knowledge_base:
            tests += knowledge_base[symptom]
    return tests

# Define the user interface
def get_symptoms():
    symptoms = input("Enter your symptoms, separated by commas: ")
    symptoms = [symptom.strip() for symptom in symptoms.split(",")]
    return symptoms

def show_recommendations(tests):
    if len(tests) == 0:
        print("No tests recommended.")
    else:
        print("Recommended tests:")
        for test in tests:
            print("- " + test)

# Define the main program
def main():
    symptoms = get_symptoms()
    tests = recommend_tests(symptoms)
    show_recommendations(tests)

# Run the program
if __name__ == "__main__":
    main()

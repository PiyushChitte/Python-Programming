knowledge_base = {
    "symptoms": {
        "fever": ["Typhoid", "Malaria", "COVID-19"],
        "cough": ["Common Cold", "Flu", "COVID-19"],
        "shortness of breath": ["Pneumonia", "Asthma", "COVID-19"]
    },
    "diagnosis": {
        "Typhoid": ["Blood test", "Stool test"],
        "Malaria": ["Blood test"],
        "COVID-19": ["PCR test", "Antigen test"],
        "Common Cold": ["Symptomatic treatment"],
        "Flu": ["Symptomatic treatment"],
        "Pneumonia": ["Chest X-ray", "Blood test"],
        "Asthma": ["Spirometry"],
    }
}

def infer_disease(symptoms):
    for symptom, diseases in knowledge_base["symptoms"].items():
        if symptom in symptoms:
            for disease in diseases:
                if all(test in knowledge_base["diagnosis"][disease] for test in required_tests(disease)):
                    return disease
    return "Unknown"

def required_tests(disease):
    return knowledge_base["diagnosis"][disease]


def main():
    print("Welcome to the expert system for hospitals and medical facilities")
    symptoms = input("Please enter the symptoms separated by commas: ").split(",")
    disease = infer_disease(symptoms)
    print(f"The most likely diagnosis is {disease}")

if __name__ == "__main__":
    main()

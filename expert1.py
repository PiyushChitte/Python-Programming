# Define the knowledge base
knowledge_base = {
    'symptom': {
        'fever': ['flu', 'pneumonia'],
        'cough': ['cold', 'flu', 'pneumonia'],
        'fatigue': ['flu', 'pneumonia'],
        'shortness of breath': ['pneumonia']
    },
    'treatment': {
        'flu': 'Rest and fluids',
        'cold': 'Rest and fluids',
        'pneumonia': 'Antibiotics'
    }
}

# Define the inference engine
def diagnose_symptoms(symptoms):
    diseases = set()
    for symptom in symptoms:
        if symptom in knowledge_base['symptom']:
            diseases.update(knowledge_base['symptom'][symptom])
    if not diseases:
        return 'Unknown'
    if len(diseases) == 1:
        return list(diseases)[0]
    return 'Multiple'

def prescribe_treatment(disease):
    if disease in knowledge_base['treatment']:
        return knowledge_base['treatment'][disease]
    return 'Unknown'

# Build the user interface
symptoms = input('Enter your symptoms (separated by commas): ').split(',')
disease = diagnose_symptoms(symptoms)
treatment = prescribe_treatment(disease)

print('Diagnosis: ', disease)
print('Treatment: ', treatment)


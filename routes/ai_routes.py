from flask import Blueprint, render_template, request
from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm
import json
import os

ai = Blueprint('ai', __name__)

# Load model and data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

with open(os.path.join(BASE_DIR, "../symptoms.json")) as f:
    symptoms = json.load(f)

with open(os.path.join(BASE_DIR, "../diagnoses.json")) as f:
    diagnoses = json.load(f)

with open(os.path.join(BASE_DIR, "../doctors.json")) as f:
    doctors = json.load(f)

with open(os.path.join(BASE_DIR, "../hospital_locations.json")) as f:
    hospital_locations = json.load(f)

# Embedding utility
def get_embedding(text):
    return MODEL.encode(text, convert_to_numpy=True)

# Precompute symptom embeddings
symptom_embeddings = {symptom: get_embedding(symptom) for symptom in symptoms}

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Match user symptom to best known condition
def get_best_diagnosis(user_input):
    user_embedding = get_embedding(user_input)
    best_match = None
    best_score = -1

    for symptom, emb in symptom_embeddings.items():
        score = cosine_similarity(user_embedding, emb)
        if score > best_score:
            best_match = symptom
            best_score = score

    diagnoses_list = symptoms.get(best_match, "No diagnosis found")
    return best_match, diagnoses_list

# ✅ GET Route: AI Model Page (blank or initial load)
@ai.route("/ai_model", methods=["GET"])
def ai_model():
    return render_template(
        "ai_model.html",
        diagnosis_result=None,
        doctor_info=None,
        specialist=None,
        hospitals=[]
    )

# ✅ POST Route: Diagnose symptoms and return results
@ai.route("/diagnose", methods=["POST"])
def diagnose():
    diagnosis_result = None
    doctor_display_list = []
    hospitals = []
    specialist = None

    # Get user input
    user_symptoms = request.form["symptoms"]
    matched_symptom, possible_diagnoses = get_best_diagnosis(user_symptoms)
    diagnosis_list = possible_diagnoses.split(", ")
    diagnosis_result = {"symptom": matched_symptom, "diagnoses": diagnosis_list}

    if diagnosis_list[0] != "No diagnosis found":
        diagnosis = diagnosis_list[0]
        specialist = diagnoses.get(diagnosis, "General Physician")

        # Get doctors for the specialist
        raw_doctors = doctors.get(specialist, [])

        for doctor in raw_doctors:
            name = doctor.get("NAME", "Unknown")
            hosp_name = doctor.get("HOSPITAL", "Unknown Hospital")
            address = doctor.get("ADDRESS", "Address not available")

            # Append to the display list
            doctor_display_list.append({
                "name": name,
                "hospital": hosp_name,
                "address": address
            })

            # Append hospital info if available for the map
            if hosp_name in hospital_locations:
                info = hospital_locations[hosp_name]
                hospitals.append({
                    "name": hosp_name,
                    "lat": info["lat"],
                    "lng": info["lng"],
                    "address": info["address"]
                })

    return render_template(
        "ai_model.html",
        diagnosis_result=diagnosis_result,
        doctor_info=doctor_display_list,
        specialist=specialist,
        hospitals=hospitals
    )

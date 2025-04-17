"""
translator.py
This module handles translation functionality for the Travel Translator app.
In a production version, this would connect to real translation APIs.
"""

# For a full implementation, you would integrate with translation APIs like:
# - Google Cloud Translation
# - Azure Translator
# - DeepL API
# - LibreTranslate (open source)

import random

# Supported languages
SUPPORTED_LANGUAGES = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese", 
    "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Hindi", 
    "Thai", "Vietnamese", "Dutch", "Greek", "Turkish"
]

# Sample common phrases by category
COMMON_PHRASES = {
    "Greetings": [
        {"source": "Hello", "target": "", "pronunciation": ""},
        {"source": "Good morning", "target": "", "pronunciation": ""},
        {"source": "Good evening", "target": "", "pronunciation": ""},
        {"source": "Thank you", "target": "", "pronunciation": ""},
        {"source": "You're welcome", "target": "", "pronunciation": ""},
        {"source": "How are you?", "target": "", "pronunciation": ""},
        {"source": "Nice to meet you", "target": "", "pronunciation": ""}
    ],
    "Transportation": [
        {"source": "Where is the bus station?", "target": "", "pronunciation": ""},
        {"source": "How much is a taxi to the airport?", "target": "", "pronunciation": ""},
        {"source": "One ticket, please", "target": "", "pronunciation": ""},
        {"source": "What time does the train depart?", "target": "", "pronunciation": ""},
        {"source": "Is this the right bus for the city center?", "target": "", "pronunciation": ""}
    ],
    "Accommodation": [
        {"source": "I have a reservation", "target": "", "pronunciation": ""},
        {"source": "Do you have any available rooms?", "target": "", "pronunciation": ""},
        {"source": "How much per night?", "target": "", "pronunciation": ""},
        {"source": "Is breakfast included?", "target": "", "pronunciation": ""},
        {"source": "The air conditioning doesn't work", "target": "", "pronunciation": ""}
    ],
    "Dining": [
        {"source": "A table for two, please", "target": "", "pronunciation": ""},
        {"source": "The menu, please", "target": "", "pronunciation": ""},
        {"source": "I'm vegetarian", "target": "", "pronunciation": ""},
        {"source": "I'm allergic to nuts", "target": "", "pronunciation": ""},
        {"source": "The check, please", "target": "", "pronunciation": ""}
    ],
    "Shopping": [
        {"source": "How much does this cost?", "target": "", "pronunciation": ""},
        {"source": "Can I pay by credit card?", "target": "", "pronunciation": ""},
        {"source": "I'm just looking", "target": "", "pronunciation": ""},
        {"source": "Do you have this in a different size?", "target": "", "pronunciation": ""},
        {"source": "That's too expensive", "target": "", "pronunciation": ""}
    ],
    "Emergencies": [
        {"source": "Help!", "target": "", "pronunciation": ""},
        {"source": "I need a doctor", "target": "", "pronunciation": ""},
        {"source": "Call an ambulance, please", "target": "", "pronunciation": ""},
        {"source": "I've lost my passport", "target": "", "pronunciation": ""},
        {"source": "I need to contact my embassy", "target": "", "pronunciation": ""}
    ],
    "Directions": [
        {"source": "Where is the nearest bathroom?", "target": "", "pronunciation": ""},
        {"source": "How do I get to the museum?", "target": "", "pronunciation": ""},
        {"source": "Is it far from here?", "target": "", "pronunciation": ""},
        {"source": "Can you show me on the map?", "target": "", "pronunciation": ""},
        {"source": "I'm lost", "target": "", "pronunciation": ""}
    ],
    "Numbers & Time": [
        {"source": "One, two, three", "target": "", "pronunciation": ""},
        {"source": "What time is it?", "target": "", "pronunciation": ""},
        {"source": "Today, tomorrow, yesterday", "target": "", "pronunciation": ""},
        {"source": "Monday, Tuesday, Wednesday", "target": "", "pronunciation": ""},
        {"source": "How long does it take?", "target": "", "pronunciation": ""}
    ]
}

# Mock translations for demonstration purposes
# In a real implementation, these would be handled by API calls
TRANSLATIONS = {
    "English-Spanish": {
        "Hello": {"text": "Hola", "pronunciation": "OH-lah"},
        "Thank you": {"text": "Gracias", "pronunciation": "GRAH-see-ahs"},
        "Where is the bathroom?": {"text": "¿Dónde está el baño?", "pronunciation": "DON-day es-TAH el BAN-yo"},
        "How much does this cost?": {"text": "¿Cuánto cuesta esto?", "pronunciation": "KWAN-toh KWES-tah ES-toh"},
        "I need help": {"text": "Necesito ayuda", "pronunciation": "neh-seh-SEE-toh ah-YOO-dah"},
    }
}

def get_supported_languages():
    """Return list of supported languages."""
    return SUPPORTED_LANGUAGES

def get_language_index(language):
    """Get index of language in supported languages list."""
    try:
        return SUPPORTED_LANGUAGES.index(language)
    except ValueError:
        return 0  # Default to English

def translate_text(text, source_lang, target_lang):
    """
    Translate text from source language to target language.
    
    In a real implementation, this would call a translation API.
    This mock version just adds some language-specific characters
    and returns a mock pronunciation guide.
    """
    # In a real implementation, call translation API here
    
    # Mock translation for demo purposes
    if source_lang == target_lang:
        return text, "Same pronunciation"
    
    translation_key = f"{source_lang}-{target_lang}"
    if translation_key in TRANSLATIONS and text in TRANSLATIONS[translation_key]:
        return (TRANSLATIONS[translation_key][text]["text"], 
                TRANSLATIONS[translation_key][text]["pronunciation"])
    
    # Generate mock translation if not found in our mock database
    # This is just for demonstration - real implementation would use an API
    if target_lang == "Spanish":
        translation = text + " (en español)"
        pronunciation = "Mock Spanish pronunciation"
    elif target_lang == "French":
        translation = text + " (en français)"
        pronunciation = "Mock French pronunciation"
    elif target_lang == "German":
        translation = text + " (auf Deutsch)"
        pronunciation = "Mock German pronunciation"
    elif target_lang == "Japanese":
        translation = text + " (日本語で)"
        pronunciation = "Mock Japanese pronunciation"
    elif target_lang == "Chinese":
        translation = text + " (用中文)"
        pronunciation = "Mock Chinese pronunciation"
    else:
        translation = text + f" (in {target_lang})"
        pronunciation = f"Mock {target_lang} pronunciation"
    
    return translation, pronunciation

def translate_conversation(text, source_lang, target_lang):
    """
    Translate conversation text and provide a response.
    
    In a real implementation, this might use a more sophisticated
    translation API or model that maintains conversation context.
    """
    # Translate the input text
    translation, pronunciation = translate_text(text, source_lang, target_lang)
    
    # Generate a simple response based on the input
    # In a real implementation, you might use a chatbot API or more sophisticated logic
    if "hello" in text.lower() or "hi" in text.lower():
        response = "Hello! How can I help you today?"
    elif "thank" in text.lower():
        response = "You're welcome! Anything else you need help with?"
    elif "help" in text.lower():
        response = "I'm here to help you communicate during your travels. What do you need assistance with?"
    elif "?" in text:
        response = "That's a good question. Let me help you with that."
    else:
        responses = [
            "I understand. Is there anything specific you'd like to know?",
            "I see. How can I assist you further with your travel needs?",
            "Understood. Would you like translations for any other phrases?",
            "Got it. Is there anything else you'd like to communicate?"
        ]
        response = random.choice(responses)
    
    # Translate the response back to the target language
    translated_response, resp_pronunciation = translate_text(response, "English", target_lang)
    
    return translated_response, resp_pronunciation

def get_common_phrases(category, source_lang, target_lang):
    """Get common phrases for a specific category."""
    phrases = COMMON_PHRASES.get(category, [])
    
    # Translate phrases (in a real implementation, these would be pre-translated or use the API)
    translated_phrases = []
    for phrase in phrases:
        target_text, pronunciation = translate_text(phrase["source"], source_lang, target_lang)
        translated_phrases.append({
            "source": phrase["source"],
            "target": target_text,
            "pronunciation": pronunciation
        })
    
    return translated_phrases

def search_phrases(search_term, source_lang, target_lang):
    """Search for phrases containing the search term."""
    results = []
    search_term = search_term.lower()
    
    # Search through all categories
    for category, phrases in COMMON_PHRASES.items():
        for phrase in phrases:
            if search_term in phrase["source"].lower():
                target_text, pronunciation = translate_text(phrase["source"], source_lang, target_lang)
                results.append({
                    "source": phrase["source"],
                    "target": target_text,
                    "pronunciation": pronunciation
                })
    
    return results
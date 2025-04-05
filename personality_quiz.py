from animals import *

class PersonalityQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "You see someone being bullied. What do you do?",
                "answers": {
                    "a": {"text": "Step in and help immediately", "traits": {"brave": 3, "kind": 2}},
                    "b": {"text": "Go get someone who can help", "traits": {"cautious": 2, "kind": 1}},
                    "c": {"text": "Observe from a distance", "traits": {"timid": 2, "analytical": 1}},
                    "d": {"text": "Walk away, it's not your problem", "traits": {"cold": 2, "independent": 1}}
                }
            },
            {
                "question": "Your friend is having trouble reaching a high shelf. What do you do?",
                "answers": {
                    "a": {"text": "Immediately offer to help", "traits": {"helpful": 2, "kind": 1}},
                    "b": {"text": "Wait to see if they ask for help", "traits": {"patient": 2, "considerate": 1}},
                    "c": {"text": "Suggest a different solution", "traits": {"clever": 2, "analytical": 1}},
                    "d": {"text": "Watch them figure it out themselves", "traits": {"independent": 2, "observant": 1}}
                }
            },
            {
                "question": "You find a lost item. What do you do?",
                "answers": {
                    "a": {"text": "Search for the owner right away", "traits": {"responsible": 2, "kind": 1}},
                    "b": {"text": "Turn it in to lost and found", "traits": {"lawful": 2, "trustworthy": 1}},
                    "c": {"text": "Leave it where you found it", "traits": {"cautious": 2, "neutral": 1}},
                    "d": {"text": "Keep it for yourself", "traits": {"opportunistic": 2, "selfish": 1}}
                }
            },
            {
                "question": "How do you prefer to solve problems?",
                "answers": {
                    "a": {"text": "Head-on with force", "traits": {"brave": 2, "direct": 1}},
                    "b": {"text": "Carefully plan everything", "traits": {"analytical": 2, "cautious": 1}},
                    "c": {"text": "Work with others", "traits": {"cooperative": 2, "social": 1}},
                    "d": {"text": "Find creative solutions", "traits": {"clever": 2, "adaptable": 1}}
                }
            },
            {
                "question": "What's your ideal way to spend free time?",
                "answers": {
                    "a": {"text": "Physical activities", "traits": {"energetic": 2, "active": 1}},
                    "b": {"text": "Reading or studying", "traits": {"intelligent": 2, "curious": 1}},
                    "c": {"text": "Hanging with friends", "traits": {"social": 2, "friendly": 1}},
                    "d": {"text": "Relaxing alone", "traits": {"calm": 2, "independent": 1}}
                }
            },
            {
                "question": "You see food you really want, but it belongs to someone else. What do you do?",
                "answers": {
                    "a": {"text": "Ask if you can have some", "traits": {"honest": 2, "polite": 1}},
                    "b": {"text": "Ignore it completely", "traits": {"disciplined": 2, "respectful": 1}},
                    "c": {"text": "Take just a tiny bit", "traits": {"mischievous": 2, "impulsive": 1}},
                    "d": {"text": "Find your own food", "traits": {"independent": 2, "resourceful": 1}}
                }
            },
            {
                "question": "How do you handle dangerous situations?",
                "answers": {
                    "a": {"text": "Face them head-on", "traits": {"brave": 3, "confident": 1}},
                    "b": {"text": "Proceed with caution", "traits": {"careful": 2, "analytical": 1}},
                    "c": {"text": "Run away", "traits": {"cautious": 2, "survival-focused": 1}},
                    "d": {"text": "Freeze in place", "traits": {"timid": 2, "nervous": 1}}
                }
            },
            {
                "question": "What's most important to you?",
                "answers": {
                    "a": {"text": "Strength and power", "traits": {"ambitious": 2, "powerful": 1}},
                    "b": {"text": "Knowledge and wisdom", "traits": {"intelligent": 2, "wise": 1}},
                    "c": {"text": "Friends and family", "traits": {"loyal": 2, "caring": 1}},
                    "d": {"text": "Peace and harmony", "traits": {"peaceful": 2, "balanced": 1}}
                }
            }
        ]
        self.trait_to_animal_mapping = {
            "brave": ["Lion", "Wolf", "Eagle"],
            "kind": ["Deer", "Rabbit", "Robin"],
            "intelligent": ["Gorilla", "Chimpanzee", "Velociraptor"],
            "cautious": ["Mouse", "Rabbit", "Deer"],
            "powerful": ["Bear", "Tiger", "Lion"],
            "social": ["Wolf", "Chimpanzee", "Penguin"],
            "independent": ["Tiger", "Leopard", "Eagle"],
            "clever": ["Fox", "Raccoon", "Crow"],
            "peaceful": ["Deer", "Koala", "Giant Panda"],
            "energetic": ["Cheetah", "Squirrel", "Hare"]
        }
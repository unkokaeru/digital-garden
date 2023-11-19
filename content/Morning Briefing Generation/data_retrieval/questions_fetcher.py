"""Contains functions for retrieving questions from the database."""
import random
from utils.logger import get_logger


def get_driving_questions(num: int = 3) -> str:
    """
    Get a list of questions to ask myself each day.

    :param num: The number of questions to return.
    :return: A string containing the questions.
    """

    logger = get_logger()  # Initialize the logger
    questions_string = ""

    logger.info("Starting to get driving questions.")

    questions = [
        "What should you do at a stop sign?",
        "How do you perform an emergency stop?",
        "What are the rules for overtaking?",
        "How should you react to a flashing amber traffic light at a pedestrian crossing?",
        "What does a double white line in the middle of the road mean?",
        "How do you identify a zebra crossing at night?",
        "What should you do when approaching a roundabout?",
        "What is the national speed limit on a single carriageway road?",
        "How should you check your blind spot?",
        "What does an amber traffic light mean?",
        "How would you check your brakes are working before starting a journey?",
        "What's the correct way to use anti-lock brakes in an emergency?",
        "What should you do when the ABS light stays on?",
        "How should you adjust your headrest to reduce the risk of neck injury?",
        "What does the law say about using a mobile phone while driving?",
        "What's the minimum tread depth for car tyres in the UK?",
        "What should you do if you're feeling tired while driving?",
        "How can you reduce fuel consumption while driving?",
        "What should you do if you encounter an ambulance with flashing lights?",
        "When can you overtake on the left?",
        "What is the two-second rule?",
        "How should you react to an oncoming vehicle on a narrow road?",
        "What do the colors of the cat's eyes on the motorway indicate?",
        "What does a solid white line at the side of the road indicate?",
        "What should you do if your vehicle breaks down on the motorway?",
        "What's the purpose of the hard shoulder on a motorway?",
        "What does it mean if you see red flashing lights at a railway crossing?",
        "How should you respond to a school crossing patrol sign?",
        "What is aquaplaning and how do you correct it?",
        "What are the rules regarding horn usage in built-up areas at night?",
        "How should you react to a flashing blue light without a siren?",
        "What does a red and white triangular sign indicate?",
        "How do you signal your intentions to other drivers at a roundabout?",
        "What's the procedure for overtaking a cyclist?",
        "How do you check for underinflated tyres?",
        "What does a green arrow showing with a red light mean at a traffic light?",
        "How should you park on a hill with and without a curb?",
        "What's the legal limit for alcohol consumption before driving?",
        "How do you respond to a 'Low Fuel' warning light?",
        "What does a flashing green light on a traffic signal mean?",
        "When should you use your car's fog lights?",
        "How do you deal with a skid?",
        "What's the importance of a catalytic converter?",
        "What are the rules for using a bus lane?",
        "How should you adjust your mirrors correctly?",
        "What does the brake system warning light indicate?",
        "What's the procedure for towing another vehicle?",
        "How should you behave in a contraflow system?",
        "What's the purpose of a diverging diamond interchange?",
        "How do you deal with aggressive drivers on the road?",
    ]

    daily_questions = random.sample(questions, num)
    logger.info(f"Selected {len(daily_questions)} questions randomly for the day.")

    for i, question in enumerate(daily_questions, 1):
        questions_string += f"{i}. {question}\n"

    logger.info("Completed formatting the selected driving questions.")
    return questions_string

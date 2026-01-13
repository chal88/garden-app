"""
Gardening Advice Application
This version refactors the logic into functions and uses dictionaries
to store advice for better readability and maintainability.
"""

# Dictionary storing advice based on season
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Prepare the soil and start planting.",
    "autumn": "Reduce watering and prepare plants for colder weather."
}

# Dictionary storing advice based on plant type
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "tree": "Prune dead branches to encourage healthy growth."
}


def get_gardening_advice(season, plant_type):
    """
    Returns gardening advice based on the season and plant type.
    """
    advice = ""

    advice += SEASON_ADVICE.get(
        season, "No advice available for this season."
    ) + "\n"

    advice += PLANT_ADVICE.get(
        plant_type, "No advice available for this type of plant."
    )

    return advice


def main():
    """Main program execution."""
    season = input("Enter the season (summer, winter, spring, autumn): ").lower()
    plant_type = input("Enter the plant type (flower, vegetable, tree): ").lower()

    advice = get_gardening_advice(season, plant_type)

    print("\nGardening Advice:")
    print(advice)


# Run the program
if __name__ == "__main__":
    main()


from IPython.display import HTML

# Minimal Python ReAct Agent
# Kerala Restaurant Finder Tool
# Google Colab Ready

# --------------------------------
# TOOL DEFINITIONS
# --------------------------------

def restaurant_finder(district):
    """
    Restaurant finder tool using Kerala district data
    """

    restaurants = {
        "thiruvananthapuram": "Zam Zam Restaurant",
        "kollam": "Ramees Restaurant",
        "pathanamthitta": "Hotel Aaryaas",
        "alappuzha": "Brothers Hotel",
        "kottayam": "Theos Food Factory",
        "idukki": "Hotel Sri Krishna",
        "ernakulam": "Grand Pavilion",
        "thrissur": "Pathans Restaurant",
        "palakkad": "Noorjahan Hotel",
        "malappuram": "Salkara Restaurant",
        "kozhikode": "Paragon Restaurant",
        "wayanad": "1980's A Nostalgic Restaurant",
        "kannur": "MVK Restaurant",
        "kasaragod": "Food Land Restaurant"
    }

    return restaurants.get(
        district.lower(),
        "No restaurant found for this district"
    )


# --------------------------------
# REACT AGENT
# --------------------------------

def react_agent(user_query):

    print(f"\nUSER: {user_query}\n")

    # Thought
    print("Thought: I should identify the Kerala district and use the restaurant finder tool.\n")

    # Extract district
    district = user_query.strip()

    # Action
    print("Action: Restaurant_Finder")
    print(f"Action Input: {district}\n")

    # Tool Call
    result = restaurant_finder(district)

    # Observation
    print(f"Observation: {result}\n")

    # Final Answer
    print("Final Answer:")
    display(HTML(f"""
        <div style="background-color: #f0f0f0; padding: 15px; border-radius: 8px; border: 1px solid #ccc;">
            <h3 style="color: #333;">Restaurant Recommendation</h3>
            <p style="font-size: 16px;">A popular restaurant in <strong>{district.title()}</strong> is <span style="color: #007bff; font-weight: bold;">{result}</span>.</p>
        </div>
    """))


# --------------------------------
# RUN AGENT
# --------------------------------

district_name = input("Enter the district name: ")

react_agent(district_name)

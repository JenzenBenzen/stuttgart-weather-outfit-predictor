# Outfit recommendation based on temperature ranges

def outfit_recommendation(temp_celsius):
    """
    Returns a clothing recommendation based on the input temperature in Celsius.
    """
    if temp_celsius >= 22:
        return "T-Shirt"
    elif 16 <= temp_celsius < 22:
        return "T-Shirt + Pullover"
    else:
        return "T-Shirt + Jacket"

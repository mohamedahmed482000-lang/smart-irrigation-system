def irrigation_decision(moisture):
    if moisture < 30:
        return "🚰 Irrigate Now"
    elif moisture < 50:
        return "🤔 Monitor"
    else:
        return "❌ No Irrigation"


def irrigation_duration(moisture, temperature):
    if moisture < 20:
        return 30
    elif moisture < 30:
        return 20
    elif temperature > 35:
        return 15
    else:
        return 0
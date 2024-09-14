import json
import numpy as np

def compare_classification(user_data: str, ml_data: dict) -> str:
    # Parse the JSON strings into dictionaries
    user_data = json.loads(user_data)
    
    # Extract user and ML results from the dictionaries
    user_results = [int(user_data[key]) for key in ml_data]
    ml_results = [int(ml_data[key]) for key in ml_data]

    # Compute user performance based on comparison of user and ml results
    user_performance = np.array([
        1 if user_results[i] == ml_results[i] else 0 
        for i in range(len(ml_results))
    ])

    user_accuracy = np.mean(user_performance)

    # Convert ml_results directly into an array for accuracy comparison
    ml_performance = np.array(ml_results)
    network_accuracy = np.mean(ml_performance)

    if network_accuracy > user_accuracy:
        diff = (network_accuracy - user_accuracy) * 100
        return f"The neural network beat you by {diff:.2f}%."
    elif network_accuracy == user_accuracy:
        return "You tied with the neural network."
    else:
        diff = (user_accuracy - network_accuracy) * 100
        return f"You beat the neural network by {diff:.2f}%."


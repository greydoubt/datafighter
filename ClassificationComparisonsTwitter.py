import numpy as np

def compare_classification(user_data, ml_data, ground_truths):
    
    #user comparisons    
    userPerformance = np.array([])
    
    for i in np.arange(len(user_data)):
        if user_data[i] == ground_truths[i]:
            userPerformance = np.append(userPerformance, 1)
        else:
            userPerformance = np.append(userPerformance, 0)
            
    userAccuracy = np.count_nonzero(userPerformance == 1)/userPerformance.shape[0]
    
    
    #ml comparisons
    networkPerformance = np.array([])
    
    for i in np.arange(len(ml_data)):
        if ml_data[i] == ground_truths[i]:
            networkPerformance = np.append(networkPerformance, 1)
        else:
            networkPerformance = np.append(userPerformance, 0)
    
    networkAccuracy = np.count_nonzero(networkPerformance == 1)/networkPerformance.shape[0]
    
    if networkAccuracy > userAccuracy:
        diff = 100*(networkAccuracy-userAccuracy)
        diff = str(diff)
        string = "The neural network beat you by " + diff + "%."
        return string
    elif networkAccuracy == userAccuracy:
        string = "You tied with the neural network."
        return string
    elif networkAccuracy < userAccuracy:
        diff = 100*(userAccuracy-networkAccuracy)
        diff = str(diff)
        string = "You beat the neural network by " + diff + "%."
        return string
    
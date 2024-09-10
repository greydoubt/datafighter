import json
import numpy as np

def compare_classification(user_data, ml_data):
    
    userData = json.loads(list)
    mlData = json.load(dict)
    
    userResults = []
    mlResults = []
    
    i = 0
    for key in mlData:
        userClass = int(userData[i])
        mlClass = int(mlData[key])
        
        userResults.append(userClass)
        mlResults.append(mlClass)
        i=i+1
        
    userPerformance = np.array([])
    
    for i in np.arange(len(mlResults)):
        if (mlResults[i] == 0) and (userResults[i] == 0):
            userPerformance = np.append(userPerformance, 0)
        elif (mlResults[i] == 0) and (userResults[i] == 1):
            userPerformance = np.append(userPerformance, 1)
        elif (mlResults[i] == 1) and (userResults[i] == 0):
            userPerformance = np.append(userPerformance, 0)
        elif (mlResults[i] == 1) and (userResults[i] == 1):
            userPerformance = np.append(userPerformance, 1)
            
    userAccuracy = np.count_nonzero(userPerformance == 1)/userPerformance.shape[0]
    
    networkPerformance = np.array([mlData])
    
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
        
    
        
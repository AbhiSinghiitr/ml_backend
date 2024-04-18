from voice_preprocess import calculate_mfccs
import numpy as np
from joblib import load
import os

emotion = np.array(["angry", "anxious", "apologetic", "assertive", "concerned", "encouraging", "excited", "happy", "neutral","sad"])

model_path = './classifier/rf.joblib'


rf_model1 = load(model_path, mmap_mode='r')



# def get_prob_class(spath):
#     feat, mx = calculate_mfccs(spath)
#     arp = np.array(feat)
#     arp = arp.reshape(1, 12)
#     probabilities = rf_model1.predict_proba(arp)
    
#     # Assuming emotion is a list of class labels, replace it with your actual class labels if needed
#     classes = [emotion[i] for i in range(len(emotion))]
    
#     # Create a dictionary to store class probabilities
#     class_probabilities = dict(zip(classes, probabilities[0]))
    
#     return class_probabilities


def get_voice_class(spath):
    feat,mx=calculate_mfccs(spath)
    arp=np.array(feat)
    arp=arp.reshape(1,12)
    lb=rf_model1.predict(arp)
    probabilities = rf_model1.predict_proba(arp)
    
    classes = [emotion[i] for i in range(len(emotion))]
    class_probabilities = dict(zip(classes, probabilities[0]))
    cl=emotion[int(lb[0])]
    
    obj={
        "class": cl,
        "prob" : class_probabilities
    }
    
    return obj

def get_class(aud):
    ex=get_voice_class(aud)
    return ex


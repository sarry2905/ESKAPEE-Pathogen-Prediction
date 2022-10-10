import glob
import os
import pickle
import time
import pandas as pd



def e_ne_prediction(tsX):
    """
    This function takes the generated kmer features as input and predicts whether it
    belongs to ESKAPEE or NON ESKAPEE Category.
    type data: dataframe
    :rtype: pred_cls contains the name of the predicted class
    """
    # model_dir contains the trained models.
    models = glob.glob(model_dir) 
    

    cls_lb = ['Enterococcus faecium', 'Staphylococcus aureus', 'Klebsiella pneumoniae', 'Acinetobacter baumannii',
               'Pseudomonas aeruginosa', 'Enterobacter', 'Escherichia coli', 'Non ESKAPE']

    pred_df = pd.DataFrame()
    
    for mod in models:
        model = pickle.load(open(mod, "rb"))
        predY_temp = model.predict(tsX)
        name = os.path.splitext(os.path.basename(mod))[0]
        pred_df[name] = predY_temp
        
    pred = pred_df.mode(axis=1).iloc[:, 0].values.tolist()[0]
    pred_cls = cls_lb[pred-1]

    return pred_cls

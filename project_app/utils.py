
import numpy as np
import pickle
import json

try:
    import config
except:
    pass



class medical():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region
    def load_model(self):
        try:
            
            with open(config.MODEL_FILE_PATH,"rb") as f:
                self.model=pickle.load(f)
                
            with open(config.JSON_FILE_PATH,"r") as m:
                self.data=json.load(m)
         
        except:
            
            with open ('Medical.pkl','rb') as f:
                self.model=pickle.load(f)
   
            with open ('data.json','r') as m:
                self.data=json.load(m)
   
    def get_predicted(self):

        self.load_model()
        region_index=self.data['columns'].index(self.region)

        array=np.zeros(len(self.data['columns']))
        array[0]=self.age
        array[1]=self.data['sex'].get(self.sex)
        array[2]=self.bmi
        array[3]=self.children
        array[4]=self.data['smoker'].get(self.smoker)
        array[region_index]=1

        print('test_array',array)
        prediction=np.around(self.model.predict([array])[0],3)
        print(prediction)
        return prediction
if __name__=="__main__":
    age=24
    sex="male"
    bmi=27
    children=5
    smoker="yes"
    region="northeast"
    med=medical(age,sex,bmi,children,smoker,region)
    med.get_predicted()

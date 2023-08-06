#from rasa.nlu.model import Interpreter #Comented by Pravin K on 26-APR-21  [to avoide rasa installation issue] 
import json
import glob
import os
import loggerutility as logger

class Rasa_id_interpreter:
    
    # def __init__(self):
    #     logger.log("init Rasa_id_interpreter ","0")

    @staticmethod
    def get_model_path(enterprise, modelScope, modelType, modelName):
        if modelScope=="" and modelType=="" and modelName=="":
        logger.log(f"In get_model_path.[{enterprise}]pwd= {os.getcwd()}","0")
            logger.log(f"predictor_rasa modelPath \n enterprise- {enterprise} modelScope- {modelScope}, modelType- {modelType}, modelName- {modelName} ","0")
            modelScope = "enterprise"
            enterprise = "enterprise1"
            modelType  = "product_identification"
            modelName  = "rasa_trained_model"

        logger.log(f"enterprise::{enterprise}, modelScope::{modelScope}, modelType::{modelType}, modelName::{modelName}","0")    
        # list_of_files = glob.glob("/proteus-sense/trained_model/"+ modelType +  "/" +modelScope + "/" + enterprise + "/"+ modelName+"/models/*.tar.gz")    # Added by SwapnilB on [ 29-Dec-22 ] for loading model stored on new location
        list_of_files1 = glob.glob("/proteus-sense/trained_model/"+ modelType +  "/" +modelScope + "/" + enterprise + "/"+ modelName+"/models/*.tar.gz")    # Added by SwapnilB on [ 12-Jan-22 ] 
        logger.log(f"list_of_files1 [{list_of_files1}]","0")
        latest_file = max(list_of_files1, key=os.path.getctime)
        rasa_model_path = latest_file+"/nlu"
        return rasa_model_path

    @staticmethod
    def rasa_output(text,attr_count,enterprise,modelScope, modelType, modelName):   #Added by SwapnilB
    # def rasa_output(self,text,attr_count,modelName):  
        logger.log(f"In rasa_output text:{text}","0")
        from rasa.nlu.model import Interpreter  #Added by Pravin K on 26-APR-21 [to avoide rasa installation issue]
        res=[]
        rasa_model_path = Rasa_id_interpreter.get_model_path(enterprise,modelScope, modelType, modelName)
        
        interpreter = Interpreter.load(rasa_model_path)
        logger.log(f"In rasa_output interpreter:{interpreter}","0")
        for t in range(len(text)):
            result = interpreter.parse(text[t])
            entities = result['entities']
            entity_dict = {}
            for j in range(attr_count):
                attr_name = 'attr' + str(j + 1)
                for i in range(len(entities)):
                    if entities[i]['entity'] == attr_name and entities[i]['extractor'] == 'DIETClassifier' and entities[i]['confidence_entity'] >= 0.90:
                        entity_dict[attr_name] = entities[i]['value']
            res.append(entity_dict)
        return res

    @staticmethod
    def extract_entities(products,attr_count,enterprise, modelScope, modelType, modelName):  #Added by SwapnilB 
    # def extract_entities(self,products,attr_count,modelName):  
        # logger.log(f"In extract_entities[{products}]attr_count[{attr_count}],enterprise[{modelName}]","0")
        result = []
        entities_extracted = Rasa_id_interpreter.rasa_output(products,attr_count,enterprise,modelScope, modelType, modelName)
        # entities_extracted = self.rasa_output(self,products,attr_count,modelName)   # Added by SwapnilB
        for i in range(len(entities_extracted)):
            attr_list = []
            for j in range(attr_count):
                attr_key = 'attr' + str(j+1)
                attr_list.append(entities_extracted[i].get(attr_key,0))
            text=''
            result_dict={}
            for k in range(len(attr_list)):
                if attr_list[k]!=0:
                    key='attr'+ str(k+1)
                    result_dict[key] = attr_list[k]
            result_dict['descr'] = products[i]
            result_dict['id'] = i+1
            result.append(result_dict)
        return result

    # extract_entities( ["Augmentin 375mg Intravenous"],attr_count=3)
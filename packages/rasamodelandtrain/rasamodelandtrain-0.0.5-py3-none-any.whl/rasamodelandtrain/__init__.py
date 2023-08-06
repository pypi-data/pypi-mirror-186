from .rasa_id_interpreter import Rasa_id_interpreter
import subprocess, glob, os, shutil, tarfile, json,jsonify
import loggerutility as logger

    ##### Create new rasa directory #####
class Rasa:


    @staticmethod
    def init_rasa(enterprise, modelScope, modelType, modelName):
        if modelScope=="global":
            if  not os.path.exists("/proteus-sense/trained_model/" +  modelType +  "/" + modelScope +  "/"+ modelName):
                os.makedirs("/proteus-sense/trained_model/" +  modelType + "/" + modelScope + "/" + modelName) 
                return True   

        else:
            if  not os.path.exists("/proteus-sense/trained_model/" + modelType + "/" + modelScope + "/" + enterprise + "/"+ modelName):
                os.makedirs("/proteus-sense/trained_model/" + modelType + "/" + modelScope + "/" + enterprise + "/"+  modelName)
                return True


    ##### Train API #####
    @staticmethod
    def create_model(enterprise, mode,  parsed_json, modelScope, modelName, modelType):
        # Added By SwapnilB for calling from trainemodel api on [29-Dec-22] START 
        logger.log(f"In train_rasa mode[{mode}{type(mode)}]enterprise[{enterprise}{type(enterprise)}]","0")
        logger.log(f"In train_rasa modelName[{modelName}][{type(modelName)}]","0" )
        logger.log(f"In train_rasa modelType[{modelType}][{type(modelType)}]","0" )
        logger.log(f"In train_rasa parsed_json[{parsed_json}][{type(parsed_json)}]","0" )
        
        rasaFolderStructure = Rasa.init_rasa(enterprise, modelScope, modelType, modelName)                                                              #  Added by SwapnilB [26-Dec-22] 
        if rasaFolderStructure :
            logger.log(f"rasaFolderStructure created.","0")
        
        if mode=='init': # init for first training with new data passed
            data = parsed_json
            
            logger.log(f"train_model init: data [{data}]","0") 
            data = json.dumps(data).encode('utf-8')           
            logger.log(f"train_model init: data after byte conversion [{data}]","0") 
            data = eval(data)
            logger.log(f"train_model init: data [{data}]","0") 

            converted_data = Rasa.format_rasa_data(data) #Convert to rasa format
            logger.log(f"train_rasa:: converted_data::{converted_data}","0")
            
            Rasa.export_train_data(converted_data, modelScope, enterprise, modelType, modelName) #Store file in data directory   # file gets created Dec-26
        
        elif mode=='add': # update to update existing data. Data passed
            logger.log(f"train_rasa add.","0")
            # data = request.get_data()
            data = eval(data)
            logger.log(f"train_model add: data [{data}]","0") 
        if type(data)==list:
        
            logger.log(f"train_model init:object: data [{data}]", "0")
            newArr = {}
            prods = []
            id = 1
            for obj in data :
                descr = obj["descr"]         #  Added by SwapnilB [23-Dec-22]    #### columnName
                # descr = obj["text"]
                descArr = descr.split()
                i=1
                prod = {"id":"I"+str(id),"descr":descr}
                for txt in descArr:
                    prod["attr"+str(i)]= txt 
                    i = i+1
                
                prod["no_of_attr"] = len(descArr)
                prods.append(prod)
                id= id+1
                
            newArr["product_data"] = prods
            logger.log(f"\n\ndata after Process:{newArr}","0")
            logger.log(f"\n\n","0")

            Rasa.modify_train_data(newArr,modelScope, enterprise, modelType, modelName)
        else:
            logger.log(f"train_model with product_data ","0")
            Rasa.modify_train_data(data, modelScope, enterprise, modelType, modelName)

        if modelScope=="global":
            command = "rasa train --data /proteus-sense/trained_model/"+ modelType +"/" + modelScope + "/" + modelName +"/nlu.json --out /proteus-sense/trained_model/"+ modelType + "/"+ modelScope+ "/"  + modelName
        else:
            command = "rasa train --data /proteus-sense/trained_model/"+modelType +"/" + modelScope + "/" +enterprise+ "/" + modelName +"/nlu.json --out /proteus-sense/trained_model/"+ modelType + "/" + modelScope + "/" + enterprise+ "/" + modelName
        os.system(command)
        export_modelResult = Rasa.export_model(modelScope, enterprise, modelType, modelName)
        if export_modelResult:
            logger.log("Model metadata file extracted.","0")
        return "Model Created"
        # Added By SwapnilB for calling from trainemodel api on [29-Dec-22] END
    
    @staticmethod
    def export_model(modelScope, enterprise, modelType, modelName):  # Added By SwapnilB for calling from trainemodel api on [29-Dec-22] 
        logger.log(f"export_model::enterprise[{enterprise}]","0")
        file_path= "/proteus-sense/trained_model/"+ modelType +"/"+modelScope+ "/" +enterprise+ "/" + modelName  # Added By SwapnilB for calling from trainemodel api on [29-Dec-22] 
        list_of_files = glob.glob(file_path+'/*.tar.gz')  # * means all if need specific format then *.csv
        logger.log(f"export_model::enterprise[{list_of_files}]","0")
        latest_file = max(list_of_files, key=os.path.getctime)
        logger.log(f"latest: {latest_file}","0")
        latest_file_name = latest_file.split(file_path)[1]
        my_tar = tarfile.open(latest_file)
        my_tar.extractall(file_path+"/models/"+latest_file_name)  # specify which folder to extract to
        my_tar.close()
        return True

    @staticmethod
    def convert_data(data):
        result = []
        for i in range(len(data)):
            numb_of_attr = int(data[i].get("no_of_attr"))
            attr=[]
            for j in range(numb_of_attr):
                attr_key = 'attr'+ str(j+1) #attr1,attr2,attr3..
                attr.append(data[i].get(attr_key, 0))
            text = data[i].get('descr', 0)
            rasa_dict = {}
            rasa_dict['text'] = text
            rasa_dict['intent'] = data[i].get("id", 0)
            rasa_dict['entities'] = []
            for value in range(len(attr)):
                if attr[value] !=0:
                    attr_key = 'attr'+ str(value+1)
                    attr_start = text.find(attr[value])
                    attr_end = attr_start + len(attr[value])
                    rasa_dict['entities'].append(
                        {"entity": attr_key, "start": attr_start, "end": attr_end, "value": attr[value]})
            result.append(rasa_dict)

        logger.log(f"convert_data::result:{result}","0")
        return result
    @staticmethod
    def format_rasa_data(data):
        converted_dict={}
        result = Rasa.convert_data(data)
        converted_dict['rasa_nlu_data']={}
        converted_dict['rasa_nlu_data']['common_examples']=result
        converted_dict['rasa_nlu_data']['entity_synonyms']=[]
        logger.log(f"format_rasa_data::format_rasa_data:{converted_dict}","0")
        return converted_dict

    @staticmethod
    def export_train_data(converted_data, modelScope, enterprise, modelType, modelName):       # Added by SwapnilB for trainemodel api [29-Dec-22]
        logger.log(f"export_train_data::converted_data[{converted_data}]enterprise[{enterprise}]","0") 
        os.system("pwd")
        if modelScope=="global":
            with open("/proteus-sense/trained_model/"+ modelType +"/"+ modelScope + "/" + modelName + "/nlu.json", "w") as outfile:
                json.dump(converted_data, outfile)
        else:    
            with open("/proteus-sense/trained_model/"+ modelType +"/" + modelScope + "/" +enterprise+"/" + modelName + "/nlu.json", "w") as outfile:
                json.dump(converted_data, outfile)


    @staticmethod
    def modify_train_data(new_data, modelScope, enterprise, modelType, modelName):    # Added by SwapnilB for trainemodel api [29-Dec-22]
        logger.log(f"In modify_train_data[{new_data}]enterprise[{enterprise}]","0") 
        f = open("/proteus-sense/trained_model/" + modelType +"/" + modelScope + "/" + enterprise+ "/" + modelName +"/nlu.json")  # Added by SwapnilB for trainemodel api [29-Dec-22]
        data = json.load(f)
        product_data = new_data['product_data']
        synonym_data = new_data.get('synonym_data',0)
        logger.log(f"{synonym_data}","0")
        converted_data = Rasa.convert_data(product_data)
        for i in range(len(converted_data)):
            data['rasa_nlu_data']['common_examples'].append(converted_data[i])
        if synonym_data!=0:
            for value in synonym_data.keys():
                flag=0
                for j in range(len(data['rasa_nlu_data']['entity_synonyms'])):
                    if(value==data['rasa_nlu_data']['entity_synonyms'][j]['value']):
                        flag=1
                        data['rasa_nlu_data']['entity_synonyms'][j]['synonyms'].append(synonym_data[value])
                if flag==0:
                    new_synonym = {"value":value,"synonyms":synonym_data[value]}
                    data['rasa_nlu_data']['entity_synonyms'].append(new_synonym)
        Rasa.export_train_data(data,modelScope,enterprise, modelType, modelName)

            ##### Predict API #####
    @staticmethod
    def get_prediction(data, enterprise, modelScope="", modelType="", modelName=""):
        if "text" in data.keys():
        # if "descr" in data.keys():                 # Added  by SwapnilB on [29-Dec-22] because "text" gets a keyError 
            logger.log(f"predictor_rasa : having text key.","0")
            product_list = data['text']
            # product_list = data['descr']        # Added  by SwapnilB on [29-Dec-22] because "text" gets a keyError 
        elif "lines" in data.keys():
            logger.log(f"data with lines.","0")
            lines = data['lines']
            str='['
            for x in lines:
                str = str+"\""+x["descr"]+"\","
            str = str +"]"

            product_list = eval(str)
            logger.log(f"Extract text from lines:{product_list}","0")
        else:
            
            logger.log(f"noline data found return blank prediction. ","0")
            return jsonify({"prediction":[]})

        logger.log(f"predictor_rasa : product_list [{product_list}]","0") 
        attr_count = 3
        if data.get('attr_count',0):
            attr_count = data['attr_count']
        logger.log(f"predictor_rasa : attr_count {attr_count}]","0")   
        
        rasa_id_interpreter = Rasa_id_interpreter()
        return rasa_id_interpreter.extract_entities(product_list, attr_count, enterprise, modelScope, modelType, modelName)
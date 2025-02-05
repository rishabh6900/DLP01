import os
from box.exceptions import BoxValueError # type: ignore
import yaml
from DL01_in_cnn import logger 
import json
import joblib
from ensure import ensure_annotations # type: ignore
from box import ConfigBox # type: ignore
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): pah and returns

    Raises:
          ValueError if yaml file is empty
          e: empty file 
              
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded Successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list,verbose = True):
    """ create list of directories 
    Args:
        path_to_directories(list): list of path of directories 
        ignore_log (bool,optional): ignore if multiple dirs is to be created.Defaul
    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")



@ensure_annotations
def save_json(path:Path,data:dict):
    """save  json data 
    Args:
        path(Path):path to json file 
        data(dict): data to be savd in json file
    
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at : {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data 
    Args:
        path(Path) : path to json file 

    Returns:
    ConfigBox: data as class attributes instead of dict 
    
    """
    
    with open(path) as f:
        content = json.loads(f)

    logger.info(f"json file loaded succesfully from : {path}")
    return ConfigBox(content)



@ensure_annotations 
def save_bin(data: Any, path:Path):
    """save binary file 
    Args:
        data(Any): data to be saved as binary
        path(Path): path to binary file 
    """

    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at :{path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data 
    Args:
        path(Path):path to binart file 
    Returns:
           Any: Object stored in the file 
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from : {path}")
    return data 



@ensure_annotations
def get_size(path:Path) ->str:
    """get size in KB 
    Args:
        path(Path):path of the file 

    Returns :
           str: size in KB
    
    """
    size_in_Kb = round(os.path.getmtime(path)/1024)
    return f"~{size_in_Kb} KB"



def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName,"wb") as f:
        f.write(imgstring)
        f.close()

    
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())
   

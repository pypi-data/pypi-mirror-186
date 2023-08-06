import os
from random import randint
from subprocess import Popen, PIPE
from os.path import join, dirname
from dotenv import load_dotenv

class AWSConfig:    
    def __init__(self,config_file_path:str) -> None:
        self.AWS_PROFILE_NAME = f"""user_{randint(999,9999)}"""

        config_variables = self._get_config_variables(config_file_path)
        
        if len(config_variables["SESSION_TOKEN"]) > 0:
            commands = f"""aws configure set default.region ap-south-1 --profile {self.AWS_PROFILE_NAME}; aws configure set aws_access_key_id {config_variables["ACCESS_KEY_ID"]} --profile {self.AWS_PROFILE_NAME}; aws configure set aws_secret_access_key {config_variables["SECRET_ACCESS_KEY"]} --profile {self.AWS_PROFILE_NAME}; aws configure set aws_session_token {config_variables["SESSION_TOKEN"]} --profile {self.AWS_PROFILE_NAME}"""
        else:
            commands = f"""aws configure set default.region ap-south-1 --profile {self.AWS_PROFILE_NAME}; aws configure set aws_access_key_id {config_variables["ACCESS_KEY_ID"]} --profile {self.AWS_PROFILE_NAME}; aws configure set aws_secret_access_key {config_variables["SECRET_ACCESS_KEY"]} --profile {self.AWS_PROFILE_NAME}"""
        
        for command in commands.split(";"):
            process = Popen(command.strip(" "),shell=True,stdout=PIPE)
            stdout, _ = process.communicate()
    
        self._get_connection_details()
            
    def _get_connection_details(self):
        command = f"aws sts get-caller-identity --profile {self.AWS_PROFILE_NAME} --output json"

        try:
            process = Popen(command,shell=True,stdout=PIPE)
            stdout, _ = process.communicate()
            print(stdout.decode("utf-8"))
        except Exception as E:
            print(E)
            
    
    def _get_config_variables(self,config_file_path:str):
        
        if os.path.exists(config_file_path):
            dotenv_path = join(config_file_path)
            load_dotenv(dotenv_path)

            ACCESS_KEY_ID = os.environ.get("aws_access_key_id","")
            SECRET_ACCESS_KEY = os.environ.get("aws_secret_access_key","")
            SESSION_TOKEN = os.environ.get("aws_session_token","")
            
            if ACCESS_KEY_ID == "" or SECRET_ACCESS_KEY == "":
                raise Exception("Invalid Environment Variables, Please check the given config file")
            
            return {
                "ACCESS_KEY_ID":ACCESS_KEY_ID,
                "SECRET_ACCESS_KEY":SECRET_ACCESS_KEY,
                "SESSION_TOKEN":SESSION_TOKEN 
            }
        
        else:
            raise Exception("Invalid Config File Path")
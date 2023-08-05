from __future__ import print_function

# import logging

import json
import sys
import uuid
from random import randrange # TODO remove this
import requests
import logging
from cakework import exceptions
from urllib3.exceptions import NewConnectionError
import os
from cakework import auth

# TODO: need to re-enable TLS for the handlers in the fly.toml file. Try these settings: https://community.fly.io/t/urgent-grpc-server-unreachable-via-grpcurl/2694/12 for alpn
# TODO figure out how to configure the settings for fly.toml for grpc!
# TODO also need to make sure different runs don't interfere with each other
# TODO add a parameter for an entry point into the system (currently, assume that using cakework_app.py)
logging.basicConfig(level=logging.INFO)

class Client:
    def __init__(self, project, client_token, local=False): # TODO: infer user id // TODO revert local back to False

        # TODO get rid of "shared"
        self.project = project.lower().replace('_', '-')
        # make a call to the frontend to get the user_id using the client token
        if local:
            self.frontend_url = "http://localhost:8080"
        else:
            self.frontend_url = "https://cakework-frontend.fly.dev"

        response = None
        self.headers = None
        try:

            # based on the particular user id, how do we fetch user credentials and get a token on behalf of the user?
            # need SOME sort of token first
            token = auth.get_token("LtM7DMVVmENYKIL8UYIvcUqmQxxwru5B", "CJ2HtEMSGMWVyxxlHfuluPLQ4-ZDrcOTIF_DDUmabkog24DuHLV8ElaL08gk8wVG", "get:user_from_client_token get:status get:result submit:task")
            self.headers = {'content-type': 'application/json', 'authorization': 'Bearer ' + token}
            response = requests.get(f"{self.frontend_url}/get-user-from-client-token", json={"token": client_token}, headers=self.headers)      # Q: should this take app?        
               
            # if dont' get a avalid user
            # TODO raise exception
                       
            # TODO: handle error for if can't get a user from the client token. technically
            # we should be getting a JWT token instead first
            response.raise_for_status() # TODO delete this?
            # TODO: handle http error, or request id not found error
        except requests.exceptions.HTTPError as errh:
            logging.exception("Http error while connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Http error while connecting to Cakework frontend")
        except requests.exceptions.Timeout as errt:
            logging.exception("Timed out connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Timed out connecting to Cakework frontend")
        except requests.exceptions.RequestException as err:
            logging.exception("Request exception connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Request exception connecting to Cakework frontend")
        except (ConnectionRefusedError, ConnectionResetError) as e:
            logging.exception("Failed to connect to Cakework frontend service", exc_info=True)
            raise exceptions.CakeworkError("Failed to connect to Cakework frontend service")
        except Exception as e:
            # TODO catch and raise specific errors? 
            logging.exception("Error happened while initializing client", exc_info=True)
            raise exceptions.CakeworkError("Something unexpected happened")
        if response is not None:
            if response.status_code == 200:
                response_json = response.json()
                self.user_id = response_json["id"] # Q: how to return None if process is still executing? instead of empty string
                self.headers = {'content-type': 'application/json', 'authorization': 'Bearer ' + token}
            else:
                raise exceptions.CakeworkError("Error happened while trying to get the user from the client token")
        else:
            raise exceptions.CakeworkError("Error happened while trying to get the user from the client token")

        self.local = local
        
    def get_status(self, request_id):
        response = None
        try:
            # Q: status 200 vs 201??? what's the diff?
            # TODO strip app from everywhere
            response = requests.get(f"{self.frontend_url}/get-status", json={"userId": self.user_id, "app": self.project, "requestId": request_id}, headers=self.headers)                
            response.raise_for_status() # TODO delete this?
            # TODO: handle http error, or request id not found error
        except requests.exceptions.HTTPError as errh:
            logging.exception("Http error while connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Http error while connecting to Cakework frontend")
        except requests.exceptions.Timeout as errt:
            logging.exception("Timed out connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Timed out connecting to Cakework frontend")
        except requests.exceptions.RequestException as err:
            logging.exception("Request exception connecting Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Request exception connecting Cakework frontend")
        except (ConnectionRefusedError, ConnectionResetError) as e:
            logging.exception("Failed to connect to Cakework frontend service", exc_info=True)
            raise exceptions.CakeworkError("Failed to connect to Cakework frontend service")
        except Exception as e:
            # TODO catch and raise specific errors? 
            logging.exception("Error happened while getting status", exc_info=True)
            raise exceptions.CakeworkError("Something unexpected happened")
        if response is not None:
            if response.status_code == 200:
                response_json = response.json()
                status = response_json["status"] # this may be null?
                return status
            elif response.status_code == 404:
                return None
            else:
                raise exceptions.CakeworkError("Internal server exception")
        else:
            raise exceptions.CakeworkError("Internal server exception") 

    # TODO figure out how to refactor get_result and get_status  
    def get_result(self, request_id):
        response = None
        try:
            # Q: status 200 vs 201??? what's the diff?
            response = requests.get(f"{self.frontend_url}/get-result", json={"userId": self.user_id, "app": self.project, "requestId": request_id}, headers=self.headers)                
            response.raise_for_status() # TODO delete this?
            # TODO: handle http error, or request id not found error
        except requests.exceptions.HTTPError as errh:
            logging.exception("Http error while connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Http error while connecting to Cakework frontend")
        except requests.exceptions.Timeout as errt:
            logging.exception("Timed out connecting to Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Timed out connecting to Cakework frontend")
        except requests.exceptions.RequestException as err:
            logging.exception("Request exception connecting Cakework frontend", exc_info=True)
            raise exceptions.CakeworkError("Request exception connecting Cakework frontend")
        except (ConnectionRefusedError, ConnectionResetError) as e:
            logging.exception("Failed to connect to Cakework frontend service", exc_info=True)
            raise exceptions.CakeworkError("Failed to connect to Cakework frontend service")
        except Exception as e:
            # TODO catch and raise specific errors? 
            logging.exception("Error happened while getting status", exc_info=True)
            raise exceptions.CakeworkError("Something unexpected happened")
        if response is not None:
            if response.status_code == 200:
                response_json = response.json()
                result = response_json["result"] # Q: how to return None if process is still executing? instead of empty string
                return result
            elif response.status_code == 404:
                return None
            else:
                raise exceptions.CakeworkError("Internal server exception")
        else:
            raise exceptions.CakeworkError("Internal server exception") 
       
    def __getattr__(self, name):
        def method(*args):
            sanitized_name = name.lower()
            sanitized_name = name.replace('_', '-')          
            response = requests.post(f"{self.frontend_url}/submit-task", json={"userId": self.user_id, "app": self.project, "task": sanitized_name, "parameters": json.dumps(args)}, headers=self.headers)
            response_json = response.json()
            request_id = response_json["requestId"] # this may be null?
            return request_id

        return method
    
# if __name__ == '__main__':
#     run() 
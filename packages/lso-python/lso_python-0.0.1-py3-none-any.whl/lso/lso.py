import json
import requests
import traceback
from datetime import datetime, timezone
from typing import Optional, Callable


class LogSearchOptimizer:

    __BACKENDURL = "http://34.28.32.204/api/validate-pk"
    __CHUNK_SIZE = 100
    __DISPATH_API = "https://us-central1-angry-nerds-374213.cloudfunctions.net/push-messages"

    def __init__(self, private_key: str, product_id: str, fail_silently: bool=True) -> None:    
        self.__is_authenticated = False
        self.fail_silently = fail_silently
        self.token = None
        self.__buffer = []
        self.__connect(private_key, product_id)

    def __connect(self, private_key: str, product_id: str) -> None:
        resp = self.__make_api_call(
            url=self.__BACKENDURL, method="POST", payload={"private_key": private_key, "product_id": product_id}
        )
        # code for setting token, is_authenticated to True
        self.token = resp.get("data", {}).get("token", "")
        self.__is_authenticated = True

    def __make_api_call(self, url, method, payload: Optional[dict]={},  headers:Optional[dict]={}) -> dict:
        headers.update({"Content-Type": "application/json"})
        resp = requests.request(method=method, url=url, headers=headers, json=payload)
        if resp.status_code != 200 and not self.fail_silently:
            raise Exception(resp.text)
        if resp.status_code != 200 and self.fail_silently:
            print(f"ERROR FROM LOGGER: {resp.text}")
        
        return resp.json()
    
    @staticmethod
    def __serialize_log(msg)-> str:
        if isinstance(msg, (dict, list,tuple, set)):
            msg = json.dumps(msg, default=str)
        if not isinstance(msg, str):
            raise Exception("Message has to be strictly in string")
        return msg
    
    def __create_msg(self, msg: str, is_error: bool = False) -> str:
        # timestamp in milliseconds since unix epoch
        utc_time = datetime.now(timezone.utc).timestamp() * 1000
        return {"log": msg, "is_error": is_error, "timestamp": utc_time}

    def __reset_buffer(self) -> None:
        self.__buffer = []

    
    def logging_wrapper(self, func: Callable):
        def inner(*args, **kwargs):
            trace_back_error = ''
            try:
                resp = func(*args, **kwargs)
            except Exception as e:
                trace_back_error = traceback.format_exc()
                self.print(trace_back_error, is_error=True)
                self.dispatch()
                raise
            self.dispatch()
            return resp
        return inner
    

    def print(self, msg, is_error:bool = False) -> None:
        print(msg)
        serialized_msg = self.__serialize_log(msg)
        msg = self.__create_msg(serialized_msg, is_error)
        if len(msg) >= self.__CHUNK_SIZE:
            self.__reset_buffer()
            self.dispatch()
        self.__buffer.append(msg)

    def dispatch(self) -> None:
        if not self.__is_authenticated and not self.fail_silently:
            raise Exception("Please authenticate yourself")
        if not self.__is_authenticated and self.fail_silently:
            print("ERROR FROM LOGGER: Please authenticate yourself")
        if self.__buffer and self.__is_authenticated:
            resp = self.__make_api_call(
                self.__DISPATH_API, method="POST", payload={"messages": self.__buffer}, headers={
                    "token": self.token
                }
            )
            self.__reset_buffer()

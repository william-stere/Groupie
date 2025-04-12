import json
import requests
from uuid import uuid4
from IflytekVudioToText import VudioToText


class dify:
    def __init__(self):
        with open("DifyConfig.json") as file:
            ConfigJson = json.loads(file.read())
            self.config = {
                "API_BASE" : ConfigJson["API_BASE"],
                "WORKFLOW_ID" : ConfigJson["WORKFLOW_ID"],
                "API_KEY" : ConfigJson["API_KEY"],
                "USER_INFO" : ConfigJson["USER_INFO"]
                }


        self.session = {
            "session_id" : str(uuid4()),
            "user_agent" : "api"
        }

    def _build_headers(self):
        return {
            "Authorization": f"Bearer {self.config['API_KEY']}",
            "Content-Type": "application/json"
        }
    
    def send_request(self, user_input, *png):
        try:
            if a[0] == None:
                    exit
        except:
            a = None
        payload = {
            #TODO 图片处理逻辑
            "user": self.config["USER_INFO"],
            "inputs": {"input": user_input, "png" : png[0]},
            "session": self.session,
            "response_mode": "blocking"
        }

        url = f"{self.config['API_BASE']}/{self.config['WORKFLOW_ID']}"
  
        print(f"{url}\n\n", 
              f"{self._build_headers()}\n\n", 
              f"{payload}\n\n")

        response = requests.post(
            url, 
            json=payload,
            headers=self._build_headers(),
            timeout=3600
        )

        print(f"{response.status_code}")

        json_response = response.json()

        print(json.dumps(json_response, indent=2, ensure_ascii=False))

def AudioToText():
    return 



if __name__ == "__main__":
    VudioInput = VudioToText(input(">>>"))
    #TODO 图片输入逻辑
    #TODO 行空板的代码
    dify.send_request(VudioInput)
    print("\nEXIT")
    
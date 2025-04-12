import json
import requests
from uuid import uuid4
from IflytekVudioToText import VudioToText


class DifyMain:
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
    
    def send_request(self, user_input):
        payload = {
            "user": self.config["USER_INFO"],
            "inputs": {"input": user_input,},
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
    UserInput = VudioToText("lfasr_涉政.wav")
    print(UserInput)
    send = DifyMain()
    send.send_request(UserInput)
    print("\nEXIT")
    
import json
import requests
from uuid import uuid4

class DifyMain:
    def __init__(self):
        self.config = {
            "API_BASE" : "http://192.168.31.36/v1/app",
            "WORKFLOW_ID": "7ba32635-fef4-4b55-be9e-995c0c66f870",
            "API_KEY": "app-GhvZsM754wsnvKCwealEEc9b",
            "USER_INFO": "ws"
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
    
    def send_request(self, user_input, png):
        payload = {
            "user": self.config["USER_INFO"],
            "inputs": {"input": user_input, "png" : png},
            "session": self.session,
            "response_mode": "blocking"
        }

        url = f"{self.config['API_BASE']}/{self.config['WORKFLOW_ID']}/workflows/run"
  
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

if __name__ == "__main__":
    #TODO 图片上传，上下文
    send = DifyMain()
    send.send_request("hello", None)
    print("\nEXIT")

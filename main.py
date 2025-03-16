import json
import requests
from uuid import uuid4

class DifyMain:
    def __init__(self):
        self.config = {
            "API_BASE" : "http://ws-server/v1",
            "WORKFLOW_ID": "workflows/run",
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
    
    def send_request(self, user_input,png):
        payload = {
            "user": self.config["USER_INFO"],
            "inputs": {"input": user_input, "png" : png},
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
            timeout=360
        )

        print(f"{response.status_code}")

        json_response = response.json()

        print(json.dumps(json_response, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    send = DifyMain()
    send.send_request("hello", None)
    print("\nEXIT")
    
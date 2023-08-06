import requests

class Model:
    def __init__(self, api_key: str):
        self.model = None
        self.beautify = False
        self.api_key = api_key
        
    def beautify_response(self):
        self.beautify = True
        
    def set_model(self, model: str):
        """
        Args:
            model (str): Model UUID or model alias name
        """
        self.model = model
        
    def predict(self, image: str):
        api_call = requests.post(
            "https://api.server.cameralyze.co/model/{model}".format(model=self.model),
            json={"apiKey": self.api_key, "image": image, "rawResponse": self.beautify}
        )
        
        return api_call.json() 
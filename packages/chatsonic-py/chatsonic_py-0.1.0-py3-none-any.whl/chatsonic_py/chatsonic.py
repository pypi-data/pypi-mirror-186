import requests
import enum


class EngineType(str, enum.Enum):
    premium = "premium"


class Conversation:
    """ 
    A conversation class that allows you to send messages to chatsonic and get a reply from the AI,
    use send_message to send a message to chatsonic and get a reply from the AI,
    use the history attribute to get the history of a conversation, 

    Attributes
    ----------
    api_key : str
        the API key to writesonic's v2 API, you can get one using this : https://docs.writesonic.com/reference/finding-your-api-key
    google_enabled : bool
        If enabled, ChatSonic will use Google search results to answer the question. This is useful when trained AI model doesn't have an answer to the question.
    enable_memory : bool
        wether to enable memory or not (default False), you can override the original history_data by using the history_data parameter in send_message 

    Methods
    -------
    send_message(message: str, history_data: list = []) -> dict:
        sends a message to chatsonic and gets a reply from the AI: \n

    Examples
    --------
    For Memory Enabled Conversation
    ```
    from chatsonic_py import Conversation
    chatsonic = Conversation(api_key="Your api key here",enable_memory=True)
    reply = chatsonic.send_message(message="Hello")
    print(reply)

    ```

    """
    api_key: str
    google_enabled: str
    engine: EngineType
    enable_memory: bool
    host: str = "https://api.writesonic.com"
    timeout: int = 45
    history: list = []

    def __init__(
        self,
        *,
        api_key,
        google_enabled: bool = True,
        enable_memory: bool = False,
        engine: EngineType = EngineType.premium,
        timeout: int = 45,
    ) -> None:

        self.api_key = api_key
        self.google_enabled = google_enabled
        self.engine = engine
        self.enable_memory = enable_memory
        self.timeout = timeout

    def send_message(self, *, message: str, history_data: list = []) -> dict:
        """Send a message to chatsonic and get a reply from the AI, 
        history_data is a list of dictionaries with the following format: \n 
        ```
        [
        {
            "is_sent": true,
            "message": "Who is the President of the United States?"
        },
        {
            "is_sent": false,
            "message": "The 46th and current President of the United States is Joseph R. Biden, Jr., who was sworn in on January 20, 2021."
        }
        ]
        ```
        
        more about history_data [here](https://docs.writesonic.com/reference/memory-functionality)
        to get history for a conversation, use the history attribute of the Conversation object  """

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": self.api_key,
        }
        payload = {
            "input_text": message,
            "history_data": history_data,
            "enable_google_results": self.google_enabled,
            "enable_memory": self.enable_memory,


        }
        params = {
            "engine": self.engine,
        }
        if self.enable_memory:
            payload["history_data"] = history_data if len(history_data) > 0 else self.history
       
        data = requests.post(
            f"{self.host}/v2/business/content/chatsonic",
            headers=headers,
            json=payload,
            params=params,
            timeout=45,
            
        ).json()

        

        history_data.append({"is_sent":True,"message":message})
        history_data.append({"is_sent":False,"message":data.get("message")})
        self.history  = history_data
        return data


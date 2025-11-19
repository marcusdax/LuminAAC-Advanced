import os

class Config:
    # API Settings
    API_HOST = "0.0.0.0"
    API_PORT = 8000
    
    # Model Settings
    SPEECH_MODEL = "microsoft/speecht5_tts"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Privacy Settings
    PRIVACY_ENABLED = True
    FEDERATED_LEARNING = True
    
    # Storage
    DATA_PATH = "./data"
    MODEL_PATH = "./models"
# Full implementation from previous response
import torch
import torch.nn as nn
import torchaudio
import numpy as np
from transformers import AutoProcessor, AutoModel
import librosa
from typing import Dict, List, Optional

class SpeechLMProcessor:
    """
    End-to-end Speech Language Model processor
    Preserves both semantic and paralinguistic features
    """
    
    def __init__(self, model_name: str = "microsoft/speecht5_tts"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # ... rest of implementation from previous response
        pass
    
    def process_audio(self, audio_array: np.ndarray, sample_rate: int = 16000) -> Dict:
        """End-to-end speech processing"""
        # ... implementation from previous response
        pass
    
    # ... all other methods from previous response
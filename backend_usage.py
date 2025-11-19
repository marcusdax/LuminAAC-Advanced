"""
Example usage of the LuminAAC backend API
"""

import requests
import json
import numpy as np

# Backend API base URL
BASE_URL = "http://localhost:8000"

def analyze_speech_example():
    """Example of speech analysis API call"""
    
    # Generate mock audio data (1 second of 440Hz sine wave)
    sample_rate = 16000
    t = np.linspace(0, 1, sample_rate)
    audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)  # 440Hz tone
    
    payload = {
        "audio_data": audio_data.tolist(),
        "sample_rate": sample_rate,
        "user_context": {
            "user_id": "example_user",
            "environment": "home"
        }
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/analyze-speech", json=payload)
        if response.status_code == 200:
            result = response.json()
            print("Speech Analysis Result:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Request failed: {e}")

def multimodal_fusion_example():
    """Example of multimodal fusion API call"""
    
    payload = {
        "audio_data": np.random.random(16000).tolist(),  # 1 second of random audio
        "visual_data": np.random.random(512).tolist(),   # Visual features
        "behavioral_context": {
            "hour_of_day": 14,
            "environment": "therapy",
            "recent_interactions": ["request", "comment", "request"],
            "preferences": {
                "preferred_communication_style": 0.8
            }
        },
        "user_id": "test_user_123",
        "session_id": "session_456"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/fuse-modalities", json=payload)
        if response.status_code == 200:
            result = response.json()
            print("Multimodal Fusion Result:")
            print(json.dumps(result, indent=2))
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    print("Testing LuminAAC Backend API...")
    print("\n1. Testing Speech Analysis:")
    analyze_speech_example()
    
    print("\n2. Testing Multimodal Fusion:")
    multimodal_fusion_example()
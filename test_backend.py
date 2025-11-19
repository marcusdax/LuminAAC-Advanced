"""
Backend API tests for LuminAAC
"""

import pytest
import requests
import numpy as np
from backend.main_service import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_speech_analysis():
    """Test speech analysis endpoint"""
    
    # Generate test audio data
    sample_rate = 16000
    t = np.linspace(0, 1, sample_rate)
    audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)
    
    payload = {
        "audio_data": audio_data.tolist(),
        "sample_rate": sample_rate,
        "user_context": {"user_id": "test_user"}
    }
    
    response = client.post("/api/analyze-speech", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert "prediction_id" in data
    assert "analysis" in data
    assert "timestamp" in data

def test_system_health():
    """Test system health endpoint"""
    response = client.get("/api/system-health")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] in ["healthy", "degraded", "unhealthy"]
    assert "components" in data
    assert "statistics" in data

def test_ethical_guidelines():
    """Test ethical guidelines endpoint"""
    response = client.get("/api/ethical-guidelines")
    assert response.status_code == 200
    
    data = response.json()
    assert "privacy_policy" in data
    assert "ethical_guidelines" in data
    assert "compliance" in data

if __name__ == "__main__":
    pytest.main([__file__])
"""
Frontend component tests for LuminAAC
"""

import pytest
import sys
import os

# Add frontend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../frontend'))

from audio_therapy.mood_modulation import BinauralTherapy, MoodState
from audio_therapy.sound_library import SoundTherapyLibrary, NatureSounds

def test_binaural_therapy():
    """Test binaural therapy initialization"""
    therapy = BinauralTherapy()
    
    # Test mood states
    assert len(MoodState) == 6
    assert MoodState.CALM.value == "calm"
    
    # Test frequency presets
    presets = therapy.frequency_presets
    assert MoodState.CALM in presets
    assert "base_freq" in presets[MoodState.CALM]

def test_sound_library():
    """Test sound library functionality"""
    sound_lib = SoundTherapyLibrary()
    
    # Test nature sounds enum
    assert len(NatureSounds) == 5
    assert NatureSounds.OCEAN.value == "ocean"
    
    # Test sound generation
    ocean_sound = sound_lib.generate_nature_soundscape(NatureSounds.OCEAN, duration=1)
    assert ocean_sound is not None

def test_communication_categories():
    """Test communication category generation"""
    from user_interface.aac_interface import AACUserInterface
    
    ui = AACUserInterface()
    
    # Test category generation
    happy_cats = ui._get_happy_categories()
    calm_cats = ui._get_calm_categories()
    
    assert "Share Joy" in happy_cats
    assert "Relaxation" in calm_cats
    assert len(happy_cats["Share Joy"]) == 4

if __name__ == "__main__":
    pytest.main([__file__])
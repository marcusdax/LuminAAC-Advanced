"""
Example usage of LuminAAC frontend components
"""

from frontend.audio_therapy import BinauralTherapy, MoodState
from frontend.audio_therapy import SoundTherapyLibrary, NatureSounds

def test_audio_therapy():
    """Test the audio therapy system"""
    
    print("Testing Audio Therapy System...")
    
    # Test binaural therapy
    therapy = BinauralTherapy()
    
    print("\n1. Testing Calm Therapy:")
    therapy.start_mood_therapy(MoodState.CALM)
    time.sleep(3)  # Play for 3 seconds
    therapy.stop_therapy()
    
    print("\n2. Testing Focus Therapy:")
    therapy.start_mood_therapy(MoodState.FOCUSED, therapy_type="isochronic")
    time.sleep(3)
    therapy.stop_therapy()
    
    # Test sound library
    print("\n3. Testing Nature Sounds:")
    sound_lib = SoundTherapyLibrary()
    ocean_sound = sound_lib.generate_nature_soundscape(NatureSounds.OCEAN, duration=2)
    
    print("Audio therapy test completed!")

def test_user_interface():
    """Test user interface components"""
    
    print("\nTesting User Interface Components...")
    
    # This would typically involve Streamlit testing
    # For now, just demonstrate component creation
    from frontend.user_interface.aac_interface import AACUserInterface
    
    ui = AACUserInterface()
    print("User interface components initialized successfully!")
    
    # Test communication categories
    happy_categories = ui._get_happy_categories()
    print(f"Happy categories: {list(happy_categories.keys())}")
    
    calm_categories = ui._get_calm_categories() 
    print(f"Calm categories: {list(calm_categories.keys())}")

if __name__ == "__main__":
    test_audio_therapy()
    test_user_interface()
    print("\nAll tests completed!")
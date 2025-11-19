
**docs/user_guide.md**
```markdown
# LuminAAC User Guide

## Overview

LuminAAC is an advanced Augmentative and Alternative Communication (AAC) system that combines AI-powered communication with therapeutic support. This guide covers both user and caretaker interfaces.

## User Interface

### Getting Started

1. **Launch the Application**
   - Run `streamlit run main_application.py` from the frontend directory
   - Select "AAC User" from the sidebar
   - The interface will load with calming colors and animations

2. **Basic Communication**
   - Tap any button to speak the associated phrase
   - Buttons are organized by categories (Basic Needs, Feelings, Activities)
   - The system learns from your selections to provide better suggestions

3. **Emotional Expression**
   - Use the mood selector at the bottom to express how you're feeling
   - The interface adapts colors and categories based on your mood
   - Select from: Happy, Calm, Energetic, Sad, or Frustrated

### Audio Therapy Features

1. **Mood Support**
   - Tap any mood support button to start therapeutic audio
   - Options: Calm, Focus, Energy, Happy, Grounding
   - Each uses different frequencies to support your emotional state

2. **Volume Control**
   - Use the slider to adjust therapy volume
   - Lower volumes provide subtle support
   - Higher volumes for more pronounced effects

3. **Breathing Exercises**
   - Tap "Start Breathing Exercise" for guided relaxation
   - Follow the visual guide for breathing rhythm
   - Combines with calming audio therapy

### Predictive Suggestions

- The system shows "You might want to say..." suggestions
- These are AI-predicted based on your patterns and current context
- Tap any suggestion to speak it immediately

## Caretaker Interface

### Dashboard Overview

1. **Launch Caretaker View**
   - Select "Caretaker" from the sidebar when launching
   - View real-time monitoring dashboard

2. **Key Metrics**
   - **Current Mood**: User's emotional state
   - **Stress Level**: Automated stress detection
   - **Communication Rate**: Messages per minute
   - **Engagement**: Participation level

3. **Alert System**
   - Red alerts for high-priority issues
   - Yellow alerts for medium-priority observations
   - Green for normal operation

### Monitoring Features

1. **Mood Timeline**
   - View emotional patterns throughout the day
   - Identify trends and triggers
   - Track progress over time

2. **Stress Monitor**
   - Real-time stress indicator analysis
   - Vocal tension, speech rate, pause frequency
   - Color-coded stress levels

3. **Communication Analysis**
   - Pie chart of communication types
   - Insights into communication patterns
   - Recommendations for support

### Annotation Tools

1. **Quick Annotation**
   - Click "New Annotation" in sidebar
   - Select observed emotion and context
   - Add confidence rating and notes
   - Save to help improve AI models

2. **Intervention Recommendations**
   - AI-suggested interventions based on current state
   - Priority levels (High, Medium, Low)
   - Step-by-step action plans

### Reporting

1. **Weekly Reports**
   - Generate comprehensive progress reports
   - View key metrics and achievements
   - Export as PDF for records

2. **System Settings**
   - Adjust alert thresholds
   - Configure privacy settings
   - Manage user profiles

## Best Practices

### For Users
- Use mood selection regularly to help the system learn
- Try different audio therapy options to find what works best
- Use predictive suggestions to speed up communication
- Take breaks and use breathing exercises when needed

### For Caretakers
- Review the dashboard daily for patterns
- Use annotations to capture important observations
- Implement recommended interventions promptly
- Generate weekly reports to track progress

## Troubleshooting

### Common Issues

**Audio Not Working**
- Check system volume
- Ensure headphones/speakers are connected
- Restart the application

**Interface Not Responding**
- Refresh the browser page
- Check internet connection
- Restart the backend server

**Predictions Seem Inaccurate**
- Use the feedback system to correct predictions
- Add annotations to provide more context
- The system improves with more data

### Getting Help

- Check the system health page
- Review this user guide
- Contact technical support
- Check GitHub issues for known problems

## Privacy and Ethics

- All data is processed with privacy protection
- Audio therapy uses subtle frequencies outside typical hearing range
- Users can opt out of data collection
- Caretakers should respect user privacy and consent

---

For additional support, contact the LuminAAC development team or create an issue on our GitHub repository.
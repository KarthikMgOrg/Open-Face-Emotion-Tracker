
# Open-Face-Emotion-Tracker

An end-to-end real-time emotion tracker that captures and analyzes facial expressions using a powerful stack:

1. **[OpenFace](https://github.com/TadasBaltrusaitis/OpenFace)** – for facial landmark detection and Action Unit (AU) extraction  
2. **Kalman Filtering** – to smooth noisy gaze signals and facial features  
3. **Custom Feature Engineering** – to extract blink rates, gaze focus, head pose, emotion frequency, and more  
4. **Google Vertex AI** – for summarizing and interpreting emotional states using a Large Language Model (LLM)

---

## 🚀 What It Does

- Streams live facial tracking data using OpenFace
- Applies Kalman filtering to clean gaze and motion signals
- Detects emotions using AU-based logic (joy, anger, sadness, surprise, confusion, etc.)
- Engineers features in real time, including:
  - Blink frequency
  - Smile intensity
  - Gaze deviation
  - Emotional state distribution
- Periodically sends a consolidated summary to Vertex AI LLM to analyze user engagement and mood

---

## 🧠 Sample LLM Prompt

```json
{
  "blink_freq": 0.27,
  "smile_freq": 0.12,
  "avg_head_tilt": 3.8,
  "percent_away": 22.4,
  "emotion_counts": {
    "neutral": 19,
    "joy": 6,
    "confusion": 4
  }
}
````

🗣️ Prompt:

> "Given the following user gaze and emotion features, analyze the user's cognitive and emotional state. Please describe the user's likely focus level, mood, and engagement."

---

## 🛠️ Tech Stack

* `Python 3.11`
* `OpenFace` (AU detection)
* `Kafka` (streaming facial data)
* `NumPy`, `deque`, `Kalman filters` (signal smoothing)
* `Vertex AI` (LLM analysis and interpretation)

---

## 📊 Real-Time Feature Engineering

Feature extraction includes:

| Feature          | Description                             |
| ---------------- | --------------------------------------- |
| `blink_freq`     | Blinks per second (based on AU45)       |
| `smile_freq`     | Smile activity from AU12/AU06           |
| `avg_head_tilt`  | Pose\_Rx average for attention tracking |
| `percent_away`   | % of time gaze deviates from center     |
| `emotion_counts` | Count of detected emotions in window    |

---

## 📦 How to Run

1. Install [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) and make sure it's streaming facial data to Kafka
2. Install Python dependencies:

   ```bash
   pip install numpy kafka-python
   ```
3. Run the consumer:

   ```bash
   python kafka/consumer.py
   ```
4. Check `feature.txt` for real-time summaries and LLM prompts

---

## 🤖 Coming Soon

* Emotion timeline charts
* Real-time dashboard UI (using WebSockets)
* Improved deep learning-based emotion detection
* Integration with video conferencing tools

---

## 📄 License

MIT License. Use freely and contribute back!

---

## 🤝 Contribute

Pull requests, ideas, and bug reports are welcome!
If you’ve got a new way to engineer features or want to bring in another LLM provider—let’s collaborate!

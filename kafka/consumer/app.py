from collections import deque
from kafka import KafkaConsumer
import csv
import os
from collections import deque, Counter
from datetime import datetime, timedelta
import io
import numpy as np
from tqdm import tqdm

frame_buffer = deque()
MAX_TIME_WINDOW = 5  # seconds
# Constants
LOOK_AWAY_THRESHOLD_DEG = 15
SMILE_THRESHOLD = 1.0
BLINK_THRESHOLD = 1.0
EMOTION_THRESHOLD = 1.0
# Example Kalman filter implementation

eye_contact_list = []
facial_expressions_list = []
posture_list = []
professional_attire_list = []
time_stamp_list = []

global_behavioral_insights = {
    "eye_contact":"",
    "facial_expressions":"",
    "posture":"",
    "professional_attire":""
}

global_eye_gaze_tracking = {
    "detected":"",
    "time_stamps":[]
}


class SimpleKalmanFilter:
    def __init__(self):
        self.estimate = 0
        self.error_estimate = 1
        self.error_measurement = 1

    def update(self, measurement):
        kalman_gain = self.error_estimate / \
            (self.error_estimate + self.error_measurement)
        self.estimate = self.estimate + \
            kalman_gain * (measurement - self.estimate)
        self.error_estimate = (1 - kalman_gain) * self.error_estimate
        return self.estimate


# Initialize separate Kalman filters for X and Y
kf_x = SimpleKalmanFilter()
kf_y = SimpleKalmanFilter()

# Output CSV path
OUTPUT_DIR = "/Users/karthikeyan/Downloads"
SMOOTHED_OUTPUT_FILE = os.path.join(OUTPUT_DIR, "output_chunk_001_smooth.csv")

os.makedirs(os.path.dirname(SMOOTHED_OUTPUT_FILE), exist_ok=True)

# Connect to Kafka topic
consumer = KafkaConsumer(
    'gaze-user-1',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True
)


def process_new_frame(new_frame):
    try:
        frame = list(map(float, new_frame))
        timestamp = float(frame[2])  # assuming index 2 is timestamp
        frame_buffer.append((timestamp, frame))

        # Remove old frames outside the time window
        current_time = timestamp
        while frame_buffer and (current_time - frame_buffer[0][0]) > MAX_TIME_WINDOW:
            frame_buffer.popleft()

        if len(frame_buffer) >= 30:  # ensure enough data
            frames = [f for _, f in frame_buffer]
            engineer_features(frames)
    except Exception as e:
        print(f"Failed to process frame: {e}")


def detect_emotions(frame):
    emotions = []

    # Thresholds (adjust if needed based on data)
    THRESH_JOY = 0.6
    THRESH_CONFUSION = 0.7
    THRESH_SURPRISE = 0.4
    THRESH_ANGER = 0.4
    THRESH_SADNESS = 0.6
    THRESH_NEUTRAL = 0.4

    # Joy: AU06 + AU12
    if frame[443] > THRESH_JOY and frame[439] > THRESH_JOY:
        emotions.append('joy')

    # Confusion: AU01 + AU04 (inner brow raise + brow lowerer)
    if frame[435] > THRESH_CONFUSION and frame[437] > THRESH_CONFUSION:
        emotions.append('confusion')

    # Surprise: AU01 + AU02 + AU05 + AU26
    if frame[435] > THRESH_SURPRISE and frame[441] > THRESH_SURPRISE \
            and frame[445] > THRESH_SURPRISE and frame[449] > THRESH_SURPRISE:
        emotions.append('surprise')

    # Anger: AU04 + AU07 + AU23
    if frame[437] > THRESH_ANGER and frame[447] > THRESH_ANGER and frame[441] > THRESH_ANGER:
        emotions.append('anger')

    # Sadness: AU01 + AU15
    if frame[435] > THRESH_SADNESS and frame[453] > THRESH_SADNESS:
        emotions.append('sadness')

    # Neutral only if no other emotion detected
    if not emotions and frame[451] > THRESH_NEUTRAL:
        emotions.append('neutral')

    return emotions


def gaze_angle(x, y):
    return np.degrees(np.arccos(1.0 / np.sqrt(x**2 + y**2 + 1)))


def detect_outside_gaze(frames, threshold_deg=15, window_size=5, min_duration=0.5):
    """
    Frame-rate independent detection of outside gaze.
    Only considers gaze shifts that last at least min_duration seconds.
    """
    from collections import deque

    outside_gaze_timestamps = []
    gaze_window = deque(maxlen=window_size)

    in_outside_gaze = False
    outside_gaze_start_time = None

    for frame in frames:
        timestamp = float(frame[2])  # Make sure timestamp is in seconds
        x, y = float(frame[5]), float(frame[6])
        angle = gaze_angle(x, y)

        gaze_window.append(angle)
        smoothed_angle = sum(gaze_window) / len(gaze_window)

        if smoothed_angle > threshold_deg:
            if not in_outside_gaze:
                # Start timing
                outside_gaze_start_time = timestamp
                in_outside_gaze = True
            else:
                # Check duration
                duration = timestamp - outside_gaze_start_time
                if duration >= min_duration:
                    if not outside_gaze_timestamps or timestamp - outside_gaze_timestamps[-1] > min_duration:
                        outside_gaze_timestamps.append(outside_gaze_start_time)
        else:
            # Reset if gaze returns inside
            in_outside_gaze = False
            outside_gaze_start_time = None

    return outside_gaze_timestamps


def save_features_to_file(features, filepath='feature.txt'):
    with open(filepath, 'a') as f:
        f.write(str(features) + '\n')


def cleanup_timestamps(stamps):
    all_stamps = []
    for time in stamps:
        splitted_str_time = str(time).split('.')[0]
        all_stamps.append(splitted_str_time)
    return list(set(all_stamps))

def engineer_features(frames):
    global global_behavioral_insights
    global global_eye_gaze_tracking
    try:
        frames = np.array(frames)  # shape: (N, feature_dim)

        # Compute delta (velocity) across frames
        deltas = np.diff(frames, axis=0)  # shape: (N-1, feature_dim)

        # Compute mean and std dev over time
        mean_features = np.mean(frames, axis=0)
        std_features = np.std(frames, axis=0)

        # Compute average velocity
        avg_velocity = np.mean(deltas, axis=0)

        # 1. Percent of time looking away
        gaze_angles = [gaze_angle(f[5], f[6]) for f in frames]
        looked_away = [ga > LOOK_AWAY_THRESHOLD_DEG for ga in gaze_angles]
        percent_away = 100 * np.mean(looked_away)

        # 2. Average head tilt (pose_Rx)
        head_tilts = [f[443] for f in frames]
        avg_head_tilt = np.mean(head_tilts)

        # 3. AU12 smile range and frequency
        au12 = [f[443] for f in frames]
        smile_range = np.max(au12) - np.min(au12)
        smile_freq = np.sum([a > SMILE_THRESHOLD for a in au12]) / len(frames)

        # 4. AU45 blink frequency
        timestamps = [f[2] for f in frames]
        time_diff = timestamps[-1] - timestamps[0] if len(timestamps) > 1 else 1e-6
        blink_freq = np.sum([f[451] > BLINK_THRESHOLD for f in frames]) / time_diff

        # 5. Emotion detection
        all_emotions = [
            emotion for f in frames for emotion in detect_emotions(f)]
        outside_gaze_timestamps = detect_outside_gaze(frames)
        clean_timestamps = cleanup_timestamps(outside_gaze_timestamps)

        time_stamp_list.extend(clean_timestamps)


        emotion_counts = dict(Counter(all_emotions))

        features = {
            "emotion_counts": emotion_counts,
            "blink_freq": blink_freq,
            "smile_freq": smile_freq,
            "avg_head_tilt": avg_head_tilt,
            "percent_away": percent_away
        }
        # print(features, " are the final features")
        # print(max(features['emotion_counts'],
        #       key=features['emotion_counts'].get))

        save_features_to_file(features)
        behavioral_insights = detect_behavioral_insights(frames)

        eye_contact_list.append(behavioral_insights['eye_contact'])
        facial_expressions_list.append(behavioral_insights['facial_expressions'])
        posture_list.append(behavioral_insights['posture'])
        professional_attire_list.append(behavioral_insights['professional_attire'])
        # print(eye_contact_list)
    except Exception as e:
        print(traceback.print_exc(e))
    # print(f"Behavioral Insights: {behavioral_insights}")


def detect_behavioral_insights(frames):
    """
    Analyzes all frames to detect accumulated behavioral insights across the entire video.
    """
    gaze_angles = [gaze_angle(f[5], f[6]) for f in frames]
    eye_contact_ratio = np.sum(np.array(gaze_angles) <= LOOK_AWAY_THRESHOLD_DEG) / len(gaze_angles)

    if eye_contact_ratio > 0.7:
        eye_contact = "consistent"
    elif eye_contact_ratio > 0.3:
        eye_contact = "occasional"
    else:
        eye_contact = "rare"

    all_emotions = [emotion for f in frames for emotion in detect_emotions(f)]
    if all_emotions:
        emotion_counter = Counter(all_emotions)
        most_common_emotion = emotion_counter.most_common(1)[0][0]
    else:
        most_common_emotion = "neutral"

    avg_head_tilt = np.mean([f[443] for f in frames])
    posture = "upright" if abs(avg_head_tilt) < 10 else "slouched"

    professional_attire = "yes"  # Stubbed, no visual clothing detection in this setup

    return {
        "eye_contact": eye_contact,
        "facial_expressions": most_common_emotion,
        "posture": posture,
        "professional_attire": professional_attire
    }


def summarize_results():
    global eye_contact_list
    global facial_expressions_list
    global posture_list
    global professional_attire_list
    global time_stamp_list
    global global_behavioral_insights
    global global_eye_gaze_tracking

    return {
        "behavioral_insights": {
            "eye_contact": Counter(eye_contact_list).most_common()[0][0],
            "facial_expressions": Counter(facial_expressions_list).most_common()[0][0],
            "posture": Counter(posture_list).most_common()[0][0],
            "professional_attire": Counter(professional_attire_list).most_common()[0][0],
        },
        "eye_gaze_tracking": {
            "timestamps": sorted(list(set(time_stamp_list)))
        }
    }



# Open the output CSV file and prepare to write
try:
    with open(SMOOTHED_OUTPUT_FILE, mode='w', newline='') as csvfile:
        writer = None
        print("Listening to Kafka topic: gaze-user-1")
        for message in tqdm(consumer):
            line = message.value.decode('utf-8')
            parts = next(csv.reader(io.StringIO(line.strip())))

            if parts[0] == 'frame':
                header = parts
                if 'gaze_0_x' in header and 'gaze_0_y' in header:
                    x_index = header.index('gaze_0_x')
                    y_index = header.index('gaze_0_y')
                else:
                    x_index = 5
                    y_index = 6
                header.append('smoothed_gaze_x')
                header.append('smoothed_gaze_y')
                if writer is None:
                    writer = csv.writer(csvfile)
                    writer.writerow(header)
                continue

            try:
                gaze_x = float(parts[5])
                gaze_y = float(parts[6])
            except (ValueError, IndexError) as e:
                print(f"Skipping row due to error: {e}")
                continue

            filtered_x = kf_x.update(gaze_x)
            filtered_y = kf_y.update(gaze_y)
            if writer is None and parts[0] != 'frame':
                writer = csv.writer(csvfile)
            parts.append(f"{filtered_x:.6f}")
            parts.append(f"{filtered_y:.6f}")
            writer.writerow(parts)

            # push it to a queue for feature engineering
            process_new_frame(parts)


except KeyboardInterrupt:
    result = summarize_results()
    print(result)
    # print('*'*20)
    # print({
    #     "global_behavioral_insights": global_behavioral_insights,
    #     "global_eye_gaze_tracking": global_eye_gaze_tracking
    # })
    # print('*'*20)
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")

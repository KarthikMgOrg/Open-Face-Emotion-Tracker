from kafka import KafkaProducer
import time
import os
from pathlib import Path

KAFKA_TOPIC = "gaze-user-1"
CSV_FILE_PATH = "/private/tmp/chunk_outputs/webcam.csv"


EXPECTED_COLUMNS = 470  # Adjust to match your CSV header size
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Keep track of file position


def follow_csv(file_path):
    file_path = Path(file_path)
    file_path.touch(exist_ok=True)
    with open(file_path, 'r') as f:
        header = f.readline()  # Read header
        print("CSV Header:", header.strip())

        while True:
            pos = f.tell()
            line = f.readline()

            if not line:
                time.sleep(0.1)
                f.seek(pos)  # Seek back to wait for line to complete
                continue

            if not line.endswith('\n'):
                # Incomplete line: wait for flush
                time.sleep(0.05)
                f.seek(pos)
                continue

            line = line.strip()
            if not line or line.startswith("frame") or not line[0].isdigit():
                continue

            fields = line.split(',')
            if len(fields) != EXPECTED_COLUMNS:
                print(
                    f"Incomplete row ({len(fields)} columns), skipping...")
                continue

            producer.send("gaze-user-1", value=line.encode('utf-8'))


for row in follow_csv(CSV_FILE_PATH):
    producer.send(KAFKA_TOPIC, value=row.encode('utf-8'))

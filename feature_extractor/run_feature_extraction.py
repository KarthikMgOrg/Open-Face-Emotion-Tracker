import os
import subprocess
import urllib.request
import concurrent
from concurrent.futures import ProcessPoolExecutor

OUTPUT_DIR = "/tmp"
FEATURE_EXTRACTION_PATH = "/Users/karthikeyan/openFace/OpenFace/build/bin/FeatureExtraction"
DOWNLOAD_DIR="/tmp/downloads"
# OUTPUT_FILE = os.path.join(OUTPUT_DIR, "webcam.csv")


CHUNK_DIR = "/tmp/my_output/video_chunks"


def download_data_from_url_and_split(url):
    global DOWNLOAD_FILE
    DOWNLOAD_FILE = os.path.join(DOWNLOAD_DIR, "downloaded_video.webm")

    # Ensure directories exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(CHUNK_DIR, exist_ok=True)

    # Download the video file
    urllib.request.urlretrieve(url, DOWNLOAD_FILE)
    print(f"File downloaded successfully to {DOWNLOAD_FILE}")

    # Split the video into 60-second chunks
    chunk_pattern = os.path.join(CHUNK_DIR, "chunk_%03d.webm")
    split_cmd = [
        "ffmpeg",
        "-i", DOWNLOAD_FILE,
        "-c", "copy",
        "-map", "0",
        "-segment_time", "120",
        "-f", "segment",
        chunk_pattern
    ]

    print("Splitting video into 60-second chunks...")
    subprocess.run(split_cmd, check=True)
    print(f"Chunks created in {CHUNK_DIR}")

    return CHUNK_DIR


def process_chunk(chunk_file):
    chunk_filename = os.path.basename(chunk_file)
    os.makedirs("/tmp/chunk_outputs", exist_ok=True)
    output_file = f"/tmp/chunk_outputs/output_{chunk_filename}.csv"
    
    import time
    start_time = time.time()
    print(f"Started processing {chunk_filename}...")

    cmd = [
        FEATURE_EXTRACTION_PATH,
        "-f", chunk_file,
        "-gaze",
        "-pose",
        "-aus",
        "-frame_skip","4",
        "-2Dfp",
        "-of", output_file
    ]
    proc = subprocess.Popen(cmd)
    proc.wait()
    proc.terminate()
    if proc.poll() is None:
        proc.kill()

    end_time = time.time()
    duration = end_time - start_time
    print(f"Finished processing {chunk_filename} in {duration:.2f} seconds.")
    return output_file

def launch_feature_extraction(input_url):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "chunk_outputs", "webcam.csv")
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as file:
        pass

    chunk_dir = download_data_from_url_and_split(input_url)

    chunk_files = sorted([
        os.path.join(chunk_dir, f)
        for f in os.listdir(chunk_dir)
        if f.endswith('.webm')
    ])

    print(chunk_files, " are the chunk files")

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        print('Starting concurrent processing of chunks...')
        results = list(executor.map(process_chunk, chunk_files))

    print('Combining individual chunk CSVs into final output...')
    with open(OUTPUT_FILE, 'w') as outfile:
        for idx, csv_file in enumerate(results):
            with open(csv_file, 'r') as infile:
                if idx == 0:
                    outfile.write(infile.read())
                else:
                    next(infile)  # Skip header
                    outfile.write(infile.read())

    print(f'Final combined CSV available at {OUTPUT_FILE}')

    # # Command args — customize as needed``
    # cmd = [
    #     FEATURE_EXTRACTION_PATH,
    #     # "-device", "0",
    #     "-f", DOWNLOAD_FILE,
    #     "-gaze",
    #     "-pose",
    #     "frame_skip","6",
    #     "-aus",
    #     "-2Dfp",
    #     "-of", OUTPUT_FILE
    #     # "-send_data",  # add if needed
    #     # "-zmq",        # don't add if no zmq support
    # ]
    # chunk_files = sorted(
    #     [f for f in os.listdir(CHUNK_DIR) if f.endswith('.mp4')])

    # for chunk_file in chunk_files:
    #     cmd = [
    #         FEATURE_EXTRACTION_PATH,
    #         "-f", os.path.join(CHUNK_DIR, chunk_file),
    #         "-gaze",
    #         "-pose",
    #         "-frame_skip", "6",
    #         "-aus",  # Optional: remove if you want faster processing
    #         "-2Dfp",
    #         "-of", f"/tmp/output_{chunk_file}.csv"
    #     ]
    #     subprocess.run(cmd)
    #     print("Starting FeatureExtraction...")
    # return subprocess.Popen(cmd)

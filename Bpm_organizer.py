import os
import shutil
import librosa

# Put the path of the folder you want to analyze here
directory = "path/to/your/music/folder"

tracks = {}

# For loop for each song in the folder
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Calculate the BPM
    y, sr = librosa.load(filepath)
    time, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    tracks[filename] = time

# Sort the songs based on BPM in ascending order
ordered_tracks = sorted(tracks.items(), key=lambda item: item[1])

# Create or add to the folder the sorted list
sorted_folder = os.path.join(directory, "Sorted")
os.makedirs(sorted_folder, exist_ok=True)

# Move the songs
for index, (track, _) in enumerate(ordered_tracks):
    src_path = os.path.join(directory, track)
    dest_path = os.path.join(sorted_folder, f"{index+1}_{track}")
    shutil.move(src_path, dest_path)

# Print the order to the terminal
for track, time in ordered_tracks:
    print(f"BPM for {track}: {time}")

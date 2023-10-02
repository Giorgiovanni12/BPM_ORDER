import os
import shutil
import librosa

# Metti dentro il PATH della cartella che vuoi analizzare 
directory = "dir"

tracks = {}

# For loop per ogni canzone nella cartella
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # calcola i BPM
    y, sr = librosa.load(filepath)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    tracks[filename] = tempo

# Ordina le canzoni in base al BPM in ordine crescente
ordered_tracks = sorted(tracks.items(), key=lambda item: item[1])

# Crea oppure aggiunge alla cartella la lista sistemata 
sorted_folder = os.path.join(directory, "Sistemato")
os.makedirs(sorted_folder, exist_ok=True)

# Sposta le canzoni
for index, (track, _) in enumerate(ordered_tracks):
    src_path = os.path.join(directory, track)
    dest_path = os.path.join(sorted_folder, f"{index+1}_{track}")
    shutil.move(src_path, dest_path)

# Manda a terminale l'ordine
for track, tempo in ordered_tracks:
    print(f"BPM for {track}: {tempo}")

# English Manual
Music Files Organizer
This script is designed to help you organize your music files based on their BPM (Beats Per Minute). Follow the steps below to use the script:

# 1)Clone the Repository:

```bash
git clone https://github.com/your-username/music-organizer.git
cd music-organizer
```

# 2)Install Dependencies:
Ensure you have the required dependencies installed. You can install them using:
```
pip install librosa
```
# 3)Configure the Script:
Open the Python script (organize_music.py) and update the directory variable with the path to the folder containing your music files.
```
# Change this to the directory you want to analyze
directory = "path/to/your/music/folder"
```
# 4)Run the Script:
Execute the script to organize your music files:
```
python organize_music.py
```

The script will calculate the BPM for each song, create a new folder named "Sistemato," and move the files into this folder in ascending order of BPM.

View the Results:
Once the script finishes running, you can navigate to the "Sistemato" folder to find your organized music files.

Notes
The script uses the Librosa library to calculate BPM from audio files.
Make sure to back up your music files before running the script to avoid accidental data loss.
Feel free to contribute or modify the script according to your preferences. Happy organizing!



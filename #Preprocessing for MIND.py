#Preprocessing for MIND
import os
import mne

def read_nirs_files(directory_path, file_extension=".snirf"):

    nirs_data = {}
    # Iterate through files in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(file_extension):
            file_path = os.path.join(directory_path, file_name)
            try:
                # Read the NIRS file (.snirs file)
                raw = mne.io.read_raw_snirf(file_path, preload=True)
                nirs_data[file_name] = raw
                print(f"Successfully loaded: {file_name}")
            except Exception as e:
                print(f"Failed to load {file_name}: {e}")
    
    return nirs_data

if __name__ == "__main__":
    directory_path = r"C:\Users\saish\Downloads\motion_artifacts_2\motion_artifacts_2"
    nirs_files = read_nirs_files(directory_path)
    
    # Access individual file data
    for file_name, raw_data in nirs_files.items():
        print(f"{file_name}: {raw_data.info}")

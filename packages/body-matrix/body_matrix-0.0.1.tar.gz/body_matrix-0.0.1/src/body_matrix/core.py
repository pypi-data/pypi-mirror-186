import os

def getFramesPath(sample_dir):
    frames = sorted(os.listdir(sample_dir))
    total_frames = len(frames)
    print(total_frames)
    frames_path = ["" for x in range(total_frames)]
    print(len(frames_path))
    for frame_index, frame in enumerate(frames):     
        frames_path[frame_index] = os.path.join(sample_dir + frame)
        
    return frames_path
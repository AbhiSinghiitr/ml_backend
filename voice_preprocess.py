import numpy as np
import librosa


def calculate_mfccs(audio_file, frame_length_ms=25, hop_length_ms=None, num_mfcc=12, num_mel_bins=26):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Calculate frame length and hop length in samples
    frame_length = int(sr * (frame_length_ms / 1000))
    if hop_length_ms is None:
        hop_length = int(frame_length / 2)  # 50% overlap
    else:
        hop_length = int(sr * (hop_length_ms / 1000))

    # Extract Mel spectrogram
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=frame_length, hop_length=hop_length, n_mels=num_mel_bins)

    # Calculate MFCCs
    mfccs = librosa.feature.mfcc(S=librosa.power_to_db(mel_spec), n_mfcc=num_mfcc)


    mfccs_mean = np.mean(mfccs, axis=1)
    mfccs_std = np.std(mfccs, axis=1)

    return mfccs_mean,mfccs_std


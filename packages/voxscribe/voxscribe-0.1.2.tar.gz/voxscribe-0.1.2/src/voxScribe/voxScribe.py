import os
from datetime import datetime
from pathlib import Path

import requests
import speech_recognition
from pydub import AudioSegment

from whosYourAgent import getAgent

root = Path(__file__).parent

""" Extract text from an mp3 or wav file. """


def downloadAudioFile(url: str, fileExt: str) -> Path:
    """Downloads an audio file to
    a folder named audio in
    the same folder as this file.

    :param fileExt: Can be either '.mp3' or '.wav'.

    Returns a Path object for the
    saved file."""
    dest = root / "audio"
    dest.mkdir(parents=True, exist_ok=True)
    filePath = (dest / str(datetime.now().timestamp())).with_suffix(fileExt)
    source = requests.get(url, headers={"User-Agent": getAgent()})
    with filePath.open("wb") as file:
        file.write(source.content)
    return filePath


def convertMp3ToWav(mp3Path: Path | str) -> Path:
    """Converts an mp3 file to a wav file
    of the same name, deletes the mp3 file,
    and returns a Path object for the wav file."""
    mp3Path = Path(mp3Path)
    audio = AudioSegment.from_mp3(mp3Path)
    wavPath = mp3Path.with_suffix(".wav")
    audio.export(wavPath, format="wav")
    mp3Path.unlink()
    return wavPath


def getTextFromUrl(url: str, fileExt: str) -> str:
    """Returns text from an mp3 file
    located at the given url.

    :param fileExt: Can be either '.mp3' or '.wav'"""
    audioPath = downloadAudioFile(url, fileExt)
    if fileExt == ".mp3":
        return getTextFromWav(convertMp3ToWav(audioPath))
    elif fileExt == ".wav":
        return getTextFromWav(audioPath)
    else:
        raise Exception('fileExt param must be ".mp3" or ".wav"')


def getTextFromWav(wavPath: Path | str) -> str:
    """Returns text from a wav file
    located at the give file path."""
    wavPath = Path(wavPath)
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(str(wavPath)) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    wavPath.unlink()
    return text


def getTextFromMp3(mp3Path: Path | str) -> str:
    """Returns text from an mp3 file
    located at the give file path."""
    return getTextFromWav(convertMp3ToWav(mp3Path))


def cleanUp():
    """Removes any files from the audio directory
    older than 5 minutes."""
    audioDir = root / "audio"
    if audioDir.exists():
        for file in (root / "audio").glob("*.*"):
            if (datetime.now().timestamp() - os.stat(file).st_ctime) > (60 * 5):
                file.unlink()

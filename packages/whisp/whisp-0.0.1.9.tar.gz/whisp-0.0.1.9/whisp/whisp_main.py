import whisper
from enum import Enum
from typing import Union
from pathlib import Path

LANGUAGE = "english"

class MODEL(str, Enum):
    tiny = "tiny",
    base = "base",
    small = "small",
    medium = "medium",
    large = "large"

    def __str__(self) -> str:
        return self.value

class MODEL_EN(str, Enum):
    tiny = "tiny.en",
    base = "base.en",
    small = "small.en",
    medium = "medium.en"

    def __str__(self) -> str:
        return self.value

def recognize(model: Union[MODEL, MODEL_EN], audio: Path, language=LANGUAGE):
    mod = whisper.load_model(model)

    ## audio = whisper.load_audio("audio.mp3")

    options = whisper.DecodingOptions()
    result = mod.transcribe(audio)

    print(result.text)
# print the recognized text

from enum import Enum
from typing import Union
from pathlib import Path
from whisp import Whisper

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
    mod = Whisper.load_model(model)

    ## audio = Whisper.load_audio("audio.mp3")

    options = Whisper.DecodingOptions()
    result = mod.transcribe(audio)

    print(result.text)
# print the recognized text

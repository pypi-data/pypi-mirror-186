from enum import Enum
from typing import Union
from pathlib import Path
from whisp import Whisper
import sys

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

def recognize(model: Union[MODEL, MODEL_EN], audio, language=LANGUAGE):
    mod = Whisper.load_model(model)

    audio_load = Whisper.load_audio(audio)
    audio_load = Whisper.pad_or_trim(audio_load)
    mel = Whisper.log_mel_spectrogram(audio_load).to(mod.device)
    _, probs = mod.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    result = mod.transcribe(audio_load, fp16=False)

    sys.stdout.write(result["text"])

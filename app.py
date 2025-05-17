import torch
import soundfile as sf
from kokoro import KPipeline
from pydantic import BaseModel, Field
from typing import Optional, List
import inferless
import base64
import io

@inferless.request
class RequestObjects(BaseModel):
    text: str = Field(default="Hello world, this is a test.")
    voice: Optional[str] = "af_heart"
    speed: Optional[float] = 1.0
    split_pattern: Optional[str] = r'\n+'

@inferless.response
class ResponseObjects(BaseModel):
    audio_base64: List[str] = Field(default="Test output")
    graphemes: List[str] = Field(default="Test output")
    phonemes: List[str] = Field(default="Test output")

class InferlessPythonModel:
    def initialize(self):
        self.pipeline = KPipeline(lang_code='a')

    def infer(self, request: RequestObjects) -> ResponseObjects:
        generator = self.pipeline(
            request.text,
            voice=request.voice,
            speed=request.speed,
            split_pattern=request.split_pattern
        )

        audio_base64_list = []
        graphemes = []
        phonemes = []

        for gs, ps, audio in generator:
            buffer = io.BytesIO()
            sf.write(buffer, audio, samplerate=24000, format='WAV')
            audio_bytes = buffer.getvalue()
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
            
            audio_base64_list.append(audio_base64)
            graphemes.append(gs)
            phonemes.append(ps)

        return ResponseObjects(
            audio_base64=audio_base64_list,
            graphemes=graphemes,
            phonemes=phonemes
        )

    def finalize(self):
        self.pipeline = None

import torch
import soundfile as sf
from kokoro import KPipeline
import base64
import io

class InferlessPythonModel:
    def initialize(self):
        self.pipeline = KPipeline(lang_code='a')

    def infer(self, inputs, stream_output_handler):
        text = inputs['text']
        voice = inputs.get("voice","af_heart")
        split_pattern = inputs.get("split_pattern",'\n+')
        
        generator = self.pipeline(
            text,
            voice=voice,
            speed=1.0,
            split_pattern=split_pattern
        )

        for gs, ps, audio in generator:
            buffer = io.BytesIO()
            sf.write(buffer, audio, samplerate=24000, format='WAV')
            audio_bytes = buffer.getvalue()
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
            stream_output_handler.send_streamed_output({"OUT" : audio_base64})
            
        stream_output_handler.finalise_streamed_output()

    def finalize(self):
        self.pipeline = None

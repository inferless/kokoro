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
        # speed = inputs.get("speed",1.0)
        split_pattern = inputs.get("split_pattern",'\n+')
        
        generator = self.pipeline(
            text,
            voice=voice,
            speed=1.0,
            split_pattern=split_pattern
        )
        audio_base64_list = []
        graphemes = []
        phonemes = []

        for gs, ps, audio in generator:
            sample_rate = 24000
            buffer = io.BytesIO()
            sf.write(buffer, audio, sample_rate, format='WAV')
            buffer.seek(0)
            base64_audio = base64.b64encode(buffer.read()).decode('utf-8')
            output_dict = {}
            output_dict["OUT"] = base64_audio
            stream_output_handler.send_streamed_output(output_dict)
            
        stream_output_handler.finalise_streamed_output()

    def finalize(self):
        self.pipeline = None

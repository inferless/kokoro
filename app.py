import torch
import soundfile as sf
from kokoro import KPipeline
import base64
import io

class InferlessPythonModel:
    def initialize(self):
        self.pipeline = KPipeline(lang_code='a')

    def infer(self, inputs, stream_output_handler):
        try:
            
            text = '''The sky above the port was the color of television, tuned to a dead channel. "It's not like I'm using," Case heard someone say, as he shouldered his way through the crowd around the door of the Chat. "It's like my body's developed this massive drug deficiency." It was a Sprawl voice and a Sprawl joke. The Chatsubo was a bar for professional expatriates; you could drink there for a week and never hear two words in Japanese. These were to have an enormous impact, not only because they were associated with Constantine, but also because, as in so many other areas, the decisions taken by Constantine (or in his name) were to have great significance for centuries to come. One of the main issues was the shape that Christian churches were to take, since there was not, apparently, a tradition of monumental church buildings when Constantine decided to help the Christian church build a series of truly spectacular structures. The main form that these churches took was that of the basilica, a multipurpose rectangular structure, based ultimately on the earlier Greek stoa, which could be found in most of the great cities of the empire. Christianity, unlike classical polytheism, needed a large interior space for the celebration of its religious services, and the basilica aptly filled that need. We naturally do not know the degree to which the emperor was involved in the design of new churches, but it is tempting to connect this with the secular basilica that Constantine completed in the Roman forum (the so-called Basilica of Maxentius) and the one he probably built in Trier, in connection with his residence in the city at a time when he was still caesar. [Kokoro](/kˈOkəɹO/) is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. With Apache-licensed weights, [Kokoro](/kˈOkəɹO/) can be deployed anywhere from production environments to personal projects'''
            print(inputs['text'],flush=True)
            
            voice = inputs.get("voice","af_heart")
            print(voice,flush=True)

            split_pattern = inputs.get("split_pattern",'\n+')
            print(split_pattern,flush=True)

            # Hard Coding
            voice = "af_heart"
            split_pattern = '\n+'
            
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
                print(base64_audio[:100],flush=True)
                output_dict = {}
                output_dict["OUT"] = base64_audio
                
                stream_output_handler.send_streamed_output(output_dict)
                
            stream_output_handler.finalise_streamed_output()

        except Exception as e:
            print(e,flush=True)
            
    def finalize(self):
        self.pipeline = None

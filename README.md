# CreatorVideo V3.5

An open-source research/engineering foundation for multimodal, long-form video generation.

## Our official website: https://hydransec.online/CreatorAI/index.html

**Important:** this is an independent implementation scaffold, weights, private APIs, or copyrighted training data.

## Target capabilities
- Text-to-video and image-to-video interfaces
- Text/image/video/audio conditioning
- Character, object, scene and temporal consistency
- Camera and motion conditioning
- Hierarchical long-form generation
- 720p / 1080p / 2K / 4K output pipeline
- Audio, speech, SFX and lip-sync interfaces
- Local inference + HTTP API
- Training and evaluation scaffolding
- Python/JavaScript SDKs

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn openvideo.api.server:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs`.

## Reality check
The included API defaults to a mock backend so the complete service can be tested without model
weights. It is **not a trained frontier model**. Commercial-level quality requires a large,
properly licensed dataset, trained checkpoints, distributed GPU training, evaluation and alignment.

See `docs/` for architecture, training, API, open-source and deployment guides.

## More
As I do not have sufficient funds to train this AI video generation large model, I can only open-source this commercial-grade video generation large model framework for individuals or enterprises with the necessary funds to train it. Currently, this model framework can generate 1080p/2k/4k videos, which are similar to the current Seedance effect. We will continue to develop this model framework in the future. Thank you for your support!
If I can sponsor it, I would be more than happy. I hope this project can flourish and help more people

# 使用方法

## API
`pip install -r requirements.txt`
`uvicorn openvideo.api.server:app --host 0.0.0.0 --port 8000`

Create:
`POST /v1/videos`
JSON:
`{"prompt":"cinematic sci-fi journey","duration":120,"resolution":"1080p","fps":24,"aspect_ratio":"16:9"}`

Query:
`GET /v1/videos/{id}`

Plan:
`GET /v1/video/plan?prompt=...&duration=120`

## Python
```python
from openvideo.sdk.python import VideoClient
client=VideoClient()
task=client.generate(prompt="cinematic sci-fi",duration=120,resolution="1080p",fps=24)
print(task)
```

The reference API uses a mock backend. Replace it with a trained checkpoint for actual video output.

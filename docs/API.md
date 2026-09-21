# API

- `POST /v1/videos` create generation task
- `GET /v1/videos/{id}` query task
- `GET /v1/models` list model IDs
- `GET /v1/video/plan` create long-video shot plan

Supported resolution values: `720p`, `1080p`, `2k`, `4k`.
The reference server accepts 1-3600 seconds as an orchestration parameter; actual model limits depend
on the trained checkpoint and available compute.

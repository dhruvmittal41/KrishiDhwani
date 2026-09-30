# Proposed API contract

All feature endpoints are placeholders and currently return 501.

| Method | Route | Planned behaviour |
|---|---|---|
| GET | /health | Reports scaffold status today |
| POST | /audio | Accept authenticated WAV + metadata; enqueue; return clip receipt |
| GET | /results | Paginated results by node, zone and time |
| GET | /nodes | Configured zones and node freshness |
| POST | /feedback | Human verification linked to a result |

Audio upload will be multipart with a WAV file and metadata JSON. Maximum size, duration, authentication and retention policy must be implemented before exposure. See examples/result.synthetic.json for the proposed result shape. It is fabricated UI data, not an inference result.

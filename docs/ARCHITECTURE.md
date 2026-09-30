# Architecture contract

Nodes capture and filter; the Pi classifies. LoRa is not used.

## Capture and transport

Use node_id, clip_id, sequence, captured_at, sample_rate_hz, bit_depth, channels, duration_ms and filter_version with each upload. Hardware clock synchronisation is pending; server received_at must also be retained. Assign each node to a configured zone.

Use bounded local buffers and upload queues, acknowledgements, backoff and duplicate detection. Stagger uploads when nodes compete. Packetisation alone does not compress audio. Choose sampling rate from the actual target frequencies and microphone response; validate filters so they preserve insect cues.

## Central processing

Validate type, size and duration before decoding. Store clips under generated IDs, never client filenames. Authenticate nodes before enabling LAN exposure. Queue inference outside request handlers, reject overload explicitly and track node heartbeats. Configure retention and deletion. Persist results and inspection feedback separately.

## Connectivity

Phone and nodes join the Pi local network. The Pi needs an access-point-capable Wi-Fi interface. A local network is not an internet connection. Off-site app access is a separate future feature.

from openvideo.sdk.python import VideoClient
client=VideoClient()
print(client.generate(prompt="a cinematic astronaut entering a wormhole",duration=120,resolution="1080p",fps=24))

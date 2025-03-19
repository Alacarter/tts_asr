import pyaudio

p = pyaudio.PyAudio()
device_index = None

# List available devices and find an input device
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print(f"Device {i}: {dev['name']} (Input Channels: {dev['maxInputChannels']})")
    if dev['maxInputChannels'] > 0:  # Looking for an input device
        device_index = i

if device_index is None:
    raise RuntimeError("No input microphone detected!")

# Open the input stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=device_index)
print("Audio stream successfully opened!")
print(f"Using input device {device_index}")
stream.close()


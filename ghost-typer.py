import soundfile as sf
import sounddevice as sd
from time import sleep
from random import uniform

data = """
class MyClass():
	def foo(bar=123):
		return bar
MyClass::foo(456)
"""

data = data.strip()

print('\033[H\033[J', end="", flush=True)

samples, samplerate = sf.read('key_click_short.wav')
sleep(1)
for i, c in enumerate(data, start=1):
    if str(c) in [" ", "\n"]:
        delay = uniform(0.01, 0.02)
    elif str(c).isdigit():
        delay = uniform(0.04, 0.05)
    elif str(c).isupper():
        delay = uniform(0.03, 0.04)
    elif str(c).isalpha():
        delay = uniform(0.02, 0.03)
    else:
        delay = uniform(0.05, 0.06)
    delay = delay + 0.025
    delay = delay * ((uniform(1.0, 1.1) * uniform(1.0, 1.1) * uniform(1.0, 1.1)) / 3)
    sleep(delay)
    print(c, end="", flush=True)
    sd.play(samples, samplerate)
#	sd.wait()

print("")

sleep(1)

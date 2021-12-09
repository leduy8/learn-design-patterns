from timeline import Timeline
from context_menu import ContextMenu
from audio import Audio
from clip import Clip
from text import Text


timeline = Timeline()
menu = ContextMenu(timeline)

audio = Audio("yo123.mp3")
timeline.add(audio)

clip = Clip("aaa.mp4")
timeline.add(clip)

text = Text("Helloooooo")
timeline.add(text)

menu.duplicate(text)
timeline.print_timeline()
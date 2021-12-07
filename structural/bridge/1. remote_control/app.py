from remote_control import RemoteControl
from advance_remote_control import AdvanceRemoteControl
from sony_tv import SonyTV
from samsung_tv import SamsungTV


remote_control = RemoteControl(SonyTV())
remote_control.turn_on()
remote_control.turn_off()

remote_control2 = AdvanceRemoteControl(SamsungTV())
remote_control2.turn_on()
remote_control2.set_channel(2)
remote_control2.turn_off()
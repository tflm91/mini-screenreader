from comtypes import client
import win32com.client
import time

automation = client.createObject(
    'UIAutomationClient.CUIAutomation'
)

root = automation.GetRootElement()

def on_focus_changed(sender, _):
    name = sender.CurrentName
    role = sender.ControlType
    print(name, role)
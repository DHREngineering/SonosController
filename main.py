import soco
import requests
import re
from time import sleep

XML ="""<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" 
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body>{}</s:Body></s:Envelope>
"""

HEADRS = {'Content-Type': 'text/xml; charset="utf-8"'}

class xmls:
    next = XML.format('<u:Next xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Next>')
    prev = XML.format('<u:Previous xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Previous>')

    volume = XML.format("""<u:GetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1"><InstanceID>0</InstanceID><Channel>Master</Channel></u:GetVolume>""")
    volume_chng = """<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1"><InstanceID>0</InstanceID><Channel>Master</Channel><DesiredVolume>{}</DesiredVolume></u:SetVolume></s:Body></s:Envelope>"""
    
    play = XML.format("""<u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Play>""")
    stop = XML.format("""<u:Stop xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Stop>""")
    pause = XML.format("""<u:Pause xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Pause>""")

class hdrs:
    volume ={'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"} 
    play = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Play"}
    stop = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Stop"}
    pause = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Pause"}
    next = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Next"}
    prev = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Previous"}
    volume_chng = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"}

class Sonos:
    def __init__(self, player_name):
        self.device = None
        devices = list(soco.discover())
        print(devices)
        for s in devices:
            if s.player_name == player_name:
                self.device = s 

    def volume_up(self, value):
        new_volume = self.volume + value
        if new_volume > 100:
            new_volume = 100
        self.__run_rdctrl(xmls.volume_chng.format(new_volume), hdrs.volume_chng)

    def volume_down(self, value):
        new_volume = self.volume - value
        if new_volume < 0:
            new_volume = 0
        self.__run_rdctrl(xmls.volume_chng.format(new_volume), hdrs.volume_chng)

    def play(self):
        self.__run_avt(hdrs.play, xmls.play)

    def stop(self):
        self.__run_avt(hdrs.stop, xmls.stop)

    def pause(self):
        self.__run_avt(hdrs.pause, xmls.pause)

    def next(self):
        self.__run_avt(hdrs.next, xmls.next)

    def previous(self):
        self.__run_avt(hdrs.prev, xmls.prev)

    def __run_avt(self, hdr, xml):
        requests.post('http://192.168.1.16:1400/MediaRenderer/AVTransport/Control', headers=hdr, data=xml)
    
    @property
    def volume(self):
        r = False
        r = self.__run_rdctrl(xmls.volume, hdrs.volume)
        return int(re.findall(r'[0-9]+', r.text)[1]) 

    def __run_rdctrl(self, xml, hdr):
        return requests.post('http://192.168.1.16:1400/MediaRenderer/RenderingControl/Control', headers=hdr, data=xml)
        
    
s = Sonos('Office')

s.play()
sleep(1)


s.volume_up(11)
s.next()
sleep(10)
s.volume_down(10)
s.pause()



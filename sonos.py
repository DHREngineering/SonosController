try:
    import requests
    import socket
    import select
except:
    import urequests as requests
    import usocket as socket
    import uselect as select

from time import sleep
from sonos_definitions import * #all constant(uppercase) variables

"""
class SonosDiscovery:
    Finds Sonos speakers within a local network using Simple Service Discovery Protocol
"""
class SonosDiscovery:
    
    """
    Contructor:
        sets the socket configuration for the Simple Service Discovery Protocol
    """
    def __init__(self):
        self._sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        IP_MULTICAST_TTL = 33
        self._sock.setsockopt(socket.IPPROTO_IP, IP_MULTICAST_TTL, 2)

    
    """
    Receive the ip of all the found Sonos speakers
    @return spearkers list of ip speakers' addresses
    """
    def get_speaker_ips(self):
        speakers = []

        self._sock.sendto(PLAYER_SEARCH, (MCAST_GRP, MCAST_PORT))

        while True:
            rs, _, _ = select.select([self._sock], [], [], 1)
            if rs:
                _, addr = self._sock.recvfrom(2048)
                speakers.append(addr[0])
            else:
                break
        return speakers

"""
class Sonos:
    Sonos Speaker controller
"""
class Sonos:
    """
    Constructor:
        finds the ip address of the speaker with given name 
        @param name name of the speaker
    """
    def __init__(self, name):
        ips = SonosDiscovery().get_speaker_ips()
        self.ip = None
        for ip in ips:
            link = "http://" + ip + ":1400/status/zp"
            xml = requests.get(link).text
            if self._get_name(xml) == name:
                self.ip = ip
                break
        self.http = "http://" + self.ip + ":1400/"

    
    """
    Extracts the ZoneName from  <ip>:1400/status/zp xml respnose
        @param xml <ip>:1400/status/zp xml respnose
        @return name the name of the speaker
    """
    def _get_name(self, xml):
        name = xml.split("ZoneName>")[1][:-2]
        return name

    
    """
    Turns the volume up
        @param value integer to increment the volume
    """
    def volume_up(self, value):
        new_volume = self.volume + value
        
        if new_volume > 100:
            new_volume = 100
        
        vc = VOLUME_CHNG_XML_1 + str(new_volume) + VOLUME_CHNG_XML_2
        
        self.__run_rdctrl(vc, VOLUME_CHNG_HDRS)

    
    """
    Turns the volume down
        @param value integer to dencrement the volume
    """
    def volume_down(self, value):
        new_volume = self.volume - value
        
        if new_volume < 0:
            new_volume = 0
        
        vc = VOLUME_CHNG_XML_1 + str(new_volume) + VOLUME_CHNG_XML_2
        
        self.__run_rdctrl(vc, VOLUME_CHNG_HDRS)
    
    
    """
    Send play command to Sonos
    """
    def play(self):
        self.__run_avt(PLAY_HDRS, PLAY_XML)

    
    """
    Send stop command to Sonos
    """
    def stop(self):
        self.__run_avt(STOP_HDRS, STOP_XML)

    
    """
    Send pause command to Sonos
    """
    def pause(self):
        self.__run_avt(PAUSE_HDRS, PAUSE_XML)

    
    """
    Send next command to Sonos
    """
    def next(self):
        self.__run_avt(NEXT_HDRS, NEXT_XML)

    
    """
    Send previous command to Sonos
    """
    def previous(self):
        self.__run_avt(PREV_HDRS, PREV_XML)

    
    """
    Send data to <ip>:1400/MediaRenderer/AVTransport/Control
        @param xml xml configuration
        @param hdr http headers
        @return html response body
    """
    def __run_avt(self, hdr, xml):
        link = self.http + "MediaRenderer/AVTransport/Control"
        return requests.post(link, headers=hdr, data=xml)
    
    
    """
    Property function for getting the current speaker state
        @return string of the current speaker state
    """
    @property
    def state(self):
        r = self.__run_avt(STATE_HDRS, STATE_XML)
        return r.text.split("CurrentTransportState>")[1][:-2]
    
    
    """
    Property fuction for getting the current volume
        @return integer value of the curretn volume
    """
    @property
    def volume(self):
        r = False
        r = self.__run_rdctrl(VOLUME_XML, VOLUME_HDRS)
        return int(r.text.split("CurrentVolume>")[1][:-2]) 
    
    
    """
    Send data to <ip>:1400/MediaRenderer/RenderingControl/Control
        @param xml xml configuration
        @param hdr http headers
        @return html response body
    """
    def __run_rdctrl(self, xml, hdr):
        link = self.http + "MediaRenderer/RenderingControl/Control"
        return requests.post(link, headers=hdr, data=xml)

"""
test example
"""
if __name__ == "__main__":
    s = Sonos('Office')
    for _ in range(60):
        s.play()
        sleep(0.5)
        s.stop()
        sleep(0.5)

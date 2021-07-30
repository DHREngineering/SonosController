"""
Predifined constants to be imported in sonos.py
"""


XML ="""<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body>{}</s:Body></s:Envelope>
"""

PLAYER_SEARCH = b"""M-SEARCH * HTTP/1.1
HOST: 239.255.255.250:reservedSSDPport
MAN: ssdp:discover
MX: 1
ST: urn:schemas-upnp-org:device:ZonePlayer:1"""

MCAST_GRP = "239.255.255.250"

MCAST_PORT = 1900

NEXT_XML = """<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:Next xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Next></s:Body></s:Envelope>
"""

PREV_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:Previous xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Previous></s:Body></s:Envelope>
"""

PLAY_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Play>
</s:Body></s:Envelope>
"""

STOP_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:Stop xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Stop>
</s:Body></s:Envelope>
"""

PAUSE_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:Pause xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Speed>1</Speed></u:Pause>
</s:Body></s:Envelope>
"""

STATE_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:GetTransportInfo xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID></u:GetTransportInfo>
</s:Body></s:Envelope>
"""
VOLUME_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:GetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1"><InstanceID>0</InstanceID><Channel>Master</Channel></u:GetVolume>
</s:Body></s:Envelope>
"""

POSITION_INFO_XML = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" 
s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<s:Body><u:GetPositionInfo xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID><Channel>Master</Channel></u:GetPositionInfo>
</s:Body></s:Envelope>
"""



VOLUME_CHNG_XML_1 = """<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1"><InstanceID>0</InstanceID><Channel>Master</Channel><DesiredVolume>"""
VOLUME_CHNG_XML_2 = """</DesiredVolume></u:SetVolume></s:Body></s:Envelope>"""


POSITION_INFO_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#GetPositionInfo"} 
VOLUME_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"}
PLAY_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Play"}
STOP_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Stop"}
PAUSE_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Pause"}
NEXT_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Next"}
PREV_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:AVTransport:1#Previous"}
VOLUME_CHNG_HDRS = {'Content-Type': 'text/xml; charset="utf-8"',"soapaction":"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"}
STATE_HDRS = {'Content-Type' : 'text/xml; charset="utf-8"', "soapaction": "urn:schemas-upnp-org:service:AVTransport:1#GetTransportInfo"}






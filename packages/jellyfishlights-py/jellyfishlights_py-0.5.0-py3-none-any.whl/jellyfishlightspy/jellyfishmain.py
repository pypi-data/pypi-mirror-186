# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
#TODO: get rid of above once this is done

import websocket
import json

from typing import Dict
from typing import List
from typing import Tuple
from jellyfishlightspy.runPattern import *
from jellyfishlightspy.runPatternData import *
from jellyfishlightspy.getData import *
from dataclasses import dataclass

class Light:
    """Represents a single light on an Led strip"""
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

#Do we NEED a wrapper for a List[Light]?
class LightString:
    """Represents a series of Lights on an led strip"""
    lights: List[Light]
    def __init__(self, lightz: List[Light] = None):
        self.lights = [] if lightz is None else lightz

    def add(self, light: Light):
        self.lights.append(light)

@dataclass
class PatternName:
    name: str
    folder: str

    def toFolderAndName(self):
        return f'{self.folder}/{self.name}'

#TODO: adding and setting patterns, schedules, and zones
#TODO: get current schedule
#TODO: add a way to get the current pattern (runPattern)
#TODO: add use of prebuilt pattern types
class JellyFishController:
    zones: Dict = {}
    patternFiles: List[PatternName] = []
    __ws = websocket.WebSocket()
    __address: str
    __printJSON: bool

    def __init__(self, address: str, printJSON: bool = False):
        self.__address = address
        self.__printJSON = printJSON
    
    def __send(self, message: str):
        if self.__printJSON:
            print(f"Sending: {message}")
        self.__ws.send(message)

    def __recv(self):
        message = self.__ws.recv()
        if self.__printJSON:
            print(f"Recieved: {message}")
        return message
    
    @property
    def connected(self) -> bool:
        return self.__ws.connected

    def getAndStorePatterns(self) -> List[PatternName]:
        """Returns and stores all the patterns from the controller"""
        patternFiles = self.__getData(["patternFileList"])
        for patternFile in patternFiles:
            if patternFile["name"] != "":
                self.patternFiles.append(PatternName(patternFile["name"], patternFile["folders"]))
        return self.patternFiles

    def getAndStoreZones(self) -> Dict:
        """Returns and stores zones, including their port numbers"""
        zones = self.__getData(["zones"])
        self.zones = zones
        return self.zones

    def getRunPattern(self, zone: str=None) -> RunPatternClass:
        """Returns runPatternClass"""
        if not zone:
            zone = list(self.zones.keys())[0]
        runPatterns = self.__getData(["runPattern", zone])
        runPatternsClass = RunPatternClassFromDict(runPatterns)
        return runPatternsClass

    def getRunPatterns(self, zones: List[str]=None) -> Dict[str, RunPatternClass]:
        if not zones:
            zones = list(self.zones.keys())
        runPatterns = {}
        for zone in zones:
            runPatterns[zone] = self.getRunPattern(zone)
        return runPatterns

    def __getData(self, data: List[str]) -> any:
        gd = GetData(cmd='toCtlrGet', get=[data])
        self.__send(json.dumps(gd.to_dict()))
        return json.loads(self.__recv())[data[0]]
    
    #Attempts to connect to a controller at the given address
    def connect(self):
        try:
            self.__ws.connect(f"ws://{self.__address}:9000")
        except:
            raise BaseException("Could not connect to controller at " + self.__address)
        
    # Disconnects the web socket connection
    def disconnect(self):
        try:
            self.__ws.close()
        except:
            raise BaseException("Error encountered while disconnecting from controller at " + self.__address)

    #Attempts to connect to a controller at the given address and retrieve data
    def connectAndGetData(self):
        try:
            self.connect()
            self.getAndStoreZones()
            self.getAndStorePatterns()
        except Exception as e:
            raise BaseException("Error connecting or getting data: ", e)
        

    def playPattern(self, pattern: str, zones: List[str] = None):
        rpc = RunPatternClass(
            state=1,
            zoneName=zones or list(self.zones.keys()),
            file=pattern,
            data="",
        )

        rp = RunPattern(cmd="toCtlrSet", runPattern=rpc)
        self.__send(json.dumps(rp.to_dict()))
        self.__recv() # need to read the response even if doing nothing with the result

    def turnOnOff(self, turnOn: bool, zones: List[str] = None):
        zones = zones or list(self.zones.keys())
        rpc = RunPatternClass(
            state=1 if turnOn else 0,
            zoneName=zones,
            data="",
        )

        rp = RunPattern(cmd="toCtlrSet", runPattern=rpc)
        self.__send(json.dumps(rp.to_dict()))
        # need to read the response even if doing nothing with the result
        # on/off can return multiple responses, so ensure to read them all
        zones = set(zones)
        state = int(turnOn)
        while True:
            data = json.loads(self.__recv())
            if  (
                'runPattern' in data 
                and data['runPattern']['state'] ==  state 
                and set(data['runPattern']['zoneName']) == zones
            ):
                break

    def turnOn(self, zones: List[str] = None):
        self.turnOnOff(True, zones or list(self.zones.keys()))

    def turnOff(self, zones: List[str] = None):
        self.turnOnOff(False, zones or list(self.zones.keys()))

    def sendLightString(self, lightString: LightString, zones: List[str] = None):
        colors = [0,0,0]
        colorsPos = [-1]
        for i, light in enumerate(lightString.lights):
            colors.extend((light.red, light.green, light.blue))
            colorsPos.append(i)

        rd = RunData(speed=0, brightness=100, effect="No Effect", effectValue=0, rgbAdj=[100,100,100])
        rpd = RunPatternData(colors=colors, colorPos=colorsPos, runData=rd, type="Soffit")
        rpc = RunPatternClass(
            state=3,
            zoneName=zones or list(self.zones.keys()),
            data=json.dumps(rpd.to_dict()),
        )

        rp = RunPattern(cmd="toCtlrSet", runPattern=rpc)
        self.__send(json.dumps(rp.to_dict()))
        self.__recv() # need to read the response even if doing nothing with the result

    def sendColor(self, rgb: Tuple[int,int,int], brightness: int = 100, zones: List[str] = None):
        rd = RunData(speed=10, brightness=brightness, effect="No Effect", effectValue=0, rgbAdj=[100,100,100])
        rpd = RunPatternData(colors=[*rgb], type="Color", skip=1, direction="Left", runData=rd)
        rpc = RunPatternClass(
            state=1,
            zoneName=zones or list(self.zones.keys()),
            data=json.dumps(rpd.to_dict()),
        )
        
        rp = RunPattern(cmd="toCtlrSet", runPattern=rpc)
        self.__send(json.dumps(rp.to_dict()))
        self.__recv() # need to read the response even if doing nothing with the result
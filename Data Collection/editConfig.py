import json


class EditConfig:
    def __init__(self, temp=''):
        self.__filepath = temp

    def readConfig(self):
        try:
            with open(self.__filepath) as f:
                return json.load(f)
        except:
            return None

    def addSample(self, val=''):
        try:
            jsonDict = self.readConfig()
            jsonDict[str(len(jsonDict))] = val
            with open(self.__filepathfilepath, 'w') as f:
                json.dump(jsonDict, f, indent=2)
                return True
        except:
            return False

    def countSamples(self):
        try:
            return len(self.readConfig())
        except:
            return 0

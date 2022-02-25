# No restrictions on use
# © 2021 Greg Ritacco

import jmri
import json
import time
import csv
from HTMLParser import HTMLParser
from codecs import open as codecsOpen
from os import mkdir as osMakeDir

scriptName ='OperationsExportToTrainPlayer'
scriptRev = 20220105

class CheckDestinationDirectory(jmri.jmrit.automat.AbstractAutomaton):
    '''Verify or create a destination directory'''

    def init(self):
        self.scriptName = 'OperationsExportToTrainPlayer.CheckDestinationDirectory'
        self.scriptRev = 20220105

        return

    def handle(self):

        try:
            osMakeDir(jmri.util.FileUtil.getHomePath() + 'AppData\\Roaming\\TrainPlayer\\Reports')
            print('Destination directory created')
        except OSError:
            print('Destination directory OK')

        return False

class LocationsForTrainPlayer(jmri.jmrit.automat.AbstractAutomaton):
    '''Writes a list of location names and comments for the whole profile'''

    def init(self):
        self.scriptName = 'OperationsExportToTrainPlayer.LocationsForTrainPlayer'
        self.scriptRev = 20220105
        self.jLM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.locations.LocationManager)
        self.toLoc = jmri.util.FileUtil.getHomePath() + "AppData\Roaming\TrainPlayer\Reports\JMRI - Locations.csv"

        return

    def handle(self):
        jEncoding = 'utf-8'
        jTimeNow = time.time()
        eMessage = 'No location errors'
        locationList = self.jLM.getLocationsByIdList()
        with codecsOpen(self.toLoc, 'wb', encoding=jEncoding) as csvWorkFile:
            csvLocations = u'Locale,Industry\n'
            for location in locationList:
                jLocTrackList = location.getTrackIdsByIdList()
                for track in jLocTrackList:
                    jTrackId = location.getTrackById(track)
                    jLocale = unicode(location.getName(), jEncoding) + u';' + unicode(jTrackId.getName(), jEncoding)
                    jTrackComment = unicode(jTrackId.getComment(), jEncoding)
                    if not (jTrackComment):
                        jTrackComment = 'Null'
                        eMessage = 'Missing location comment entries'
                    csvLocations = csvLocations + jLocale + ',' + jTrackComment + '\n'
            csvWorkFile.write(csvLocations)
        print(eMessage)
        print('Locations export (sec): ' + ('%s' % (time.time() - jTimeNow))[:6])

        return False

class ManifestForTrainPlayer(jmri.jmrit.automat.AbstractAutomaton):
    '''Writes a CSV manifest from the trains JSON file'''
    # CSV Writer does not support Unicode

    def init(self):
        self.scriptName = 'OperationsExportToTrainPlayer.ManifestForTrainPlayer'
        self.scriptRev = 20220105
        self.jTM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.trains.TrainManager)
        self.jProfilePath = jmri.util.FileUtil.getProfilePath()

        return

    def timeStamp(self):
        '''Valid Time, get local time adjusted for time zone and dst'''

        epochTime = time.time()
        if (time.localtime(epochTime).tm_isdst and time.daylight): # If local dst and dst are both 1
            timeOffset = time.altzone
        else:
            timeOffset = time.timezone # in seconds

        return time.strftime('%a %b %d %Y %I:%M %p %Z', time.gmtime(epochTime - timeOffset))

    def parseLoco(self, xLoco):
        jFrom = xLoco[u'location'][u'userName'] + ';' + xLoco[u'location'][u'track'][u'userName']
        jTo = xLoco[u'destination'][u'userName'] + ';' + xLoco[u'destination'][u'track'][u'userName']
        jFD = 'None;None'
        jType = xLoco[u'carType'] + "-" + xLoco[u'carSubType']

        return [xLoco[u'name'], xLoco[u'model'], jType, 'O', jFrom, jTo, jFD]

    def parseCar(self, xCar):
        fdMissing = ' - no missing FDs'
        if not xCar[u'finalDestination']:
            jFinalDestination = 'None'
            jFinalTrack = 'None'
            fdMissing = ' with some FDs not defined'
        else:
            jFinalDestination = xCar[u'finalDestination'][u'userName']
            try:
                jFinalTrack = xCar[u'finalDestination'][u'track'][u'userName']
            except KeyError:
                jFinalTrack = 'Any'
                fdMissing = ' with some FD tracks not defined'
        jFrom = xCar[u'location'][u'userName'] + ';' + xCar[u'location'][u'track'][u'userName']
        jTo = xCar[u'destination'][u'userName'] + ';' + xCar[u'destination'][u'track'][u'userName']
        jFD = jFinalDestination + ';' + jFinalTrack
        jLoad = xCar[u'load']
        if xCar[u'caboose'] or xCar[u'passenger']:
            jLoad = 'O'

        return [xCar[u'name'], xCar[u'road'], xCar[u'number'], jLoad, jFrom, jTo, jFD]

    def findManifest(self):
        '''If more than 1 train is built, pick the newest one'''

        jNewestTime = ''
        jBuildCount = 0
        trainList = self.jTM.getTrainsByTimeList() # Refers to departure time, not built time
        for train in trainList:
            if train.isBuilt():
                jBuildCount += 1
                buildMessage = 'Script completed'
                jManifestanifest =  self.jProfilePath + 'operations\jsonManifests\\train-' + train.getName() + ".json"
                with open(jManifestanifest) as f:
                    manifest = json.load(f)
                if manifest[u'date'] > jNewestTime:
                    jNewestTime = manifest[u'date']
                    jNewestManifest = jManifestanifest
                    jTrainComment = train.getComment()
            if jBuildCount == 0:
                jNewestManifest = None
                jTrainComment = 'No trains are built'

        return jNewestManifest, jTrainComment

    def writeManifest(self, jManifest, jComment):
        '''The JMRI jason manifest is encoded in HTML Entity'''
        # csv writer does not encode utf-8

        jEncoding = 'utf-8'
        with codecsOpen(jManifest) as jsonManifest:
            manifest = json.load(jsonManifest)

        jCopyTo = jmri.util.FileUtil.getHomePath() + "AppData\Roaming\TrainPlayer\Reports\JMRI - Manifest.csv"
        with codecsOpen(jCopyTo, 'wb', encoding=jEncoding) as csvWorkFile:
            jEntity = HTMLParser() # https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
            csvManifest = 'HN,' + jEntity.unescape(manifest.get('railroad')) + '\n'
            csvManifest = csvManifest + 'HT,' + jEntity.unescape(manifest.get('userName')) + '\n'
            csvManifest = csvManifest + 'HD,' + jEntity.unescape(manifest.get('description')) + '\n'
            csvManifest = csvManifest + 'HC,' + jEntity.unescape(jComment) + '\n'
            csvManifest = csvManifest + 'HV,' + self.timeStamp() + '\n'
            csvManifest = csvManifest + u'WT,' + str(len(manifest['locations'])) + '\n'
            x = 1
            for location in manifest[u'locations']:
                csvManifest = csvManifest + u'WE,' + str(x) + ',' + jEntity.unescape(location[u'userName']) + '\n'
                for loco in location[u'engines'][u'add']:
                    newLine = self.parseLoco(loco)
                    csvManifest = csvManifest + u'PL,'
                    while (newLine):
                        csvManifest = csvManifest + jEntity.unescape(newLine[0]) + ','
                        newLine.pop(0)
                    csvManifest = csvManifest + '\n'
                for loco in location[u'engines'][u'remove']:
                    newLine = self.parseLoco(loco)
                    csvManifest = csvManifest + u'SL,'
                    while (newLine):
                        csvManifest = csvManifest + jEntity.unescape(newLine[0]) + ','
                        newLine.pop(0)
                    csvManifest = csvManifest + '\n'
                for car in location['cars']['add']:
                    newLine = self.parseCar(car)
                    csvManifest = csvManifest + u'PC,'
                    while (newLine):
                        csvManifest = csvManifest + jEntity.unescape(newLine[0]) + ','
                        newLine.pop(0)
                    csvManifest = csvManifest + '\n'
                for car in location['cars']['remove']:
                    newLine = self.parseCar(car)
                    csvManifest = csvManifest + u'SC,'
                    while (newLine):
                        csvManifest = csvManifest + jEntity.unescape(newLine[0]) + ','
                        newLine.pop(0)
                    csvManifest = csvManifest + '\n'
                x += 1
            csvWorkFile.write(csvManifest)

        return 'Manifest is built'

    def handle(self):
        jTimeNow = time.time()
        jNewestManifest, jTrainComment = self.findManifest()
        if (jNewestManifest):
            print(ManifestForTrainPlayer().writeManifest(jNewestManifest, jTrainComment))
        else:
            print('No manifest to build')
        print('Manifest export (sec): ' + ('%s' % (time.time() - jTimeNow))[:6])

        return False

CheckDestinationDirectory().start()
LocationsForTrainPlayer().start()
ManifestForTrainPlayer().start()
print(scriptName + ' ' + str(scriptRev))

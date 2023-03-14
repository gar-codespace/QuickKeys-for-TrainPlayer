## QuickKeys
QuickKeys is a suite of TrainPlayer scripts that map train commands to the keyboard. The scripts are written in TrainPlayers native scripting language, TrainPlayer Programming Language, or TPL. These TPL scripts are contained in standard txt files, and can be copied directly into Subroutines folder in the users TrainPlayer folder. The following are the components that make up QuickKeys.  
### QuickKeys  
This is the 'main' component that links the other components together and provides language and help support.  
### SpeedSwitching  
SpeedSwitching maps the keyboard to TrainPlayer train control commands. This is the component that 'drives' trains.  
Within SpeedSwitching is a component called PhakePhysics. This component extends the capabilities of SpeedSwitching by adding a set of controls not found in TrainPlayer. As its name implies, PhakePhysics adds mild physics simulations to the movement of trains. Additionally, keyboard keys are remapped to better simulate real train control functions such as throttle notch and automatic brake applications. This adds the same sort of challenge real engineers face to TrainPlayers layout environment.  
### DropKick  
This is another set of mappings that allows the operator to 'kick' and 'drop' rail cars in a manner very similar to real rail operations, and adds fun to basic switching operations. These functions are unique to this suite and are not found in TrainPlayer.  
### o2o
o2o, or ops to ops, is a set of scripts which allows JMRI, the Java Model Railroad Interface to be used as the operations engine for TrainPlayer. All of the features of JMRI Operations Pro are leveraged by these scripts, and are implemented through TrainPlayer's Advanced Ops interace. On the JMRI side, my Pattern Scripts plugin is used to facilitate the use of JMRI with TrainPlayer.  
### RandomRoads
The RandomRoads subroutine is a utility tha relabels rolling stock on a layout from TraimPlayers functional nomenclature into something more 'railroady'. This sunroutine is configured via an Ops Central note. Users have control over which rolling stock
gets relabeled and the road names the rolling stock gets relabeled to. This subroutine enhances the display of Advanced Ops features.  
### TurnTable  
This component extends TrainPlayers control of turntables and transfer tables. By using the keyboard, a turntables bridge can easily be aligned to any stall or approach track.  
### SaveTimer
This script starts when a user begins switching and ends when the switching event is completed. It originated as a companion script to John Allen's Time Saver switching puzzle, but is generalized to accompany other switching puzzles as well.  
### LinkedLayouts
TrainPlayer has a feature which allows multiple layouts to be linked together to form a bigger meta-layout. The LinkedLayouts script was written to work around some of the early issues of TrainPlayers linking scheme. These issues are being addressed by the programmers and it is expected that this script will fade into obsolesence.  
### Videos
[QuickKeys Setup](https://youtu.be/nV8g_2UXFsU)  
[QuickKeys How To](https://youtu.be/htDPEsgWwQI)  
[SpeedSwitching](https://youtu.be/5_l3F8FqsZ0)  
[PhakePhysics](https://youtu.be/qM0VkDgiU6Q)  
[DropKick](https://youtu.be/_VV3hHayh6s)  
[o2o](https://youtu.be/pX_H_gtGYQA)  
[o2o - schedules](https://youtu.be/v02FAXSr3ZE)  
[RandomRoads]  
[TurnTable](https://youtu.be/Xcqcyivq_04)  
[SaveTimer]  
[LinkedLayouts]  
### Web sites
[TrainPlayer](http://trainplayer.com/)  
[JMRI Operations Pro](https://www.jmri.org/help/en/package/jmri/jmrit/operations/Operations.shtml)  
[Operations Pattern Scripts for JMRI](https://github.com/gar-codespace/OperationsPatternScripts)  
### License
There is none. Use and abuse as you see fit.  
The name TrainPlayer is copyright Jim Dill and is used with permission.

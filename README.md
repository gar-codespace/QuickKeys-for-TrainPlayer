## QuickKeys
A suite of TrainPlayer scripts that map train commands to the keyboard. The scripts are written in TrainPlayers native scripting language, TrainPlayer Programming Language, or TPL. These TPL scripts are contained in standard txt files, and can be copied directly into Subroutins folder on the users TrainPlayer folder. The followings are the modules that make up QuickKeys.  
### QuickKeys  
This is the 'main' module that links the other modules together and provides language and help support.  
### SpeedSwitching  
A set of keyboard mappings to TrainPlayer train control commands. This is the module that 'drives' trains.  
Within SpeedSwitching is a module called PhakePhysics. This module extends the capabilities of SpeedSwitching by adding a set of controls not found in TrainPlayer. As its name implies, PhakePhysics adds mild physics simulations to the movement of trains. Additionally, keyboard keys are remapped to better simulate real train control functions such as throttle notch and automatic brake applications. This adds the same sort of challenge real engineers face while controlling trains to TrainPlayers layout environment.  
### DropKick  
This is another set of mappings that allows the operator to 'kick' and 'drop' rail cars in a manner very similar to real rail operations, and adds fun to basic switching operations. These functions are unique to this suite and are not found in TrainPlayer.  
### PhastPhunctions  
PhastPhunctions are a set of mappings that allow locomotives to be selected by pressing a function key. Thus, any one of ten locomotives on a layout can quickly be selected to run.  
### TurnTable  
This module extends TrainPlayers control of turntables and transfer tables. By using the keyboard, a turntables bridge can easily be aligned to any stall or approach track.  
### SaveTimer
This script starts when a user begins switching and ends when the switching event is completed. It is intended as a companion script to John Allen's Time Saver switching puzzle, but is generalized to accompany other switching puzzles as well.
### LinkedLayouts
TrainPlayer has a feature which allows multiple layouts to be linked together to form a bigger meta-layout. The LinkedLayouts script was written to work around some of the early deficiencies of TrainPlayers linking scheme. These issues are being addressed by the programmers and it is expected that this script will fade into obsolesence.
### O2O
O2O, or Ops to Ops, is a set of scripts which allows JMRI, the Java Model Railroad Interface to be used as the operations engine for TrainPlayer. All of the advanced features of JMRI Operations Pro are leveraged by these scripts. Additionally, one script sits on the JMRI side to facilitate the export of train build data. The scripts on the TrainPlayer side then integrate the JMRI data into TrainPlayers Advanced Ops interface. The level of integration, or dependency, on JMRI Ops Pro can be chosen by the user, and is easily toggled.
### Web sites
[TrainPlayer](http://trainplayer.com/)  
(JMRI Operations Pro)[https://www.jmri.org/help/en/package/jmri/jmrit/operations/Operations.shtml]


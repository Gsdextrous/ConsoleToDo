
## How 
### do you handle remembering all that loads of plans you are going to realize everyday?

 - Producing tons of paper notes, plastered all over the house?  
 - Making 100+ Google Sheets in order to properly organise your time?  
 - Getting bored with renaming and reformatting Excel cells just to confirm that you've washed the dishes? 

If so, let me familarize you with 
# GS-ToDo
### It's a simple and convenient console app that allows you making your ToDo list without any strugglings.  
 You can **add**, **edit**, **delete**, **revive**, **destruct** and gather together events in your ToDo list by just a single command.  
 Try it once and feel the difference.
 
 ## Command list
 Here are all the commands, supported in **v 1.3.7** of GS-ToDo.  
 ### **Attention!** Note that each command is containing a dot, which means **function application operator** in the GS-ToDo ideology.
 
Major command pattern:  
### object_ID.function  
If a function is applied to the whole ToDo list (i.e. to a non-determined object), then _**object_ID is considered to be an empty string**_.  
All non-empty ID's starts with '@'.

**.add** - adds new event in your ToDo list and setting main features like  
name,  
custom ID (if you skip this step, app will generate a random ID), detailed info,  
deadline,  
status (ordinary/urgent/done),  
required achievement points (if task completion means completing several subtasks) 

**.show** - shows common and detailed info about an event or all events  
**.done** - changes your event status to ‘Done’  
**.delete** - deletes your event, but you are still able to recover it  
**.update_info** - changes detailed info of the event  
**.update_status** - changes event status  
**.update_progress** - changes the number of achievement points.  
**.update_id** - changes event ID  
**.delete_all** - deletes all events  
**.revive_all** - recovers all deleted (not destructed) events.  
**.destruct_all** - permanently destroys all deleted events  
**.save** - save your actions (autosave is not supported yet)  
**.exit** - save and quit (don’t forcibly terminate the programme unless you want to lose the current state of ToDo list)


### Please don't be silent and write if you are reaching some bugs or have an idea how to improve all that mess

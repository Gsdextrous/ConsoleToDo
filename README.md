
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
_name_,  
_custom ID_ (if you skip this step, app will generate a random ID),  
_detailed info_ (to finish multiline input, press Ctrl+Enter to make '__________' or type it by yourself and then press Enter),  
_deadline_,  
_status_ (ordinary/urgent/done),  
_required achievement points_ (if task completion means completing several subtasks) 

```commandline
>> .add
name?
>> Somebody
custom ID (without '@') ?
>> once
add some info?
>> told_me
>> the world is gonna
>> roll me
>> I ain't the sharpest tool
>> in the shed
>> __________
achievement points?
>> 1
ordinary/urgent/done
>> 2
active till?
31.12.21
```


**.show** - shows common and detailed info about an event or all events 
```commandline
@once.show
common info:
Urgent task       | Somebody | time_left: 57d 07h     | 1 pts left | ID @once
details:
told me
the world is gonna
roll me
I ain't the sharpest tool
in the shed
```
```commandline
.show
Urgent task       | Somebody         | time left: 57d 07h     | 1   pts left | ID @once
Urgent task       | Research!        | time left: 26d 07h     | 10  pts left | ID @res
Ordinary task     | Homework         | time left: -2d 16h     | 3   pts left | ID @dz
Completed         | Las-Vegas        | time left: --/--       | 1   pts left | ID @joycasino
```
(In practice, the above text is a bit more colorized)

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

# ExeLib 1.0.0

A python module as an alt to default exec() fun , with new features :  )

<br>

For getting return and logging from exec and also limit cpu time and ram usage...

 Use: from Exelib import exec_

## Install !!

    pip install ExeLib

## How to return ?? 
    
      
      __reexec__ <whatever you want to return>

## How to log ??
     
     
     __logging__ <whatever you want to log>

## How to use auto return ??
    
    exec_("bla bla bla" , auto_return = "<something you want to return , when the program crashes>")

## How to access these ??
   
    rets , logs = exec_("bla bla bla")


## How to set cpu time ??
      
      exec_(cmd,cpu_t= <time in seconds>)

## How to limit ram usage  ??
    
    exec_(cmd,ram_u= <max-size>)
 

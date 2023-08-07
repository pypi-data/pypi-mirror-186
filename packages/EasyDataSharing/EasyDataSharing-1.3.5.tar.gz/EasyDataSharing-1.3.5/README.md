# EasyScriptsDataSharing

Share Data between Scripts.

## About

This package allows multiple scripts to communicate each other while running

## instructions

1. Install

```
pip install EasyDataSharing
```

2. Import

```
from EasyDataSharing import *

```

## Functions

1. CreateData

if New Data created leave the ScriptId blank and it will a new one

```

UpdateData(myScriptName,otherScriptName,dataName,Data,ScriptId)

```

2. GetData

```

getFrom(otherScriptId,dataName)

```

3. GetScriptId

```

IdFromAuthor(otherScriptName)

```

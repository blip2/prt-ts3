prt-ts3
==========

PRT TS3 Permission Setting API
Uses a Flask app to act as an intermediary between the PRT website and the TS3 server

Uses/includes python-ts3 and Flask (and dependancies) licenses for all libraries can be found in their respective folder.

API Reference
---------

PUT Request: http://prt.blip2.net:7215/player/
Data:
{"uid": "urYh87jvJBJMvOrFAll/Md9whDA=", "team": "emc", "rank": "grunt",}
Valid Response:
200 {"response": "success"}
Error Response:
XXX {"response": "Error message here"}

Valid Teams:
emc
apn

Valid Ranks:
reserve
grunt
nco
sl
hco
xo
co
sco

DELETE Request: http://prt.blip2.net:7215/player/
Data:
{"uid": "urYh87jvJBJMvOrFAll/Md9whDA=", }
Valid Response:
200 {"response": "success"}
Error Response:
XXX {"response": "Error message here"}


License
---------

Copyright 2016 Ben Hussey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

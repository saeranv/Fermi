%run src/openstudio_python.py "C:\ladybug\hb_office1\\OpenStudio\hb_office1.osm"
argv ['src/openstudio_python.py', 'C:\\ladybug\\hb_office1\\\\OpenStudio\\hb_office1.osm']
C:\Program Files\OpenStudio 1.12.0\CSharp\openstudio
using openstudio 1.12
hello

print(osm)
OpenStudio.Model

zones = osm.getThermalZones()

zones
Out[16]: <OpenStudio.ThermalZoneVector at 0x1696fba8>

zones.Count
Out[17]: 5

zones[0]
Out[18]: <OpenStudio.ThermalZone at 0x16968080>

zones[0].name
Out[19]: <bound method 'name'>

zones[0].name()
Out[20]: <OpenStudio.OptionalString at 0x1696fda0>

zones[0].name().ToString()
Out[21]: u'OpenStudio.OptionalString'

dir(zones[0].name())
Out[22]:
['Dispose',
 'Equals',
 'Finalize',
 'GetHashCode',
 'GetType',
 'MemberwiseClone',
 'Overloads',
 'ReferenceEquals',
 'ToString',
 '__call__',
 '__class__',
 '__delattr__',
 '__delitem__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__init__',
 '__iter__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__overloads__',
 '__reduce__',
 '__reduce_ex__',
 '__ref__',
 '__repr__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'get',
 'isNull',
 'is_initialized',
 'reset',
 'set',
 'swigCMemOwn']

zones[0].name().get()
Out[23]: u'zone_9'

for i in xrange(len(zones)):
    print(zones[i].name().get())

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-69c91a0a2440> in <module>()
----> 1 for i in xrange(len(zones)):
      2     print(zones[i].name().get())
      3

TypeError: object of type 'ThermalZoneVector' has no len()

for i in xrange(zones.Count):
    print(zones[i].name().get())

zone_9
zone_8
zone_6
zone_7
zone_5


%run -m src.openstudio_python $osmfile
argv ['C:\\saeran\\master\\git\\Fermi\\src\\openstudio_python.py', 'C:\\ladybug\\hb_office1\\OpenStudio\\hb_office1.osm']
C:\Program Files\OpenStudio 1.12.0\CSharp\openstudio
using openstudio 1.12
hello

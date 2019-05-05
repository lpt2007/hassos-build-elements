# IR KITCHEN HOOD with 5-SPEED-FAN and LIGHT

# HARDWARE
- ir kitchen hood with fan control + light
- broadlink rm mini 3 form this link: https://www.banggood.com/Broadlink-Black-Bean-Smart-Home-Wifi-Remote-IR-Controller-Universal-Appliances-Smart-Control-p-1049494.html?rmmds=search&cur_warehouse=CN

configuration.yaml
```
  customize: !include_dir_merge_named customize/
  
input_number: !include components/input_number.yaml
input_boolean: !include components/input_boolean.yaml

sun:
python_script:

automation: !include_dir_merge_list automation
switch: !include_dir_merge_list switch
group: !include_dir_merge_named group
```
# IR CODES
```
FAN:"JgBQAAABK5IVNhUQFRAVEBUQFRAVEBU2FRAVNRU1FRAVEBU2FTUVEBU1FRAVERUQFRAVEBUQFTUVEBU2FTUVNRU1FTUWNRUQFQAFbQABLEcWAA0FAAAAAAAAAAA="
LIGHT:"JgBIAAABLJETNxMTFBEUERQRFBEUERU1ExITOBI4ExITEhM3EzcTExI4ExITEhM3EzcTEhMTEjgTEhM3EzcTEhMSEzgSOBMSEwANBQ=="
UP:"JgBQAAABK5IUNxMSExITEhUQFBEUERQ2FBITNxQ2FBEUERQ3EzcTEhQ2FBEUNxMSExITEhMSFDYUERQ3ExITNxQ2FDYUNxMSEwAFbwABK0gUAA0FAAAAAAAAAAA="
DOWN:"JgBIAAABKpMUNhMTExITEhMSFBEUERQ2FBISOBM3FBEUERM3FDcTEhMSEzcUERQ2FBITEhMSEzcUNhMSEzgTEhM3FDYUNhMTEwANBQ=="

```

# TODO
```
- add switch
```


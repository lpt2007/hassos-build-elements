rf = { "FAN":"JgBQAAABK5IVNhUQFRAVEBUQFRAVEBU2FRAVNRU1FRAVEBU2FTUVEBU1FRAVERUQFRAVEBUQFTUVEBU2FTUVNRU1FTUWNRUQFQAFbQABLEcWAA0FAAAAAAAAAAA=",
       "LIGHT":"JgBIAAABLJETNxMTFBEUERQRFBEUERU1ExITOBI4ExITEhM3EzcTExI4ExITEhM3EzcTEhMTEjgTEhM3EzcTEhMSEzgSOBMSEwANBQ==",
       "UP":"JgBQAAABK5IUNxMSExITEhUQFBEUERQ2FBITNxQ2FBEUERQ3EzcTEhQ2FBEUNxMSExITEhMSFDYUERQ3ExITNxQ2FDYUNxMSEwAFbwABK0gUAA0FAAAAAAAAAAA=",
       "DOWN":"JgBIAAABKpMUNhMTExITEhMSFBEUERQ2FBISOBM3FBEUERM3FDcTEhMSEzcUERQ2FBITEhMSEzcUNhMSEzgTEhM3FDYUNhMTEwANBQ=="
     }

cmd = data.get('command')

if cmd is not None:
  cmd = int(cmd)
  if -5 <= cmd <= 7:
    if cmd == 0:
      loop = 1
      rfc = rf['FAN']
    elif cmd == 6:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['FAN'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      loop = 1
      rfc = rf['DOWN']
    elif cmd == 7:
      loop = 1
      rfc = rf['LIGHT']
    else:
      if cmd > 0:
        rfc = rf['DOWN']
      else:
        rfc = rf['UP']
      loop = abs(cmd)

    service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rfc)}
    for i in range(loop):
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)

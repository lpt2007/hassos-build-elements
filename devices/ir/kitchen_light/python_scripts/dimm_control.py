rf = { "ON":"JgBQAAABJZMSExE3EhMRExE4ETgRExE4ETgRExI3EjcSEhISEjcSEhISEjcSEhISEhISExETETgRNhMTETgROBE4ETgROBETEgAFJgABJUYSAA0FAAAAAAAAAAA=",
       "OFF":"JgBQAAABJpITERM2ExESEhM2EzYTERM2EzYTERM2EjcTERMSEjcSEhETERMROBI3EjcSEhI3EjcSNxI3EhISEhISEjcTERMREgAFJgABJUYSAA0FAAAAAAAAAAA=",
       "UP":"JgBQAAABKJMSEhI3EhISExE4ETgRExE4ETgRExE4ETgRExETEjcSEhISEjcSEhI3EhIUEBQ1FDUUNRQQFDUUEBQ1FDUUEBQREwAFJAABKEQUAA0FAAAAAAAAAAA=",
       "DOWN":"JgBQAAABJpIUEBQ1FBAUEBQ1FDUUEBQ1FDUUEBQ1EzYUERISEjcSEhISEjYTEhMREzYTERM2EzYTNhMREzYTNhMREzYTERMREwAFJQABJ0UUAA0FAAAAAAAAAAA=",
       "SUN":"JgBUAAABJZITEhI3EhISEhI3EjcSEhI3EjcSEhI3EjcSEhMREzYTERMREzYTNhM2ExETERM2EzYTNhMRExISEhI3EjcSEhISEgAFJgABJUYTAAWLFwANBQAAAAA=",
       "MOON":"JgBQAAABJJQRExE4ERMRExI3EjcSEhI3EjcSEhI3EjcSEhISEjcSEhISEhISExETERMRExETETgROBE4ETgROBE4ETgROBETEgAFJgABJEcSAA0FAAAAAAAAAAA="
     }

cmd = data.get('command')

if cmd is not None:
  cmd = int(cmd)
  if -10 <= cmd <= 12:
    if cmd == 0:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['MOON'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      loop = 1
      rfc = rf['OFF']
    elif cmd == 12:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['ON'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      loop = 1
      rfc = rf['MOON']
    elif cmd == 11:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['ON'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      loop = 1
      rfc = rf['SUN']
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

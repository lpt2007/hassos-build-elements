rf = { "C":"JgBQAAABJpIUEBQ1FBAUEBQ1FDUUERM1FDUUERQ1FDUUEBQQFDUUEBQ1FBAUEBQ1FDUUEBQQFDUUEBQ1FDUUEBQQFDUUNRQQFAAFJAABJ0UUAA0FAAAAAAAAAAA=",
       "W":"JgBQAAABJ5EUEBQ1FBAUEBQ1FDUUERM1FDUVEBQ1FDUUEBQQFDUUEBQ1FBAUEBQQFBAUEBQ1FDUUEBQ1FDUUNRQ1FDUUERMRFAAFJAABJ0QUAA0FAAAAAAAAAAA="
     }

cmd = data.get('command')

if cmd is not None:
  cmd = int(cmd)
  if -10 <= cmd <= 12:
    if cmd == 0:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
    elif cmd == 12:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['C'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
    elif cmd == 11:
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
      service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rf['W'])}
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)
    else:
      if cmd > 0:
        rfc = rf['C']
      else:
        rfc = rf['W']
      loop = abs(cmd)

    service_data = {'host':'192.168.2.1', 'packet':'{}'.format(rfc)}
    for i in range(loop):
      hass.services.call('broadlink', 'send', service_data, False)
      time.sleep(0.55)

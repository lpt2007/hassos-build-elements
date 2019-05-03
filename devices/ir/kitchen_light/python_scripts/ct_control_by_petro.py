cmd = data.get('command')

def call_service(hass, host, rfkey, count):
    rf = {
        "C":"JgBQAAABJpIUEBQ1FBAUEBQ1FDUUERM1FDUUERQ1FDUUEBQQFDUUEBQ1FBAUEBQ1FDUUEBQQFDUUEBQ1FDUUEBQQFDUUNRQQFAAFJAABJ0UUAA0FAAAAAAAAAAA=",
        "W":"JgBQAAABJ5EUEBQ1FBAUEBQ1FDUUERM1FDUVEBQ1FDUUEBQQFDUUEBQ1FBAUEBQQFBAUEBQ1FDUUEBQ1FDUUNRQ1FDUUERMRFAAFJAABJ0QUAA0FAAAAAAAAAAA="
        }
    for i in range(count):
        service_data = {'host':host, 'packet':'{}'.format(rf[rfkey])}
        hass.services.call('broadlink', 'send', service_data, False)
        time.sleep(0.55)
    
if cmd is not None:
    cmd = int(cmd)
    if -10 <= cmd <= 12:
        if cmd in [0, 10]:
            call_service(hass, '192.168.2.1', 'C', 10)
        elif cmd == 11:
            call_service(hass, '192.168.2.1', 'W', 10)
        else:
            rfkey = 'C' if cmd > 0 else 'W'
            count = abs(cmd)
            call_service(hass, '192.168.2.1', rfkey, count)

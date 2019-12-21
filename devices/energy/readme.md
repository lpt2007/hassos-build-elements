ENERGY CONSMPTION

MEASUREING POINTS:

- hallway_climate_tasmota
- childrensroom_electronic_tasmota
- bathroom_washer_and_dryer

NEEDED configuration.yaml SETTINGS:

input_number: !include_dir_merge_named components/input_number
mqtt: !include components/mqtt.yaml
notify: !include components/notify.yaml
matrix: !include_dir_merge_named components/matrix
utility_meter: !include_dir_merge_named components/utility_meter
input_datetime: !include components/input_datetime.yaml

switch: !include_dir_merge_list switch
script: !include_dir_merge_named scripts
sensor: !include_dir_merge_list sensor
binary_sensor: !include_dir_merge_list binary_sensor
#automation: !include automations.yaml
#script: !include scripts.yaml

FILE TREE:
hassos-build-elements/devices/energy/

hassos-build-elements/devices/energy/automation/
hassos-build-elements/devices/energy/automation/energy_costs_daily_report.yaml
hassos-build-elements/devices/energy/automation/energy_costs_tariffs.yaml

hassos-build-elements/devices/energy/binary_sensor/
hassos-build-elements/devices/energy/binary_sensor/dark_outside.yaml

hassos-build-elements/devices/energy/components/
hassos-build-elements/devices/energy/components/input_datetime.yaml
hassos-build-elements/devices/energy/components/input_number/
hassos-build-elements/devices/energy/components/input_number/energy_costs.yaml
hassos-build-elements/devices/energy/components/utility_meter/
hassos-build-elements/devices/energy/components/utility_meter/energy_costs.yaml

hassos-build-elements/devices/energy/lovelace/
hassos-build-elements/devices/energy/lovelace/energy_usage.yaml
hassos-build-elements/devices/energy/lovelace/energy_usage_children_electronics.yaml
hassos-build-elements/devices/energy/lovelace/energy_usage_climate.yaml
hassos-build-elements/devices/energy/lovelace/energy_usage_washer_and_dryer.yaml

hassos-build-elements/devices/energy/scripts/
hassos-build-elements/devices/energy/scripts/energy_costs_reset_cumulative_costs.yaml

hassos-build-elements/devices/energy/sensors/
hassos-build-elements/devices/energy/sensors/date.yaml
hassos-build-elements/devices/energy/sensors/sehlly_bathroom_washer_and_dryer.yaml
hassos-build-elements/devices/energy/sensors/tasmota_childrensroom_electronics.yaml
hassos-build-elements/devices/energy/sensors/tasmota_hallway_climate_mitsubishi.yaml
hassos-build-elements/devices/energy/sensors/template_bathroom_washer_and_dryer.yaml
hassos-build-elements/devices/energy/sensors/template_childrensroom_electronics.yaml
hassos-build-elements/devices/energy/sensors/template_hallway_climate.yaml
hassos-build-elements/devices/energy/sensors/template_total.yaml




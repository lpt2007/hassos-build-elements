IR KITCHE LIGHT - HASS CONTROL

configuration.yaml
```
  customize: !include_dir_merge_named customize/

sun:
python_script:

automation: !include_dir_merge_list automation
switch: !include_dir_merge_list switch
group: !include_dir_merge_named group
```

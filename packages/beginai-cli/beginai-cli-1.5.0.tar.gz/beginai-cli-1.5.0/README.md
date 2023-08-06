# cli

Begin AI CLI - PySDK Batch Processing Wrapper

Available commands:

## Process User Data

```
    beginai-cli process_user_data --app-id {app_id_uuid} --license-key {license_key} --csv-file-location {file_location} --column-representing-user-id {csv_colum_name} --column-representing-label {csv_column_representing_label} --column-representing-created-at {csv_column_representing_created_at} --file-separator {csv_file_separator}
```

## Process Object Data

```
    beginai-cli process_object_data --app-id {app_id_uuid} --license-key {license_key} --csv-file-location {file_location} --column-representing-object-id {csv_colum_name} --object-name {object_name_as_defined_on_schema} --column-representing-label {csv_column_representing_label} --column-representing-created-at {csv_column_representing_created_at} --file-separator {csv_file_separator}
```

## Process User Interactions With Object

```
    beginai-cli process_interactions --app-id {app_id_uuid} --license-key {license_key} --csv-file-location {file_location}  --column-representing-user-id {csv_colum_name} --column-representing-object-id {csv_colum_name} --object-name {object_name_as_defined_on_schema} --column-representing-action {csv_column_representing_action_as_defined_on_schema} --column-representing-created-at {csv_column_representing_created_at} --file-separator {csv_file_separator}
```

**Note: all the methods accept an optional parameter --host that can be used when testing locally**

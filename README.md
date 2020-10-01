# datacatalog-custom-model-manager

Python scripts to load user specified metadata models into Google Cloud Data Catalog, comprising
[Custom Entries](https://cloud.google.com/data-catalog/docs/how-to/custom-entries), Tag Templates,
and [Tags](https://cloud.google.com/data-catalog/docs/concepts/overview#tags).

- *COMMANDS* 

**Python + virtualenv**

```bash
python load_model_csv.py \
  --files-folder <CSV-FILES-PATH> \
  --project-id <YOUR-PROJECT-ID> \
  --location-id <YOUR-LOCATION-ID>
```

# datacatalog-custom-model-manager

A Python package intended to load user-specified metadata models into Google Cloud Data Catalog,
comprising [Custom Entries](https://cloud.google.com/data-catalog/docs/how-to/custom-entries), Tag
Templates, and [Tags](https://cloud.google.com/data-catalog/docs/concepts/overview#tags).

It is powered by [datacatalog-custom-entries-
manager](https://github.com/ricardolsmendes/datacatalog-custom-entries-manager), [datacatalog-
tag-template-processor](https://github.com/mesmacosta/datacatalog-tag-template-processor), and
[datacatalog-tag-manager](https://github.com/ricardolsmendes/datacatalog-tag-manager), leveraging
their features in the format of a single CLI.

> **WORK IN PROGRESS**: This repository is under active development and breaking changes are
> expected in the coming weeks!

- *COMMANDS* 

**Python + virtualenv**

```bash
python load_model_csv.py \
  --files-folder <CSV-FILES-PATH> \
  --project-id <YOUR-PROJECT-ID> \
  --location-id <YOUR-LOCATION-ID> \
  [--delete-existing-tag-templates]
```

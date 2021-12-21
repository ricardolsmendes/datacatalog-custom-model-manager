# datacatalog-custom-model-manager

A Python package intended to load user-specified metadata models into Google Cloud Data Catalog,
comprising [Custom Entries](https://cloud.google.com/data-catalog/docs/how-to/custom-entries), Tag
Templates, and [Tags](https://cloud.google.com/data-catalog/docs/concepts/overview#tags).

It is powered by [datacatalog-custom-entries-
manager](https://github.com/ricardolsmendes/datacatalog-custom-entries-manager), [datacatalog-
tag-template-processor](https://github.com/mesmacosta/datacatalog-tag-template-processor), and
[datacatalog-tag-manager](https://github.com/ricardolsmendes/datacatalog-tag-manager), leveraging
their features in the format of a single CLI.

[![license](https://img.shields.io/github/license/ricardolsmendes/datacatalog-custom-model-manager.svg)](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/blob/master/LICENSE)
[![pypi](https://img.shields.io/pypi/v/datacatalog-custom-model-manager.svg)](https://pypi.org/project/datacatalog-custom-model-manager)
[![issues](https://img.shields.io/github/issues/ricardolsmendes/datacatalog-custom-model-manager.svg)](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/issues)
[![continuous integration](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/actions/workflows/continuous-integration.yaml)
[![continuous delivery](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/actions/workflows/continuous-delivery.yaml/badge.svg)](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/actions/workflows/continuous-delivery.yaml)

---

## Load Custom Model

### From CSV files

- _SCHEMAS_

Loading custom models from CSV requires a folder (`--files-folder` argument in the below commands)
containing three files: `entries.csv`, `tag_templates.csv`, and `tags.csv`. Please refer to the
following external resources for further details on their layouts:

| FILE                | LAYOUT DOCUMENTATION                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `entries.csv`       | [datacatalog-custom-entries-manager README](https://github.com/ricardolsmendes/datacatalog-custom-entries-manager#211-to-a-csv-file)                                        |
| `tag_templates.csv` | [datacatalog-tag-template-processor README](https://github.com/mesmacosta/datacatalog-tag-template-processor#21-create-a-csv-file-representing-the-templates-to-be-created) |
| `tags.csv`          | [datacatalog-tag-manager README](https://github.com/ricardolsmendes/datacatalog-tag-manager#211-from-a-csv-file)                                                            |

- _SAMPLE INPUT_

1. [sample-input/egeria-business-glossary](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/tree/master/sample-input/egeria-business-glossary)
   for reference;
1. [Sample metadata for datacatalog-custom-model-manager](https://docs.google.com/spreadsheets/d/13MuxLjQGrD-A7R4p_3TGaVFCV3X0atWmyxIINQNF2R4)
   (Google Sheets) might help to create/export the mandatory CSV files.

- _COMMANDS_

**Python + virtualenv**

```sh
pip install datacatalog-custom-model-manager

datacatalog-custom-model load \
  --files-folder <CSV-FILES-PATH> \
  --project-id <YOUR-PROJECT-ID> --location-id <YOUR-LOCATION-ID> \
  [--delete-existing-tag-templates]
```

**Docker**

```sh
docker build --rm --tag datacatalog-custom-model-manager .

docker run --rm --tty \
  --volume <CREDENTIALS-FILE-FOLDER>:/credentials --volume <CSV-FILE-FOLDER>:/data \
  datacatalog-custom-model-manager load \
  --files-folder <CSV-FILES-PATH> \
  --project-id <YOUR-PROJECT-ID> --location-id <YOUR-LOCATION-ID> \
  [--delete-existing-tag-templates]
```

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/blob/master/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please
add a comment saying that you encountered the problem as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/datacatalog-custom-model-manager/blob/master/.github/CONTRIBUTING.md)
before making a pull request.

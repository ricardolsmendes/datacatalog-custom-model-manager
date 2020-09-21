"""
This application loads a user specified metadata model into Google Data Catalog, reading
information from CSV files.
"""
import argparse
import logging

import datacatalog_custom_entries_manager
import datacatalog_tag_manager
from datacatalog_tag_template_processor.datacatalog_tag_template_processor_cli import \
    tag_template_datasource_processor

"""
Main program entry point
========================================
"""
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Load user specified metadata model from CSV')

    parser.add_argument(
        '--files-folder', help='Path to the CSV files container folder', required=True)
    parser.add_argument('--project-id', help='Google Cloud Project ID', required=True)
    parser.add_argument('--location-id', help='Google Cloud Location ID', required=True)

    args = parser.parse_args()

    datacatalog_custom_entries_manager.CustomEntriesSynchronizer(
        args.project_id, args.location_id).sync_to_file(f'{args.files_folder}/entries.csv', '')

    tag_template_datasource_processor.TagTemplateDatasourceProcessor()\
        .create_tag_templates_from_csv(f'{args.files_folder}/tag_templates.csv')

    datacatalog_tag_manager.TagDatasourceProcessor().upsert_tags_from_csv(
        f'{args.files_folder}/tags.csv')

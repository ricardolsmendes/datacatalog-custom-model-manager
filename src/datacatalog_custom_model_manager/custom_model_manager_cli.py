import argparse
import logging
import sys

import datacatalog_custom_entries_manager
import datacatalog_tag_manager
from datacatalog_tag_template_processor.datacatalog_tag_template_processor_cli import \
    tag_template_datasource_processor


class CustomModelManagerCLI:

    @classmethod
    def run(cls, argv):
        cls.__setup_logging()

        args = cls._parse_args(argv)
        args.func(args)

    @classmethod
    def __setup_logging(cls):
        logging.basicConfig(level=logging.INFO)

    @classmethod
    def _parse_args(cls, argv):
        parser = argparse.ArgumentParser(description=__doc__,
                                         formatter_class=argparse.RawDescriptionHelpFormatter)

        subparsers = parser.add_subparsers()

        load_model_parser = subparsers.add_parser('load', help='Load Custom Model')
        load_model_parser.add_argument('--files-folder',
                                       help='Path to the CSV files container folder',
                                       required=True)
        load_model_parser.add_argument('--project-id',
                                       help='Google Cloud Project ID',
                                       required=True)
        load_model_parser.add_argument('--location-id',
                                       help='Google Cloud Location ID',
                                       required=True)
        load_model_parser.add_argument(
            '--delete-existing-tag-templates',
            action='store_true',
            help='Delete existing Tag Templates and recreate them with the provided metadata')

        load_model_parser.set_defaults(func=cls.__load_custom_model)

        return parser.parse_args(argv)

    @classmethod
    def __load_custom_model(cls, args):
        datacatalog_custom_entries_manager.CustomEntriesSynchronizer(
            args.project_id, args.location_id).sync_to_file(f'{args.files_folder}/entries.csv', '')

        tag_template_ds_proc = tag_template_datasource_processor.TagTemplateDatasourceProcessor()
        if args.delete_existing_tag_templates:
            tag_template_ds_proc.delete_tag_templates_from_csv(
                f'{args.files_folder}/tag_templates.csv')

        tag_template_ds_proc.create_tag_templates_from_csv(
            f'{args.files_folder}/tag_templates.csv')

        datacatalog_tag_manager.TagDatasourceProcessor().upsert_tags_from_csv(
            f'{args.files_folder}/tags.csv')


def main():
    argv = sys.argv
    CustomModelManagerCLI.run(argv[1:] if len(argv) > 0 else argv)

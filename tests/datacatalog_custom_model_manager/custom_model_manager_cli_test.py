import unittest
from unittest import mock

import datacatalog_custom_model_manager
from datacatalog_custom_model_manager import custom_model_manager_cli


class CustomModelManagerCLITest(unittest.TestCase):
    __CLI_MODULE = 'datacatalog_custom_model_manager.custom_model_manager_cli'
    __CLI_CLASS = f'{__CLI_MODULE}.CustomModelManagerCLI'

    @mock.patch(f'{__CLI_CLASS}._CustomModelManagerCLI__load_custom_model')
    @mock.patch(f'{__CLI_CLASS}._parse_args')
    def test_run_load_model_should_parse_args(self, mock_parse_args, mock_load_custom_model):
        mock_parse_args.return_value.func = mock_load_custom_model
        custom_model_manager_cli.CustomModelManagerCLI.run([])
        mock_parse_args.assert_called_once()

    @mock.patch(f'{__CLI_CLASS}._CustomModelManagerCLI__load_custom_model')
    @mock.patch(f'{__CLI_CLASS}._parse_args')
    def test_run_load_model_should_call_load_custom_model(self, mock_parse_args,
                                                          mock_load_custom_model):

        mock_parse_args.return_value.func = mock_load_custom_model
        custom_model_manager_cli.CustomModelManagerCLI.run([])
        mock_load_custom_model.assert_called_once_with(mock_parse_args.return_value)

    def test_parse_args_invalid_subcommand_should_raise_system_exit(self):
        self.assertRaises(SystemExit, custom_model_manager_cli.CustomModelManagerCLI._parse_args,
                          ['create'])

    def test_parse_args_load_model_missing_mandatory_args_should_raise_system_exit(self):
        self.assertRaises(SystemExit, custom_model_manager_cli.CustomModelManagerCLI._parse_args,
                          ['load'])

    def test_parse_args_load_model_should_parse_mandatory_args(self):
        args = custom_model_manager_cli.CustomModelManagerCLI._parse_args([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location'
        ])
        self.assertEqual('test-folder', args.files_folder)
        self.assertEqual('test-project', args.project_id)
        self.assertEqual('test-location', args.location_id)

    def test_parse_args_load_model_should_parse_optional_args(self):
        args = custom_model_manager_cli.CustomModelManagerCLI._parse_args([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location', '--delete-existing-tag-templates'
        ])
        self.assertTrue(args.delete_existing_tag_templates)

    @mock.patch(f'{__CLI_CLASS}._CustomModelManagerCLI__load_custom_model')
    def test_parse_args_load_model_should_set_default_function(self, mock_load_custom_model):
        args = custom_model_manager_cli.CustomModelManagerCLI._parse_args([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location'
        ])
        self.assertEqual(mock_load_custom_model, args.func)

    @mock.patch(f'{__CLI_MODULE}.datacatalog_tag_manager.TagDatasourceProcessor',
                lambda *args: mock.MagicMock())
    @mock.patch(f'{__CLI_MODULE}.tag_template_datasource_processor.TagTemplateDatasourceProcessor',
                lambda *args: mock.MagicMock())
    @mock.patch(f'{__CLI_MODULE}.datacatalog_custom_entries_manager.CustomEntriesSynchronizer')
    def test_load_custom_model_should_sync_entries_from_csv(self,
                                                            mock_custom_entries_synchronizer):

        custom_model_manager_cli.CustomModelManagerCLI.run([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location'
        ])
        mock_custom_entries_synchronizer.assert_called_with('test-project', 'test-location')
        mock_custom_entries_synchronizer.return_value.sync_to_file.assert_called_with(
            'test-folder/entries.csv', '')

    @mock.patch(f'{__CLI_MODULE}.datacatalog_tag_manager.TagDatasourceProcessor',
                lambda *args: mock.MagicMock())
    @mock.patch(f'{__CLI_MODULE}.tag_template_datasource_processor.TagTemplateDatasourceProcessor')
    @mock.patch(f'{__CLI_MODULE}.datacatalog_custom_entries_manager.CustomEntriesSynchronizer',
                lambda *args: mock.MagicMock())
    def test_load_custom_model_should_create_tag_templates_from_csv(
            self, mock_tag_template_datasource_processor):

        custom_model_manager_cli.CustomModelManagerCLI.run([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location'
        ])
        mock_tag_template_datasource_processor.assert_called_once()
        mock_tag_template_datasource_processor.return_value.create_tag_templates_from_csv\
            .assert_called_with('test-folder/tag_templates.csv')

    @mock.patch(f'{__CLI_MODULE}.datacatalog_tag_manager.TagDatasourceProcessor',
                lambda *args: mock.MagicMock())
    @mock.patch(f'{__CLI_MODULE}.tag_template_datasource_processor.TagTemplateDatasourceProcessor')
    @mock.patch(f'{__CLI_MODULE}.datacatalog_custom_entries_manager.CustomEntriesSynchronizer',
                lambda *args: mock.MagicMock())
    def test_load_custom_model_should_optionally_delete_existing_tag_templates(
            self, mock_tag_template_datasource_processor):

        custom_model_manager_cli.CustomModelManagerCLI.run([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location', '--delete-existing-tag-templates'
        ])
        mock_tag_template_datasource_processor.assert_called_once()
        mock_tag_template_datasource_processor.return_value.delete_tag_templates_from_csv\
            .assert_called_with('test-folder/tag_templates.csv')

    @mock.patch(f'{__CLI_MODULE}.datacatalog_tag_manager.TagDatasourceProcessor')
    @mock.patch(f'{__CLI_MODULE}.tag_template_datasource_processor.TagTemplateDatasourceProcessor',
                lambda *args: mock.MagicMock())
    @mock.patch(f'{__CLI_MODULE}.datacatalog_custom_entries_manager.CustomEntriesSynchronizer',
                lambda *args: mock.MagicMock())
    def test_load_custom_model_should_upsert_tags_from_csv(self, mock_tag_datasource_processor):
        custom_model_manager_cli.CustomModelManagerCLI.run([
            'load', '--files-folder', 'test-folder', '--project-id', 'test-project',
            '--location-id', 'test-location'
        ])
        mock_tag_datasource_processor.assert_called_once()
        mock_tag_datasource_processor.return_value.upsert_tags_from_csv\
            .assert_called_with('test-folder/tags.csv')

    @mock.patch(f'{__CLI_CLASS}.run')
    def test_main_should_call_cli_run(self, mock_run):
        datacatalog_custom_model_manager.main()
        mock_run.assert_called_once()

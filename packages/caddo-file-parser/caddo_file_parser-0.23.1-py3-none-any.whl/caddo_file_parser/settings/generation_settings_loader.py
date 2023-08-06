from caddo_file_parser.settings.generation_settings import GenerationSettings


class GenerationSettingsLoader:
    def load_settings_object(self, settings_file):
        settings_data: GenerationSettings = GenerationSettings()
        settings_data.data_input_path = settings_file["data"]["input"]["path"]
        settings_data.data_input_separator = settings_file["data"]['input']['separator']
        settings_data.data_extraction_function_path = settings_file["data"]['extraction']['function']['path']
        settings_data.data_splitting_folding_number = settings_file["data"]['splitting']['folding']['number']
        settings_data.data_splitting_runs = settings_file["data"]['splitting']['runs']
        settings_data.data_output_file_name = settings_file["data"]['output']['file']['name']
        settings_data.data_splitting_folding_method = settings_file["data"]['splitting']['folding']['method']
        settings_data.data_splitting_folding_seeds_from_list = settings_file["data"]['splitting']['folding']['seeds']['from_list']
        settings_data.data_output_file_separator = settings_file["data"]['output']['file']['separator']
        return settings_data

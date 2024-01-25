import argparse
from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder
from apollo11_simulator.config import config


# logica argparse
if __name__ == '__main__':
    event_params = config["event_params"]

    parser = argparse.ArgumentParser(description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation', choices=['generate-events', 'generate-report'],
                        help='Tipo de operacion a realizar: generar eventos, generar reportes')

    args = parser.parse_args()

    match args.operation:
            case 'generate-events':
                print('Running in "generate events" mode')
                event_manager = EventManager(input_data_file = event_params["input_data_file"],
                                             target_path= event_params["target_path"],
                                             frequency_seconds= event_params["frequency_seconds"],
                                             range_of_files= (event_params["range_of_files"]["min"], event_params["range_of_files"]["max"]))
                event_manager()
            case 'generate-report':
                print('Running in "generate report" mode')
                reporter = ReportBuilder.read_events('devices')
                reporter()

import argparse

from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder
from apollo11_simulator.config.logger import Logger

logger = Logger().get_logger(module_name='main', log_location='logs', logger_level=logging.INFO)

# logica argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation', choices=['generate-events', 'generate-report'],
                        help='Tipo de operacion a realizar: generar eventos, generar reportes')

    args = parser.parse_args()

    match args.operation:
            case 'generate-events':
                logger.info('Running in "generate events" mode')
                event_manager = EventManager(input_data_file = 'input_data/simulation.json', target_path='devices', frequency_seconds=3, range_of_files=(7, 10))
                event_manager()
            case 'generate-report':
                logger.info('Running in "generate report" mode')
                reporter = ReportBuilder.read_events('devices')
                reporter()

import argparse

# from apollo11_simulator.models.event_processing.event_manager import EventManager
# from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

# logica argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation', choices=['generate-data', 'generate-reports'],
                        help='Tipo de operacion a realizar: generar eventos, generar reportes')

    args = parser.parse_args()

    if args.operation == 'generate-data':
        print("running generate data mode...")
        # si es en modo generador
        # event_manager = EventManager(target_path='devices', frequency_seconds=3, range_of_files=(7, 10))
        # event_manager()
    elif args.operation == 'generate-reports':
        print("running generate reporter mode...")
        # si es en modo reporter
        # reporter method
        # reporter = ReportBuilder.from_path('')
        # reporter.show_reporter()

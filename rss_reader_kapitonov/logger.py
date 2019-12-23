import logging

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - '
                    '%(message)s')
logging.info('Logs go here!')
logging.error('Something went wrong with logs :(')
logging.debug('Logs debug')
log = logging.getLogger()

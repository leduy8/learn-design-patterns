from logger import Logger

logger = Logger()
logger.add({
    'name': 'log 0001',
    'content': 'review number 1',
    'priority': 1
})

logger2 = Logger()
logger2.add({
    'name': 'log 0002',
    'content': 'review number 2',
    'priority': 4
})

logger3 = Logger()
logger3.display_all_logs()
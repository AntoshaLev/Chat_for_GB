"""
Журналирование (логгирование) с использованием модуля logging
Вынесение настройки логгирования в отдельный модуль
"""

import logging
import log_config_7

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
LOG = logging.getLogger('app.main')

def main():
    ''' Тестовая главная функция
    '''
    LOG.debug('Старт приложения')

if __name__ == '__main__':
    main()
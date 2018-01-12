"""Messages stuff"""

from flaskbox import constants

base_msg = '\n\nAll available commands:\n' \
           'flaskbox --init   \tInit the flaskbox.yml file' \
           '\nflaskbox --start    \tRun your mock Server\n'

file_exists_message = constants.OK_GREEN + 'flaskbox.yml' \
                      + constants.ENDC + ' already exists'

not_exists_message = 'You need to create the ' + constants.OK_GREEN + \
                     'flaskbox.yml' + constants.ENDC + ' file' + base_msg

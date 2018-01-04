"""Messages stuff"""

from flaskbox.colors import ccolors

base_msg = '\n\nAll available commands:\n' \
           'flaskbox --init   \tInit the flaskbox.yml file' \
           '\nflaskbox --start    \tRun your mock Server\n'

file_exists_message = ccolors.OK_GREEN.value + 'flaskbox.yml' \
                      + ccolors.ENDC.value + ' already exists'

not_exists_message = 'You need to create the ' + ccolors.OK_GREEN.value + \
                     'flaskbox.yml' + ccolors.ENDC.value + ' file' + base_msg

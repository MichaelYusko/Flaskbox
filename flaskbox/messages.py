"""Messages stuff"""

from flaskbox.colors import ccolors

base_msg = '\n\nAll available commands:\n\t\t' \
           'flaskbox --init   Init the flaskbox.yml file' \
           '\n\t\tflaskbox --start    Run your mock Server\n'

file_exists_message = ccolors.OK_GREEN.value + 'flaskbox.yml' \
                      + ccolors.ENDC.value + ' already exists'

not_exists_message = 'You need create ' + ccolors.OK_GREEN.value + \
                     'flaskbox.yml' + ccolors.ENDC.value + ' file' + base_msg

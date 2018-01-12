###################
# COLOR CONSTANTS
###################
HEADER = '\033[95m'
OK_BLUE = '\033[94m'
OK_GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


###########################
# ERROR MESSAGES CONSTANTS
###########################
BASE_ERROR_MSG = '\n\nAll available commands:\n' \
           'flaskbox --init   \tInit the flaskbox.yml file' \
           '\nflaskbox --start    \tRun your mock Server\n'

FILE_EXISTS_MESSAGE = OK_GREEN + 'flaskbox.yml' \
                      + ENDC + ' already exists'

NOT_EXISTS_MESSAGE = 'You need to create the ' + OK_GREEN + \
                     'flaskbox.yml' + ENDC + ' file' + BASE_ERROR_MSG

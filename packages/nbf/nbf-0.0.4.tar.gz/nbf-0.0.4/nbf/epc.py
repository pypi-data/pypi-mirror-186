'''basic dict-based config with optional encrypted string for sensitive data'''
import os
import time
import json
import logging
import subprocess
from json.decoder import JSONDecodeError
from getpass import getpass
from google.colab import drive


def get_logger(logger_name: str, logger_level: int = logging.DEBUG):
  '''named loggers for notebooks'''
  glogger = logging.getLogger(logger_name)
  glogger.setLevel(logger_level)
  glogger.propagate = False  # no double messages
  if len(glogger.handlers) == 0:
    glogger.addHandler(logging.StreamHandler())
    glogger.handlers[0].setFormatter(
        logging.Formatter('%(asctime)s %(name)s %(levelname)-8s %(message)s',
                          '%Y-%m-%d %H:%M:%S'))
  return glogger


logger = get_logger('epc')

# LISTS
# simple dict to store config, don't clobber if it exists
if 'c' not in globals():
  c = {}

# redact these fields in intentional output
hidden_fields = ['token', 'passwd']  # , 'user']

# services for setup/edit functions to consume
api_fields = {
    'ftp': {
        'user': '',
        'host': '',
        'passwd': '',
        'protocol': 'ftp',
        'port': 21,
        'action': '-o'
    },
    'other': {
        'token': ''
    },
    'github': {
        'user': '',
        'repo': '',
        'token': '',
        'filepath': ''
    },
    'user_and_token': {
        'user': '',
        'token': ''
    },
    'quit': {}
}

# bare-minimum API templates, uses encrypted dictionaries to generate commands
api_templates = {
    'ftp':
    lambda d:
    (f"curl --user {d['user']}:{d['passwd']} {d['action']}"
     f"{d['local_path']} {d['protocol']}://{d['host']}:{d['port']}/{d['remote_path']}"
     ),
    'other':
    lambda d: f"echo {d['token']}",  # you probably want get_token()
    'github':
    lambda d:
    f"git clone --progress https://{d['user']}:{d['token']}@github.com/{d['user']}/{d['repo']}.git",
    'github_file':
    lambda d: [
        'curl', '-O', '-H', 'Authorization: token ' + d[
            'token'], '-H', 'Accept: application/vnd.github.v3.raw',
        f"https://api.github.com/repos/{d['user']}/{d['repo']}/contents/{d['filepath']}",
        '--http1.1'
    ],
    'huggingface':
    lambda d: [
        'curl', 'https://api-inference.huggingface.co/models/' + d[
            'model'], '-X', 'POST', '-d', '{"inputs": ' + d['inputs'] + '}',
        '-H', 'Authorization: Bearer ' + d['token']
    ],
    'pypi_publish':
    lambda d:
    f"twine upload -u {d['user']} -p {d['token']} {d['active_project']}/dist/*"
}

# default paths for local resources; see Pathfinding section for details
path_templates = {
    'projects_dir':
    lambda d: f"{d.get('projects_dir','/content/')}",
    'active_project':
    lambda d: f"{d.get('active_project','app')}",
    'project_path':
    lambda d:
    f"{d.get('projects_dir','/content/')}{d.get('active_project','app')}/",
    'nb_dir':
    lambda d:
    f"{d.get('projects_dir','/content/')}{d.get('active_project','app')}/notebooks/",
}

# storing the passphrase here is less annoying but less secure
__e = {}

# MAIN


def get_epcw(label=''):
  '''the most basic pass input "system", set get_epcw=your_preference()'''
  if label != '':
    label = ' for ' + label
  __e['epw'] = __e['epw'] if 'epw' in __e else getpass(
      'Save passphrase as variable, leave blank to enter each time: ')
  return __e.get('epw') or getpass('Encrypt/decrypt passphrase' + label + ': ')


def exclamation(args: list):
  '''takes str or list, approximation of `!command` syntax for .py exports'''
  if isinstance(args, str):
    args = args.split()  # split() string for Popen args
  # print(' '.join(args)) # dev only, shows tokens!
  with subprocess.Popen(args, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT) as popen:
    for line in popen.stdout:
      print(line.decode(), end='')


def encode(decoded: dict, label: str = '') -> str:
  '''convert dict to JSON and AES encode with a passphrase'''
  json_string = json.dumps(decoded)
  # logger.debug('encoding: '+json_string) # dev only, shows tokens!
  return os.popen((
      f"echo '{json_string}' |gzip -c| openssl enc -e -aes-256-cbc -base64 -A "
      f"-pass pass:{get_epcw(label)} -pbkdf2")).read()


def decode(encrypted_string: str, label: str = '') -> dict:
  '''decodes an AES passphrase-encrypted JSON string into a dict'''
  decoded = os.popen(
      (f'echo "{encrypted_string}" | openssl enc -d -aes-256-cbc -base64 -A '
       f'-pass pass:{get_epcw(label)} -pbkdf2|gunzip -c')).read()
  # logger.debug('\ndecoded into: '+str(decoded)) # dev only, shows tokens!
  try:
    return json.loads(decoded)
  except JSONDecodeError:
    print('Bad passphrase or URI. Try again.')
    if 'epw' not in __e:
      decode(encrypted_string, label)  # no endless loop with bad epw
  return None


def get_token(key_name: str) -> str:
  '''primitve token fetch'''
  ret = decode(c['epc'])[key_name]
  # logger.debug('token return: '+str(ret)) # dev only, shows tokens!
  if ret.get('token') is not None:
    return ret['token']
  return None


def redact_output(text: str, fields: dict) -> str:
  '''replace output from hidden_fields list with <REDACTED>'''
  if isinstance(text, list):
    text = ' '.join(text)  # out as str if list needed for cURL
  for field in hidden_fields:  # redact hidden fields
    if fields.get(field):
      text = text.replace(fields[field], '<REDACTED>')
  return text


def cmd_from_template(template: str,
                      conf_args: dict,
                      print_cmd=False,
                      run_cmd=False) -> str:
  '''uses `api_templates[template](conf)` to get an executable command
  using stored conf: `conf=decode(c[epc])[key_name]`
  '''
  # if arg missing catch for more helpful error message
  try:
    cmd = api_templates[template](conf_args)  # get cmd from template
    out = redact_output(cmd, conf_args)  # redact hidden_fields
    if print_cmd:
      print(out)
    if run_cmd:
      exclamation(cmd)  # run it!
    return out
  except KeyError as error:
    logger.error('missing argument: %s for %s', error, template)
  return False


def make_request(key_name: str,
                 template: str = '',
                 additional_args: dict = None) -> str:
  '''wrapper around cmd_from_template to catch and add missing data;
  recovery from missing key_name via `update_keyring()`'''
  try:  # if key_name doesn't exist catch and ask to create
    args = decode(c['epc'])[key_name]  # get decoded dict for key_name
    # default to template with same name as service chosen when created:
    if template == '':
      template = args['service']
    if additional_args is not None:
      args.update(additional_args)  # update with addititonal args
    return cmd_from_template(template, args, True, True)  # get, print, run
  except KeyError as error:
    yn = input('resource key ' + str(error) +
               ' not in encrypted config, create? y/N: ')
    if yn == 'y':
      update_keyring(c['epc'])  # add it
      return make_request(key_name, template, additional_args)
    return False


def path_free(resource: str, config: dict = None) -> bool:
  '''basic isdir/isfile checking, will use global c if config not passed, also
  useful with `do_setup` if encrypted key_name is a path relative to `projects_dir`'''
  if config is None:
    config = c  # use global
  isdir = os.path.isdir(config['projects_dir'] + resource)
  isfile = os.path.isfile(config['projects_dir'] + resource)
  if isdir or isfile:
    logger.warning('Resource exists: ' + config['projects_dir'] + resource)
    return False
  return True


def do_setup(config: dict) -> dict:
  '''convenience method: sets up config, optionally mounts google drive, runs
  any commands in `setup_commands`, and fetches any requests in `resources`
  using encrypted string from `keyring` uri if set.'''
  config = config_dict(config)
  if 'keyring' in config:
    config['epc'] = os.popen('wget -qO- ' + config['keyring']).read().strip()
  if 'setup_commands' not in config:
    config['setup_commands'] = []
  if config['use_google_drive'] and not os.path.isdir('/content/drive/'):
    drive.mount('/content/drive/')
  for cmd in config['setup_commands']:
    print(cmd)
    os.system(cmd)
  if 'resources' in config:
    config['setup_commands'].extend([
        make_request(k, '', d) for k, d in config['resources'].items()
        if path_free(k, config)
    ])
  return config


# PATHS


def path_logic(xconf: dict) -> dict:
  '''sets up paths in config; system environment vars > xconf > defaults
  `active_project` precidence: `xconf` > first `xconf['resources']` > `path_templates`'''
  if 'setup_commands' not in xconf:
    xconf['setup_commands'] = []
  # attempt to get active_project from resources
  if 'resources' in xconf and 'active_project' not in xconf:
    xconf['active_project'] = next(iter(xconf['resources']))
  # environment vars > `path_templates` defaults
  for env_var, lfunc in path_templates.items():
    xconf[env_var] = lfunc(xconf)  # use path_templates
    try:
      val = os.environ[env_var.upper()]  # bash exports are UPPERCASE
      xconf[env_var] = val
      # don't use drive if system env is set up
      xconf['use_google_drive'] = False
    except KeyError:
      pass
  # if use_google_drive==True setup needs to symlink active_project to /content
  if 'use_google_drive' in xconf and xconf['use_google_drive']:
    xconf['setup_commands'].append(
        (f"ln -s /content/drive/MyDrive/Projects/{xconf['active_project']}/ "
         f"{xconf['project_path'].rstrip('/')}"))
  return xconf


# CONFIG


def config_dict(cxtern: dict) -> dict:
  '''local variables via optional Colab form into config'''
  logger.info('epc.config_dict(c): may be overridden by `c[setting_name]`')
  # @title Default Settings { run: "auto", vertical-output: true, form-width: "45%" }
  # @param ["logging.DEBUG", "logging.INFO", "logging.WARN"] {type:"raw"}
  log_level = logging.DEBUG
  # @param ['America/Anchorage','America/Denver'] {allow-input: true}
  timezone = 'America/Anchorage'
  use_google_drive = False  # @param {type:"boolean"}
  os.environ['TZ'] = timezone
  time.tzset()
  logger.setLevel(log_level)
  cxtern = {**dict(locals()), **c, **cxtern}  # cx > global c > defaults here
  cxtern = path_logic(cxtern)
  del cxtern['cxtern']
  # del cx['c']
  for i, k in cxtern.items():
    if i == 'log_level':
      k = logging.getLevelName(k)
    logger.info('%s: %s', i, k)
  return cxtern


# UTILS


def get_letter_options(options: dict) -> str:
  '''turns a list, of, options into a [l]ist, [o]f, [o]ptions'''
  return ', '.join(['[' + o[0:1] + ']' + o[1:] for o in options])


def get_input_prompt(key_name: str, name: str, field: str, is_masked: bool,
                     default) -> str:
  '''text prompt for `input()` based on context'''
  if name == 'other':
    name = key_name  # 'other' is not useful, use key_name
  ret = name + ' ' + field  # e.g., github user
  if is_masked is True:
    ret += ' (hidden)'  # e.g. github token (hidden)
    # if default is not None:
    default = str(len(default)) + ' chars'  # e.g. (hidden) [20 chars]
  # if default is not None:
  ret += f' [{default}]'  # show default if not hidden
  return ret + ': '


def get_user_config_input(name: str, decoded: dict) -> dict:
  '''uses global api_fields[name] to loop over fields and get input() for vals'''
  fields = api_fields[name]
  logger.debug(str(fields))
  key_name = input('memorable key_name (e.g., huggingface): ')
  if decoded.get(key_name) is not None:
    print(key_name, 'key exists')
  else:
    decoded[key_name] = fields
  to_encode = [
      (getpass(get_input_prompt(key_name, name, f, True, decoded[key_name][f]))
       or decoded[key_name][f]) if f in hidden_fields else
      (input(get_input_prompt(key_name, name, f, False, decoded[key_name][f]))
       or decoded[key_name][f]) for f in fields
  ]
  to_encode = dict(zip(fields, to_encode))
  to_encode['service'] = name
  decoded[key_name] = to_encode
  c['epc'] = encode(decoded)
  return decoded


def update_keyring(epc=None) -> dict:
  '''work with epc; accepts None, dict, or an encrypted string
  :returns decrypted dict'''
  deltxt = ''
  if epc is not None:
    if isinstance(epc, dict):
      decoded = epc
    else:
      decoded = decode(epc)
    logger.info(
        '--> Entering a key_name that exists will edit, selecting an option not listed will exit.'
    )
    print('Existing keys: ' + ', '.join(decoded.keys()))
    deltxt = ', [d]elete'
  else:
    decoded = {}
    print(('\n--> Create a service or simple {key_name:auth_token} entry. '
           'Encrypt/decrypt pass should be unique to this system.'))

  start_service = input(get_letter_options(api_fields) + deltxt + ': ')

  if start_service == 'o':
    decoded = get_user_config_input('other', decoded)
  elif start_service == 'g':
    print('\n--> Leave filepath blank to clone repo.')
    decoded = get_user_config_input('github', decoded)
  elif start_service == 'f':
    print('\n--> Protocol: ftp or ftps (ports 21 & 22)')
    decoded = get_user_config_input('ftp', decoded)
  elif start_service == 'u':
    print('\n--> AUTOMATE THIS')
    decoded = get_user_config_input('user_and_token', decoded)
  elif start_service == 'd':
    delete_key = input('\n--> Enter the key_name you wish to delete: ')
    try:
      del decoded[delete_key]
      encrypted_string = c['epc'] = encode(decoded)
      print('Deleted "', delete_key, '", encrypted_string is now:',
            encrypted_string)
    except KeyError:
      print('Could not find key', delete_key, 'please try again.')
      update_keyring(decoded)
  else:
    print('Quit or unknown service, confirm with "n" to exit.')

  add_another = input('Add/edit another? y/n: ')
  if add_another == 'y':
    update_keyring(decoded)
  return c['epc']


c['epc'] = 'U2FsdGVkX1+q8onitIzydG8ZC+SdDrKgTQQl1L91LHTkNXknnga+XIEkZk8KRPG4gMpief6NNazpIu2RK3IAYKeo3B4UCQsbQLm78nktkSxt/ZIYpnneoDvD/J3vYoCDLDExrEJ8AIVAdS6n9HBKHl/4ouEA78XQc+vh5qb1nkvneiBX3LYK01KQh0SMwJQqd/o3IU9G2o6cyEur0Ys6GT6P5qX8Osg11wlJkPsPPT6wlb2OI/HZA+oouuT2/RIoHJr0BdgxOZ+3dbjOaXj5GVC2NImuqRZFQuR0CyV5tQriNioxt6Lp3gqoRxsfWLCWNOpH2EgErEdeu8qmWyrp3iRa0MaxQ8MBmDO86ozE8a+3BlNit1yx1W0FHJVOBsTP8L6qD14rMmuqHuUgvCtLs2KGss6wu6hrdiqFeohqQ2KdE39ahW+xpBW5osO3d5ZXbGCQjmH3czneZ8vnGZDXD8JKEOcZIy31FmVGNkp0LwghGDmhjNmYLwnxTy5Zgbjh/P8+PxHaKLJzwv+r7a4YCunVOb2503kZiWuikb2XpKSTPTIgX38g7l28E+sgIzrzMZivf7+gTxJv3LViG/K0eL6x+NAuYosT9xRfDPLXIJDeIEFTD7/1uWqO5heicQo/NoOHl8WcxMqk1RSl/kzpe3ldyb2CCSroGQSbrJAAOb7gJS2/rmyrwE4UFo3ojfsy'

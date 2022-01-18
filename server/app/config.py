import os

# import validators.volgactf

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.
    'DEBUG': os.getenv('DEBUG') == '1',

    'TEAMS': {
        f'Team #{i}': f'10.10.{i}.1'
        for i in [1,2,3,4,5,6]
    },
    # 'FLAG_FORMAT': r'CTF\.Moscow\{[a-zA-Z\.0-9_-]+\}',
    # 'FLAG_FORMAT': r'VolgaCTF{[\w-]*\.[\w-]*\.[\w-]*}',
    'FLAG_FORMAT': r'adcs\{[A-Z0-9]{25}\}',

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': '275_17fc104dd58d429ec11b4a5e82041cd2',

    'SYSTEM_PROTOCOL': 'w0y_http',
    'SYSTEM_URL': 'http://172.17.0.1:5100/submit',
   # 'SYSTEM_URL': 'http://ctf.hackthe.space/submit',
    'TEAM_TOKEN': '<INPUT Tommorow>',
 #   'SYSTEM_HOST': '10.10.10.10',
   # 'SYSTEM_PORT': '31337',
    
    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_VALIDATOR': 'volgactf',
    # 'SYSTEM_HOST': 'final.volgactf.ru',
    # 'SYSTEM_SERVER_KEY': validators.volgactf.get_public_key('https://final.volgactf.ru'),

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 3 * 60,

    # VOLGA: Don't make more than INFO_FLAG_LIMIT requests to get flag info,
    # usually should be more than SUBMIT_FLAG_LIMIT
    # 'INFO_FLAG_LIMIT': 10,

    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    # ########## DO NOT FORGET TO CHANGE IT ##########
    'SERVER_PASSWORD': '5gPtUdwrHfHYg7az',

    # For all time-related operations
    'TIMEZONE': 'Europe/Vienna',
}

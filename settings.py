default_protocol = 'udp'
default_port = 1194

## add functionality for this
default_server = 'US East'

openvpn_config_file = 'config'

protocol_ports = {'udp': [53,1194,8080,9201]
                 ,'tcp': [80,110,443]}

servers = {'CA North York': 'ca.privateinternetaccess.com' 
          ,'CA Toronto': 'ca-toronto.privateinternetaccess.com' 
          ,'France': 'france.privateinternetaccess.com' 
          ,'Germany': 'germany.privateinternetaccess.com'
          ,'Hong Kong': 'hk.privateinternetaccess.com'
          ,'Netherlands': 'nl.privateinternetaccess.com'
          ,'Romania': 'ro.privateinternetaccess.com'
          ,'Sweden': 'sweden.privateinternetaccess.com'
          ,'Switzlerand': 'swiss.privateinternetaccess.com'
          ,'UK London': 'uk-london.privateinternetaccess.com'
          ,'UK Southampton': 'uk-southampton.privateinternetaccess.com'
          ,'US California': 'us-california.privateinternetaccess.com'
          ,'US East': 'us-east.privateinternetaccess.com'
          ,'US Florida': 'us-florida.privateinternetaccess.com'
          ,'US Midwest': 'us-midwest.privateinternetaccess.com'
          ,'US Seattle': 'us-seattle.privateinternetaccess.com'
          ,'US Texas': 'us-texas.privateinternetaccess.com'
          ,'US West': 'us-west.privateinternetaccess.com'}

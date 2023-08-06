
import requests
import numpy as np

from PIL import Image
from io import BytesIO

class LockedException(Exception):
    pass

class StarTrackerClient():
    def __init__(self, uri) -> None:
        self.uri = uri

    def _get(self, route, params=None):
        uri = self.uri.strip('/')
        route = route.strip('/')
        url = f'{uri}/{route}'
        r = requests.get(url, params=params)
        if r.status_code == 422:
            raise LockedException(r.text)
        else:
            r.raise_for_status()
        return r

    def _get_bool(self, route):
        r = self._get(route)
        return True if r.text == 'TRUE' else False

    def _get_ard(self, cmd, com_port):
        route = '/command/arduino/{cmd}'
        if com_port:
            route += f'/{com_port}'
        ret = self._get(route).json()
        return ret['ret'][cmd]



    def ard_flap_open(self, com_port=None):
        cmd = 'MOVE_OPEN' 
        res = self._get_ard(cmd, com_port)
        return res == cmd

    def ard_flap_close(self, com_port=None):
        cmd = 'MOVE_CLOSE' 
        res = self._get_ard(cmd, com_port)
        return res == cmd

    def ard_flap_stop(self, com_port=None):
        cmd = 'MOVE_STOP' 
        res = self._get_ard(cmd, com_port)
        return res == 'STOP'


    def ard_power_on(self, com_port=None):
        cmd = 'CAM_ON' 
        res = self._get_ard(cmd, com_port)
        return res == 'SWITCH1 ON'

    def ard_power_off(self, com_port=None):
        cmd = 'CAM_OFF' 
        res = self._get_ard(cmd, com_port)
        return res == 'SWITCH1 OFF'


    def ard_state_flap(self, com_port=None):
        return self._get_ard('STATE_FLAP', com_port)

    def ard_state_version(self, com_port=None):
        return self._get_ard('STATE_VERSION', com_port)

    def ard_state_power(self, com_port=None):
        return self._get_ard('STATE_PWR', com_port)


    def get_frame(self, overlay=True, wait_for_new_img=True):
        params = {
            'wait_next': wait_for_new_img,
            'key': 'image_out' if overlay else 'image_raw'
        }
        r = self._get('frame2', params)
        im = Image.open(BytesIO(r.content[37:]))
        return im

    def get_frame_raw(self, overlay=True, wait_for_new_img=True):
        params = {
            'wait_next': wait_for_new_img,
            'key': 'image_out' if overlay else 'image_raw'
        }
        r = self._get('frame_raw', params)
        return np.array(r.json())

    def get_row(self, wait_for_new_img=True):
        params = {'wait_next': wait_for_new_img}
        return self._get('row', params).json()

    def get_log(self, n_rows_max=-1):
        if n_rows_max > 0:
            return self._get(f'log/{n_rows_max}').json()
        else:
            return self._get(f'log/').json()

    def get_time(self):
        return self._get('timeinfo').text

    def get_procinfo(self):
        text = self._get('procinfo').text
        if text.startswith('<p>'):
            text = text[len('<p>'):]
        if text.endswith('</p>'):
            text = text[:-len('</p>')]
        return text

    def get_config(self):
        return self._get('config').json()

    def get_args(self):
        return self._get('args').json()


    def cmd_config_reload(self):
        self._get_bool('config/reload')

    def cmd_restart_consumer(self):
        return self._get_bool('restart/consumer')

    def cmd_restart_producer(self):
        return self._get_bool('restart/producer')


    def cmd_start_consumer(self):
        return self._get_bool('start/consumer')

    def cmd_start_producer(self):
        return self._get_bool('start/producer')

    def cmd_lock(self):
        return self._get_bool('lock')

    def cmd_unlock(self):
        return self._get_bool('unlock')

    def cmd_start(self):
        return self._get_bool('start')

    def cmd_start(self):
        return self._get_bool('producer_del')


    def is_alive_consumer(self):
        return self._get_bool('is_alive/consumer') 

    def is_alive_producer(self):
        return self._get_bool('is_alive/producer') 

    def is_running(self):
        return self._get_bool('is_running') 

    def is_locked(self):
        return self._get_bool('is_locked')


    def cmd_connect_cam(self):
        self._get_bool('connect/camera/on')


    def cmd_connect_sim(self):
        self._get_bool('connect/simulate/on')


    def cmd_disconnect_cam(self):
        self._get_bool('connect/camera/off')


    def cmd_disconnect_sim(self):
        self._get_bool('connect/simulate/off')



# @server.route('/frame')

# @server.route('/connect/<source>/<state>')
# @server.route('/producer_del')
# @server.route('/start')
# @server.route('/config/reload')
# @server.route('/args', methods = ['GET', 'POST'])
# @server.route('/config', methods = ['GET', 'POST'])
# @server.route('/time')
# @server.route("/procinfo")
# @server.route('/is_running')
# @server.route('/is_alive/<task>')
# @server.route('/lock')
# @server.route('/unlock')
# @server.route('/is_locked')
# @server.route('/restart/<task>')
# @server.route('/start/<task>')
# @server.route('/command/arduino/<cmd>/', defaults={'com_port': None})
# @server.route('/command/arduino/<cmd>/<com_port>')
# @server.route('/log_all/', defaults = {'n_rows_max': -1})
# @server.route('/log/', defaults = {'n_rows_max': 100})
# @server.route('/log/<n_rows_max>')

import os
from copy import deepcopy
from datetime import datetime
from time import sleep
from traceback import format_exc
from typing import List, Dict

import schedule

from divinegift.config import Settings
from divinegift.logger import Logger
from divinegift.main import get_args, get_log_param, get_list_files
from divinegift.sender import Sender


class Application:
    def __init__(self):
        self.st = datetime.now()
        self.sp = datetime.now()
        self.args = get_args()
        self.lp = get_log_param(self.args)
        self.logger = Logger()
        self.logger.set_log_level(**self.lp)

        self.settings = Settings(logger_=self.logger)
        self.settings_edited_at = None
        self.conf_file_path = self.settings.find_config_file(self.args.get('c', 'settings.yaml'))
        self.cipher_key_path = self.args.get('ck', 'key.ck')

        self.print_intro()

        self.logger.log_info(f'{"=" * 20} START {"=" * 20}')

    def __repr__(self):
        return f'Application()'

    def update_settings(self, encrypt_config=True, log_changes=False, use_yaml=True, encoding='utf-8'):
        """
        Update settings at service if it changes
        :param encrypt_config: if True will encrypt key fields in self.init_config method
        :param log_changes: if True will show changes in logs
        :param use_yaml: if True will use yaml format instead json
        :param encoding: encoding
        :return:
        """
        settings_edited_at = os.path.getmtime(self.conf_file_path)
        if settings_edited_at != self.settings_edited_at:
            self.set_settings(encrypt_config, log_changes, use_yaml, encoding)

    def run(self):
        pass

    def set_run_schedule(self):
        """
        Set schedule to run service every n time_units.
        Should be set settings variable `service_run_schedule` like string:
        every n seconds/minutes/hours/days/weeks [at [[00:]00]:00].
        E.g 1: service_run_schedule: every 10 seconds
        E.g 2: service_run_schedule: every 1 minutes at :00
        E.g 3: service_run_schedule every 1 day at 10:30:00
        :return:
        """
        service_run_schedule = self.get_settings('service_run_schedule', '').split()
        if service_run_schedule:
            every = service_run_schedule[1]
            time_unit = service_run_schedule[2]
            try:
                at = service_run_schedule[4]
                at_str = f'.at("{at}")'
            except IndexError:
                at_str = ''
            eval(f"schedule.every({every}).{time_unit}{at_str}.do(self.run)")
        else:
            schedule.every(5).seconds.do(self.run)

    def run_service(self):
        self.set_run_schedule()
        while True:
            schedule.run_pending()
            sleep(1)

    def set_settings(self, encrypt_config=True, log_changes=False, use_yaml=True, encoding='utf-8'):
        self.settings.parse_settings(self.conf_file_path, self.cipher_key_path,
                                     encoding=encoding, log_changes=log_changes, use_yaml=use_yaml)
        self.settings_edited_at = os.path.getmtime(self.conf_file_path)

        if encrypt_config:
            self.init_config()

    def init_config(self):
        """
        Encrypt config if not exist key.ck file at self.cipher_key_path
        Override it if you have another passwords which should be encrypted
        :return:
        """
        if not os.path.exists(self.cipher_key_path):
            self.settings.initialize_cipher(ck_fname=self.cipher_key_path)
            self.encrypt_password('email_conf', 'pwd')           # Change it for your config
            self.settings.save_settings(self.conf_file_path)

    def encrypt_password(self, connection_name: str, pass_field: str = 'db_pass'):
        try:
            self.settings.encrypt_password(connection_name, pass_field)
        except Exception as ex:
            self.logger.log_err(f'Could not encrypt password: {ex}')

    def get_settings(self, param=None, default=None):
        """
        Return value from settings
        :param param: desired settings key
        :param default: if param not exist return this
        :return:
        """
        return self.settings.get_settings(param, default)

    def print_intro(self):
        print(f'Process {self.args.get("name")} started!')
        log_place = os.path.join(self.lp.get("log_dir"), self.lp.get("log_name")) if self.lp.get(
            "log_name") else "ON SCREEN"
        print(f'Log will be here: {log_place}')

    def log_debug(self, *args, separator: str = ' '):
        self.logger.log_debug(*args, separator)

    def log_info(self, *args, separator: str = ' '):
        self.logger.log_info(*args, separator)

    def log_warning(self, *args, separator: str = ' '):
        self.logger.log_warn(*args, separator)

    def log_warn(self, *args, separator: str = ' '):
        self.logger.log_warn(*args, separator)

    def log_err(self, *args, separator: str = ' ', src: str = None, mode: List = None, channel: Dict = None):
        self.logger.log_err(*args, separator, src, mode, channel)

    def log_crit(self, *args, separator: str = ' '):
        self.logger.log_crit(*args, separator)

    def log_err_notif(self, *args, separator: str = ' '):
        mode = self.get_settings('monitoring')
        channel = deepcopy(self.get_settings('monitoring_channel'))
        if 'email' in mode or 'email_attach' in mode:
            channel['email'] = deepcopy(self.get_settings('email_conf'))
            channel['email']['TO'] = channel.pop('email_to')
        self.log_err(*args, separator=separator)
        src = self.get_settings('service_name', self.args.get('name'))
        self.notify(*args, separator=separator, src=src, mode=mode, channel=channel)

    def notify(self, *args, separator: str = ' ', src: str = None, mode: List = None, channel: Dict = None):
        """
        :param args:
        :param separator:
        :param msg: Error message which will logged
        :param src: Source which raised error
        :type src: string
        :param mode: List of monitoring's mode (telegram, email, email_attach, slack)
        :type mode: list
        :param channel: Dict with parameters of monitoring (e.g. {'telegram': -1001343660695}
        :type channel: dict
        :return:
        """
        error_txt = f'''An error has occurred in {src}
        Error text: {separator.join([str(x) for x in args])}\n{format_exc()}'''

        sender = Sender()

        if mode:
            if 'telegram' in mode:
                sender.send_telegram(error_txt, chat_id=channel.get('telegram', -1001343660695))
            if 'slack' in mode:
                sender.send_slack(error_txt)
            if 'email' in mode:
                sender.send_mail(error_txt, f'{src} ERROR', **channel.get('email'))
            if 'email_attach' in mode:
                if self.lp.get('log_dir', '.') and self.lp.get('log_name'):
                    log = get_list_files(self.lp.get('log_dir'), self.lp.get('log_name'), add_path=True)
                else:
                    log = []
                sender.send_mail(error_txt, f'{src} ERROR', attachments=log, **channel.get('email_attach'))

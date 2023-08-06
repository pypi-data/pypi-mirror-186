from random import random
from jennifer.agent import jennifer_agent
from .profiler import TransactionProfiler


class Transaction:
    def __init__(self, agent, start_time, environ, wmonid,
                 txid=0, elapsed=0, elapsed_cpu=0, end_time=0, sql_count=0, sql_time=0, fetch_count=0,
                 fetch_time=0, external_call_count=0, external_call_time=0, client_address=None,
                 user_hash=0, service_hash=0, guid=None, browser_info_hash=0, error_code=0, ctx_id=0, path_info=None):

        self.elapsed = elapsed
        self.elapsed_cpu = elapsed_cpu
        self.end_time = end_time
        self.sql_count = sql_count
        self.sql_time = sql_time
        self.fetch_count = fetch_count
        self.fetch_time = fetch_time
        self.external_call_count = external_call_count
        self.external_call_time = external_call_time
        self.txid = txid
        self.client_address = client_address
        self.wmonid = wmonid
        self.user_hash = user_hash
        self.guid = guid
        self.browser_info_hash = browser_info_hash
        self.error_code = error_code
        self.service_hash = service_hash
        self.incoming_remote_call = None

        self.agent = agent
        self.start_system_time = 0
        self.end_system_time = 0
        self.wmonid = wmonid
        self.thread_id = ctx_id  # in async, thread_id == ctx_id
                                 # in sync, thread_id == thread id

        if environ.get('HTTP_X_FORWARDED_FOR') is not None:
            self.client_address = environ.get('HTTP_X_FORWARDED_FOR')
        elif environ.get('HTTP_CLIENT_IP') is not None:
            self.client_address = environ.get('HTTP_CLIENT_IP')
        else:
            self.client_address = environ.get('REMOTE_ADDR', '')

        self.browser_info_hash = self.agent.hash_text(environ.get('HTTP_USER_AGENT', ''), 'browser_info')

        if path_info is None:
            path_info = environ.get('PATH_INFO', '').encode('iso-8859-1').decode('utf-8')

        self.request_method = environ.get('REQUEST_METHOD', '')
        self.query_string = environ.get('QUERY_STRING', '')
        self.start_time = start_time
        self.path_info = path_info
        self.service_hash = self.agent.hash_text(path_info)
        self.profiler = TransactionProfiler(self, self.service_hash)

    def end_of_profile(self):
        self.profiler.end()  # end root method
        self.end_system_time = self.agent.current_cpu_time()
        self.end_time = self.agent.current_time()
        self.agent.end_transaction(self)

    def to_active_service_dict(self, current_time, current_cpu_time):
        self.elapsed_cpu = current_cpu_time - self.start_system_time
        self.elapsed = current_time - self.start_time

        data = { }
        data['service_hash'] = self.service_hash
        data['elapsed'] = self.elapsed
        data['txid'] = self.txid
        data['wmonid'] = self.wmonid
        data['thread_id'] = self.thread_id
        data['client_address'] = self.client_address
        data['elapsed_cpu'] = self.elapsed_cpu

        data['sql_count'] = self.sql_count
        data['fetch_count'] = self.fetch_count
        data['start_time'] = self.start_time

        data['running_mode'] = self.profiler.running_mode
        data['running_hash'] = self.profiler.running_hash
        data['running_time'] = current_time - self.profiler.running_start_time
        data['status_code'] = self.profiler.status

        return data

    def to_dict(self):
        self.elapsed_cpu = self.end_system_time - self.start_system_time
        self.elapsed = self.end_time - self.start_time

        data = { }
        data['elapsed'] = self.elapsed
        data['elapsed_cpu'] = self.elapsed_cpu
        data['end_time'] = self.end_time
        data['sql_count'] = self.sql_count
        data['sql_time'] = self.sql_time
        data['fetch_count'] = self.fetch_count
        data['fetch_time'] = self.fetch_time
        data['external_call_count'] = self.external_call_count
        data['external_call_time'] = self.external_call_time

        data['txid'] = self.txid
        data['client_address'] = self.client_address
        data['wmonid'] = self.wmonid
        data['user_hash'] = self.user_hash
        data['guid'] = self.guid

        data['browser_info_hash'] = self.browser_info_hash
        data['error_code'] = self.error_code
        data['service_hash'] = self.service_hash

        data['start_system_time'] = self.start_system_time
        data['end_system_time'] = self.end_system_time

        data['thread_id'] = self.thread_id
        data['start_time'] = self.start_time

        return data

import os
import time
import datetime
import shutil
import hashlib
import logging
from .selenium import SeleniumExt
from .report import ReportPath
from justrpa.errors import FileDownloadError
from justrpa.utils.file import save_json_file,create_dir_for_file
from justrpa.utils.time import get_date_range_by_param

class TaskBrowser(SeleniumExt, ReportPath):
    def _init_variables(self):
        self.selenium_speed = 1
        self.account = ""
        self.home_url = "about:blank"
        self.filepath_template = ""
        self.report_period = ""
        self.execution_date = ""
        self.task_output_dir = "output/"

    def init(self, env:dict):
        self.logger = logging.getLogger("robot")
        self._init_variables()
        self.set_env_variables(env)
        self.set_account_info(env)
        self.set_browser_settings(env)
        self.set_selenium_speed(self.selenium_speed)

    def set_env_variables(self,*initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
    
    def try_get_attr(self, var_name, default_value):
        return getattr(self, var_name) if hasattr(self, var_name) else default_value
        
    def set_account_info(self, env:dict):
        account_info = env["account_info"] if "account_info" in env else {}
        if len(account_info)==0:
            self.username = ""
            self.auto_login = False
            self.auto_mfa_login = False
            self.mfa_secret = ""
            return
        self.username = account_info["username"]
        self.password = account_info["password"]
        self.mfa_secret = account_info["mfa_secret"] if "mfa_secret" in account_info else ""
        self.auto_login = (account_info["auto_login"]==1) if self.username!="" else False
        self.auto_mfa_login = (account_info["mfa_login"]==1) & self.auto_login if self.mfa_secret!="" else False
    
    def set_browser_settings(self, env:dict):
        self.new_browser = int(env['new_browser']) if 'new_browser' in env else 0
        self.attach_port = int(env['attach_port']) if 'attach_port' in env else 9222
        self.headless = bool(env['headless']) if 'headless' in env else False
        assert self.new_browser in [0,1,2], f"new_browser type {self.new_browser} not valid, check env variable."
        browser_name = env['browser'] if 'browser' in env else 'chrome'
        self.browser = browser_name.lower()
        self.new_browser = self.new_browser if self.browser=="chrome" else 1
        use_profile = False if 'useProfile' not in env else bool(env['useProfile'])
        profile_path = None if 'profilePath' not in env or len(env['profilePath'])==0 else env['profilePath']
        self.browser_info = {
            'name': browser_name,
            'use_profile': use_profile,
            'profile_path' : profile_path
        }

    def screenshot_to_output(self, filename, full_page:bool=False):
        dir_path = os.getcwd()
        dir_path = os.path.join(dir_path, self.task_output_dir)
        file_path = os.path.join(dir_path, filename)
        self.screenshot_to_dest(file_path, full_page)

    def save_json_file_to_output(self, filename, data:dict):
        save_json_file(data, self.task_output_dir, filename)
    
    def move_latest_download(self, download_dir:str, target_filename:str, limits=60, tolerant=False)->str:
        checkfile_ok, checkfile_wait, checkfile_fail = 1,2,0 
        def check_file(filename):
            file_ext = os.path.splitext(filename)[1]
            try:
                filets = os.path.getctime(filename)
                if time.time() - filets > limits:
                    self.logger.info(f"Latest file {filename} is too old.")
                    return checkfile_fail
            except FileNotFoundError as e:
                self.logger.info(f"Latest file {filename} is gone. {e}")
                return checkfile_wait
            if file_ext == '.crdownload' or file_ext == '.part':
                self.logger.info(f"Download has not finished...wait 30s and retry")
                return checkfile_wait
            return checkfile_ok
        def copy_ext(filename, target_filename):
            file_ext = os.path.splitext(filename)[1]
            return target_filename.rsplit('.', 1)[0] + file_ext
        download_dir = os.path.abspath(download_dir)
        if os.path.isdir(download_dir) == False or len(os.listdir(download_dir))==0:
            self.logger.info(f"no file in {download_dir}")
            return ""
        find_new_file = lambda x: max([os.path.join(x, f) for f in os.listdir(x)], key=os.path.getctime)
        filename = find_new_file(download_dir)
        retry, limit = 0, 10
        while (retry < limit) and (check_file(filename) == checkfile_wait):
            self.sleep_long()
            retry = retry + 1
            filename = find_new_file(download_dir)
        if check_file(filename) != checkfile_ok:
            self.logger.info(f"Download_dir: {download_dir}. File not found. ")
            if tolerant==False:
                raise FileDownloadError(f"File to download not found in target location.")
            else:
                self.logger.warning(f"Download file failed. target:{target_filename}")
                return ""
        else:
            self.logger.info(f"File download finished:{filename}")
        target_filename = copy_ext(filename, target_filename)
        target_filename = os.path.abspath(target_filename)
        create_dir_for_file(target_filename)
        shutil.move(filename, target_filename) 
        return target_filename

    def get_report_hash_key(self):
        return ["report_module", "report_class", "date_range", "site"]

    def get_report_hash(self, params:dict):
        def generate_report_name(task_param:dict, char_length=8):
            values = [str(value) for value in task_param.values()]
            str_all = "_".join(values)
            hash_object = hashlib.sha512(str_all.encode())
            hash_hex = hash_object.hexdigest()
            return hash_hex[0:char_length]
        key_columns =  self.get_report_hash_key()
        key_params = {key: value for key, value in params.items() if key in key_columns}
        return generate_report_name(key_params)

    def get_report_module(self, task_params:dict)->str:
        """
        Default to taskname.
        """
        return task_params['report_module'] if 'report_module' in task_params else self.taskname
    
    def get_report_class(self, task_params:dict)->str:
        """
        Default to taskname.
        """
        return task_params['report_class'] if 'report_class' in task_params else self.taskname

    def get_report_period(self, date_range:str, shift:int=0):
        start_date,_ = self.get_date_range_dates(date_range, shift)
        return start_date[:7]
    
    def get_date_range_dates(self, date_range:str, shift:int=0):
        """
        Get date range dates, return start_date, and end_date in "%Y-%m-%d" format
        """
        current = datetime.datetime.now()
        if self.execution_date:
            try:
                current = datetime.datetime.strptime(self.execution_date,"%Y-%m-%d")
            except ValueError:
                self.logger.error(f"execution_date: {self.execution_date} is not valid and not used.")
        return get_date_range_by_param(current, date_range, shift) 

    def pre_process_params(self, params:dict):
        if params is None:
            return {}
        if "date_range" in params:
            start_date, end_date =  self.get_date_range_dates(params["date_range"])  
            params['start_date'] = start_date
            params['end_date'] = end_date
            params["report_period"] = self.get_report_period(params["date_range"])
        params["report_module"] = self.get_report_module(params)
        params["report_class"] = self.get_report_class(params)
        params["report_name"] = self.get_report_hash(params)
        return params
    
    def go_to_site(self, site:str):
        self.logger.info(f"Go to site: {site}")
    
    def before_run_reports(self, report_params:dict):
        self.logger.info(f"Before run reports: {report_params.keys()}")
        return report_params

### implement task process steps -------------------------------
    def run_task_retry_handler(self, task_context:dict):
        restore_url = task_context["restore_url"] if "restore_url" in task_context else ""
        self.logger.info(f"Before retry, go back to start page. url: {restore_url}")
        if restore_url:           
            self.go_to(restore_url)
            
    def skip_retry_check(self, ex:Exception):
        critial_erros = ["WindowNotFound","NoOpenBrowser","BrowserNotFoundError","NoSuchWindowException",
        "NotLoggedInError","ProgramError","ParameterError"]
        skip_retry_errors = ["NoDownloadLinkError","ReportOptionError",
        "NoReportError","ParameterError","TooManyExceptionsError"]
        ex_name = ex.__class__.__name__ 
        if ex_name in critial_erros:
            return True
        if ex_name in skip_retry_errors:
            return True
        return False

## ----------------- error_handler decorator--------------------
    def error_handler(func):
        def decorate(self,*args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                self.handle_error(e)
                raise e
        return decorate

## ----------------- retry decorator--------------------
    def retry(func):
        def decorate(self,*args, **kwargs):
            c = 3
            while c > 0:
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    c -= 1
                    if self.skip_retry_check(e) == True:
                        c = 0
                    if c == 0:
                        raise e 
                    self.run_task_retry_handler(*args, **kwargs)  
        return decorate 

    @error_handler
    def before_run(self, task_context:dict)->dict:
        if hasattr(self, "account") == False:
            self.account = ""
        assert hasattr(self, "account"), "account is missing from env variables."
        assert hasattr(self, "home_url")
        account = self.account
        task_context["account"] = account
        self.logger.info(f"Start task with account: {account}")
        report_params = task_context["all_task_params"]
        task_context["all_task_params"] = self.before_run_reports(report_params)
        self.prepare_browser(self.home_url)
        return task_context

    @error_handler   
    def process_task_params(self, task_context:dict)->dict:
        report_params = task_context["all_task_params"]
        result = {}
        for site, site_reports in report_params.items():
            self.logger.info(f"process task params for site: {site}")
            site_combinations = []
            date_range_last = ""
            for report in site_reports:
                new_item = report.copy()
                new_item["site"] = site
                new_item = self.pre_process_params(new_item)
                site_combinations.append(new_item)
                date_range_last = new_item["date_range"] if "date_range" in new_item else date_range_last
            result[site] = site_combinations
        task_context["all_task_params"] = result
        task_context["report_period"] = self.get_report_period(date_range_last) if date_range_last else self.report_period
        return task_context
    
    @error_handler
    def switch_site(self, task_context:dict)->dict:
        site = task_context["site"]
        self.go_to_site(site)
        task_context["restore_url"] = self.location
        return task_context

    @error_handler
    def before_task_run(self, task_context:dict)->dict:
        return task_context

    @retry
    @error_handler
    def run_task(self, task_context:dict)->dict:
        taskmethod  = task_context["taskmethod"]
        params = task_context["task_params"]
        func = getattr(self, taskmethod)
        paths = func(params)
        task_result = params.copy()
        task_result["path"] = paths if isinstance(paths, list) else [paths]
        task_context["task_status"] = "success"
        task_context["task_result"] = task_result
        return task_context

    @error_handler
    def after_task_run(self, task_context:dict)->dict:
        return task_context

    @error_handler
    def task_end(self, task_context:dict)->dict:
        self.cleanup()
        return task_context
    
    @error_handler
    def after_run(self, task_context:dict)->dict:
        return task_context

### ------------------------------------------------------------
    def handle_error(self, ex):
        error_id = int(time.time())
        self.logger.info(f"Error track id: {error_id}")
        self.logger.error(ex, exc_info=True, stack_info=True)
        filename = f"error_{error_id}.jpg"
        try:
            self.screenshot_to_output(filename, full_page=False)
        except Exception as e:
            self.logger.error(f"Error taking screenshot, target filename:{filename}")
            self.logger.error(e, exc_info=True)
    

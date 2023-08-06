# coding=utf-8
import logging
from justrpa.utils.config import load_merge_conf, load_override_conf
from justrpa.utils.time import get_report_period
from justrpa.errors import NoSiteError
from justrpa.task.executer import TaskExecuter
from justrpa.utils.file import save_json_file

class TaskHandler:
    def __init__(self):
        super().__init__()
        self.load_all_config()
    
    def load_all_config(self):
        self.logger = logging.getLogger("robot")
        self.env = self.load_env_variables()
        self.load_account()
        self.load_tasks()
        self.load_task_params()
        self.load_task_configs()
        self.init_account()
        self.generate_default_task_params()

    def load_env_variables(self):
        return load_merge_conf("env.json", "conf", "devdata")

    def load_conf(self, filename:str):
        return load_override_conf(filename, "conf", "devdata")

    def load_account(self):
        self.accounts = self.load_conf('account.json')
        if len(self.accounts)==0:
            self.accounts = [{"name":""}]

    def load_tasks(self):
        self.account_tasks = self.load_conf('task_sites.json')

    def load_task_params(self):
        self.task_params = self.load_conf('task_params.json')
    
    def load_task_configs(self):
        configfile = "task_configs.json" if "taskconfig" not in self.env else self.env["taskconfig"]
        self.task_configs = self.load_conf(configfile)
    
    def init_account(self):
        acc = self.env['account'] if 'account' in self.env else ""
        self.account = self.get_account(acc)
        self.env['account'] = self.account['name']
        self.env['account_info'] = self.account
    
    def get_task_params(self, account:str, taskname:str)->dict:
        # print(self.account_tasks)
        tasks = self.account_tasks[account]
        assert isinstance(tasks, dict) and (taskname in tasks), f"Task {taskname} is not found for account {account}"
        task_sites = tasks[taskname]
        account_sites = self.get_account(account)['sites']
        site_params = {}
        for site in task_sites:
            # print(f"site:{site}")
            if site not in account_sites:
                continue
            if isinstance(task_sites, dict):
                site_params[site] = task_sites[site]
            else:
                assert isinstance( self.task_params, dict) and (taskname in  self.task_params), f"Task {taskname} has no default params settings."
                site_params[site] = self.task_params[taskname]
        return site_params
    
    def generate_default_task_params(self):
        account_name = self.account['name']
        if account_name in self.account_tasks:
            return
        assert ("*" in self.account_tasks), f"task_sites.json error. No tasks defined for neither {account_name} or '*'."
        account_tasks = {}
        for taskname, sites_array in self.account_tasks["*"].items():
            site_for_account = [site for site in sites_array if site in self.account["sites"]]
            if len(site_for_account) > 0:
                account_tasks[taskname] = site_for_account
        self.account_tasks[account_name] = account_tasks
    
    def get_account(self, account_name:str="")->dict:
        if account_name=="":
            return self.accounts[0]
        else:
            selected = [acc for acc in self.accounts if acc['name']==account_name]
            assert len(selected)>0, f"Account {account_name} not found"
            return selected[0]

    def get_task_handler(self, taskname:str):
        assert taskname in self.task_configs, f"Task {taskname} config missing."
        assert "handler" in self.task_configs[taskname], f"Task {taskname} handler config missing."
        return self.task_configs[taskname]["handler"]

    def get_default_period_from_task_params(self, task_params):
        dr_task = ""
        for _, tasks in task_params.items():
            for params in tasks:
                if "date_range" in params:
                    dr_task = params["date_range"]
                    break
        dr = self.env['date_range'] if dr_task=="" and 'date_range' in self.env else dr_task
        dr = "LAST_MONTH" if dr=="" else dr
        execution_date = self.env['execution_date'] if 'execution_date' in self.env else ""
        return get_report_period(dr,execution_date=execution_date)

    def run(self, taskname:str=''):
        # use Environment variables.
        assert taskname!="" or "taskname" in self.env, f"taskname {taskname} is not presented either in cmd or env variables"
        taskname = self.env['taskname'] if taskname=='' else taskname
        task_params = self.get_task_params(self.account['name'] , taskname)
        report_period = self.get_default_period_from_task_params(task_params)
        self.env['report_period'] = report_period
        self.env['taskname'] = taskname
        try:
            self.logger.info(f"Before run task: {taskname}. params: {task_params}")
            if len(task_params) ==0:
                raise NoSiteError("No site specified for this task, please check settings.")
            self.do_task(taskname, task_params)
            self.logger.info(f"Run task completed.")
        except Exception as ex:
            self.logger.error(f"Run task failed.")
            self.logger.error(ex, exc_info=True, stack_info=True)
            self.save_task_erors(self.account['name'], report_period, taskname, ex)

    def get_env_variables(self, taskname:str):
        current = self.env.copy()
        if self.task_configs and taskname in self.task_configs:
            current.update(self.task_configs[taskname])
        return current

    def do_task(self, taskname, task_params):
        # print(f"taskname:{taskname} params:{task_params}")
        browser_name, method_name = self.get_task_handler(taskname)
        env = self.get_env_variables(taskname)
        t = TaskExecuter(taskname, browser_name, method_name, env, task_params)
        task_context = t.run()
        return task_context

    def get_error_msg(self, ex):
        msg_map = {
            "WindowNotFound": "机器人浏览器窗口被意外关闭,请重试.",
            "NoOpenBrowser": "机器人找不到可用浏览器窗口,请重试.",
            "BrowserNotFoundError": "RPA浏览器未打开,机器人无法启动,请打开后重试.",
            "NoSuchWindowException": "机器人浏览器窗口被意外关闭,请重试.",
            "BrowserNotAvailable": "RPA浏览器未打开,机器人无法启动,请打开后重试.",
            "NotLoggedInError": "账号未在浏览器登录,请登录后重试.",
            "LoginFailError": "自动登录失败,请检查账号密码设置,或者手动登录后重试.",
            "MFAFailError": "MFA(两步认证)失败,请检查相关设置,或者手动登录后重试.",
            "NoSiteError": "本任务没有关联站点,请检查相关设置"
        }
        ex_name = ex.__class__.__name__
        if ex_name not in msg_map:
            return str(ex)
        return msg_map[ex_name]

    def get_user_actions(self, ex):
        action_map = {
            "WindowNotFound": "Browser window has been closed, please open and retry task.",
            "NoOpenBrowser": "RPA Browser is not opened, please open and retry task.",
            "BrowserNotFoundError": "RPA Browser is not opened, please open and retry task.",
            "NoSuchWindowException": "Browser window has been closed, please open and retry task.",
            "BrowserNotAvailable": "RPA Browser is not opened, please open and retry task.",
            "NotLoggedInError": "Please login in the browser.",
            "LoginFailError": "Login fail, please check your login settings or login in the browser manually.",
            "MFAFailError": "Two factor authentication failed, please check your settings or do it in the browser manually",
            "NoSiteError": "No site has been set to this task, please check task settings."
        }
        ex_name = ex.__class__.__name__
        if ex_name not in action_map:
            return "Check and retry or contact support."
        return action_map[ex_name]

    def save_task_erors(self, account:str, report_period:str, taskname:str, err:Exception, output_dir:str='output/', filename:str='task_result.json'):
        result = {
            'account': account,
            'taskname': taskname,
            'report_period': report_period,
            'status': "Error",
            'error': self.get_error_msg(err),
            'action': self.get_user_actions(err)
        }
        save_json_file(result, output_dir, filename)
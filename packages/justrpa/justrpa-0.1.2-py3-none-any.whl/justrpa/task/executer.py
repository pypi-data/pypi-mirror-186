# coding=utf-8

from copy import deepcopy
from justrpa.utils.file import save_json_file

def get_klass(full_class_name:str):
    symbols = full_class_name.split(".")
    classname = symbols[-1]
    if len(symbols)==1:
        klass = globals()[classname]
    else:
        classmodule = ".".join(symbols[0:-1])
        mod = __import__(classmodule, fromlist=[classname])
        klass = getattr(mod, classname)
    return klass

def calc_metrics(total:dict, success:dict, failure:dict):
    metrics = {}
    total_suc = 0
    total_fail = 0
    for site, params in total.items():
        suc = len(success[site]) if site in success else 0
        fail = len(failure[site]) if site in failure else 0
        metrics[site] = {
            'success': suc,
            'fail': fail,
            'total': suc+fail
        }
        total_suc = total_suc + suc
        total_fail = total_fail + fail
    metrics['total'] = total_suc + total_fail
    metrics['success'] = total_suc
    metrics['fail'] = total_fail
    return metrics

def gen_task_result(account:str, report_period:str, taskname:str, total:dict, success:dict, failure:dict)->dict:
    metrics = calc_metrics(total, success, failure)
    status="Complete" if metrics['fail']==0 else "Partial"
    result = {
        'account': account,
        'taskname': taskname,
        'report_period': report_period,
        "period_type": "Monthly",
        'status': status,
        'metrics': metrics,
        'data':{
            'total':total,
            'success':success,
            'failure': failure
        }
    }
    return result

def save_tasks_summary(account:str,report_period:str,taskname:str, total:dict, success:dict, failure:dict, output_dir:str='output/', filename:str='task_result.json'):
    result = gen_task_result(account, report_period,taskname, total, success, failure)
    save_json_file(result, output_dir, filename)
    return result['metrics']

def save_fail_tasks(account:str, taskname:str, failure:dict, output_dir:str='output/', filename:str='task_failed.json'):
    result = {
        account:{
            taskname:failure
        }
    }
    save_json_file(result, output_dir, filename)

class TaskExecuter:
    def __init__(self, taskname:str, taskclass:str, taskmethod:str, env_variables:dict, task_params:dict):
        self.taskname = taskname
        self.taskclass = taskclass
        self.taskmethod = taskmethod
        self.env_variables = env_variables.copy()
        self.task_params = task_params.copy()
        self.init_task_class()

    def init_task_class(self):
        klass = get_klass(self.taskclass)
        self.taskinstance = klass()
        self.taskinstance.init(self.env_variables)
    
    def call_taskclass_method(self, method_name:str, task_context:dict):
        method = getattr(self.taskinstance, method_name)
        if task_context:
            return method(task_context)
        else:
            return method()
    
    def run_process_chain(self, task_context:dict, method_chain:list):
        for meth in method_chain:
            if callable(meth):
                task_context = meth(task_context)
            else:
                task_context = self.call_taskclass_method(meth, task_context)
        return task_context

    def run_tasks_by_site(self, task_context:dict)->dict:
        res_success = {}
        res_failure = {}
        task_params = task_context["all_task_params"]
        level_two_chain = ["before_task_run", "run_task", "after_task_run"]
        for site, site_reports in task_params.items():
            task_context["site"] = site
            task_context = self.call_taskclass_method("switch_site", task_context)
            success, failure = [],[]
            for params in site_reports:
                task_context["task_params"] = params
                task_context = self.run_process_chain(task_context, level_two_chain)
                if task_context["task_status"] == "success":
                    success.append(task_context["task_result"])
                else:
                    failure.append(params)
            res_success[site] = success
            res_failure[site] = failure
        task_context["res_success"] = res_success
        task_context["res_failure"] = res_failure
        return task_context
    
    def generate_task_outputs(self, task_context:dict)->dict:
        account = task_context["account"]
        total = task_context["all_task_params"]
        res_success = task_context["res_success"]
        res_failure = task_context["res_failure"]
        report_period = task_context["report_period"]
        taskname = task_context["taskname"]
        metrics = save_tasks_summary(account, report_period, self.taskname, total, res_success, res_failure)
        save_fail_tasks(account, taskname, res_failure)
        return task_context

    def run(self):
        task_context = {}
        task_context['all_task_params'] = self.task_params
        task_context['taskmethod'] =  self.taskmethod
        task_context['taskclass'] = self.taskclass
        task_context['taskname'] = self.taskname
        first_level_chain = ["before_run", "process_task_params", self.run_tasks_by_site, "after_run", self.generate_task_outputs]
        try:
            task_context = self.run_process_chain(task_context, first_level_chain)
        finally:
            task_context = self.call_taskclass_method("task_end", task_context)
        return task_context
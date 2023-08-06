import os
import datetime
from justrpa.utils.site import get_site_short, get_site_short_cn
#
# filepath_template
# module_filepath_template
# replace_template
class ReportPath:
    DEFAULT_TEMPLATE = "{account}/{site}/{taskname}/{account}-{site}-{filetag}-{timetag}.csv"
    def try_get_attr(self, var_name, default_value):
        return getattr(self, var_name) if hasattr(self, var_name) else default_value

    def get_template(self, site:str, module:str)->str:
        replaced = self.get_replace_template(site, module)
        if replaced:
            return replaced
        module_template = self.get_module_filepath_template(module)
        if module_template:
            return module_template
        return self.get_filepath_template()
    
    def get_filepath_template(self)->str:
        return self.try_get_attr('filepath_template', self.DEFAULT_TEMPLATE)

    def get_module_filepath_template(self, module:str)->str:
        if module=="":
            return None
        templates = self.try_get_attr('module_filepath_template', {})
        if  module not in templates:
            return None
        return templates[module]

    def get_replace_template(self, site, module):
        if site=="" or module == "":
            return None
        replace_templates = self.try_get_attr('replace_template', {})
        if site not in replace_templates:
            return None
        site_templates = replace_templates[site]
        self.logger.info(f"replaced site templates found for {site} - {module}")
        if 'module_filepath_template' in site_templates and module in site_templates['module_filepath_template']:
            return site_templates['module_filepath_template'][module]
        elif 'filepath_template' in site_templates:
            return site_templates['filepath_template']
        else:
            return None

    def build_filename(self, template:str="", **kwargs)->str:
        """
        Support kwargs:
        - account
        - site
        - taskname
        - filetag
        - timetag
        """
        params = kwargs.copy()
        if template=="":
            site = params["site"] if "site" in params else ""
            module = params["module"] if "module" in params else ""
            template = self.get_template(site, module)
        if "site" in params:
            params["site_short"] = get_site_short(params["site"])
            params["site_short_cn"] = get_site_short_cn(params["site"])
            params["site"] = params["site"].replace(" ", "")
        if "account" not in params:
            params['account'] = self.account
        if params['account'] != None:
            params['account_trim'] = params['account'].split("-")[0]
        if "taskname" not in params:
            params['taskname'] = self.taskname
        if "today" not in params:
            params['today'] = datetime.datetime.now().strftime("%Y-%m-%d")
        if "timetag" not in params:
            params['timetag'] = params['start_date'][:7] if 'start_date' in params else ''
        if "filetag" not in params:
            params['filetag'] = ""
        filepath = template.format(**params)
        if "fileext" in params:
            filepath = filepath.rsplit('.', 1)[0] + params['fileext']
        return filepath
    
    def build_filepath(self, template:str="", **kwargs)->str:
        dir_path = os.getcwd()
        dir_path = os.path.join(dir_path, self.target_dir)
        filename = self.build_filename(template, **kwargs)
        return os.path.join(dir_path, filename)
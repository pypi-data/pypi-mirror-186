
class JustRpaException(Exception):
    pass

class BrowserNotAvailable(JustRpaException):
    pass

class NotLoggedInError(JustRpaException):
    pass

class LoginFailError(JustRpaException):
    pass

class MFAFailError(JustRpaException):
    pass

class GotoPageFailError(JustRpaException):
    pass

class ReportOptionError(JustRpaException):
    pass

class NoDownloadLinkError(JustRpaException):
    pass

class FileDownloadError(JustRpaException):
    pass

class NoReportError(JustRpaException):
    pass

class ProgramError(JustRpaException):
    pass

class NoSiteError(JustRpaException):
    pass

class ParameterError(JustRpaException):
    pass

class TooManyExceptionsError(JustRpaException):
    pass

class ErrorCounter:
    def __init__(self, limit=5):
        self.limit = limit
        self.counter_map = {}

    def reset(self, category=""):
        self.counter_map[category] = 0
    
    def add(self, category=""):
        if category not in self.counter_map:
            self.counter_map[category] = 0
        self.counter_map[category] = self.counter_map[category] + 1
        self.check(category)
    
    def get(self, category=""):
        return self.counter_map[category] if category in self.counter_map else 0
    
    def check(self, category=""):
        if self.get(category) >= self.limit:
            raise TooManyExceptionsError(f"Too many exceptions. Category:{category}, Limit:{self.limit}")

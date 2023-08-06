
class AmazonLibraryException(Exception):
    pass

class BrowserNotAvailable(AmazonLibraryException):
    pass

class NotLoggedInError(AmazonLibraryException):
    pass

class LoginFailError(AmazonLibraryException):
    pass

class MFAFailError(AmazonLibraryException):
    pass

class GotoPageFailError(AmazonLibraryException):
    pass

class ReportOptionError(AmazonLibraryException):
    pass

class NoDownloadLinkError(AmazonLibraryException):
    pass

class FileDownloadError(AmazonLibraryException):
    pass

class NoReportError(AmazonLibraryException):
    pass

class ProgramError(AmazonLibraryException):
    pass

class NoSiteError(AmazonLibraryException):
    pass

class ParameterError(AmazonLibraryException):
    pass

class TooManyExceptionsError(AmazonLibraryException):
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

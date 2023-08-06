import sys
import inspect

from mumuki.base import BaseMumuki

class Mumuki(BaseMumuki):
    def _prepare_before_visit(self):
        frame = inspect.stack()[2]
        self.__start_line = frame.lineno
        self.__file = frame.filename

    def _register_globals(self):
        pass

    def _source_missing(self):
        with open(self.__file) as f:
            return "".join(f.readlines()[self.__start_line:self.__end_line-1])

    def _connect_after_visit(self):
        self._get_exercise()
        print("OK")

    def _prepare_before_test(self):
        frame = inspect.stack()[2]
        self.__end_line = frame.lineno

    def _report_results(self, results):
        print(results['status'])

    def _offline(self):
        return sys.flags.interactive
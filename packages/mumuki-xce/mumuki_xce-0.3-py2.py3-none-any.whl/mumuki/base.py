import requests
import inspect

from mumuki.i18n import Locale

class BaseMumuki():
    def __init__(self, token:str, locale:str, url = "https://mumuki.io"):
        self._token = token
        self._url = url
        self._locale = Locale(locale)
        self._solution = None
        self._connected = False
        self._register_globals()

    def visit(self, organization:str, exercise):
        self._prepare_before_visit()

        self.__organization = organization
        self._exercise_id = int(exercise)

        if self._offline():
            return

        try:
            self._connect_after_visit()
            self._connected = True
        except:
            self._report_auth_error()

    def _solution_url(self):
        return f"{self._exercise_url()}/solutions"

    def _exercise_url(self):
        return f"{self._url}/{self.__organization}/exercises/{self._exercise_id}"

    def _headers(self):
        return { "Authorization": f"Bearer {self._token}" }

    def _get_exercise(self):
        return requests.get(
             self._exercise_url(),
             headers = self._headers())

    def _post_solution(self):
        return requests.post(
            self._solution_url(),
            json = { "solution": { "content": self._solution } },
            headers = self._headers())

    def register_solution(self, function=None):
        self._solution = self._get_source(function)

    def get_solution(self):
        return self._solution

    def test(self, function=None):
        self._prepare_before_test()
        if self._solution is None:
            self.register_solution(function)
        self._submit()

    def _submit(self):
        if self._offline():
            return

        if not self._connected:
            self._report_auth_error()
            return

        result = self._post_solution()
        if result.status_code == 403:
            self._report_auth_error()
        else:
            self._report_results(result.json())

    def _get_source(self, function=None):
        if type(function) == str:
            return function
        if function is not None:
            lines = inspect.getsourcelines(function)[0][1:]
            indent_size = inspect.indentsize("".join(line.rstrip("\n\t ") for line in lines))
            return "".join(line[indent_size:] for line in lines)
        else:
            return self._source_missing()

    def _report_auth_error(self):
        print(self._locale.translate("could_not_load_exercise", id = self._exercise_id, url = self._exercise_url()))

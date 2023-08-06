from bs4 import BeautifulSoup
from IPython.core.display import HTML
from IPython.display import display
from IPython.core.getipython import get_ipython

from mumuki.base import BaseMumuki

def soup(html):
    s = BeautifulSoup(html, "html.parser")
    for link in s.find_all("a"):
        if 'download' not in link.attrs:
            link['target'] = '_blank'
    return s

def html(soup: BeautifulSoup):
    return HTML(str(soup))

class IMumuki(BaseMumuki):
    def show(self):
        s = soup(self._get_exercise().text)
        display(html(s.body.find_all("h1")[0]))
        display(html(s.body.find_all("div", {"class":"exercise-assignment"})[0]))

    def _register_globals(self):
        def solution(_line, cell):
            self.register_solution(cell)
            get_ipython().run_cell(cell)

        ip = get_ipython()
        if ip:
            ip.register_magic_function(solution, 'cell', 'solution')
        else:
            raise RuntimeError(self._locale.translate("no_ipython"))

    def _source_missing(self):
        raise RuntimeError(self._locale.translate("magic_cell_missing"))

    def _prepare_before_visit(self):
        pass

    def _connect_after_visit(self):
        self.show()

    def _prepare_before_test(self):
        pass

    def _report_results(self, results):
        display(html(soup(results["html"])))

    def _offline(self):
        return False

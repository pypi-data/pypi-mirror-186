import pytest

from mumuki.interactive import IMumuki, soup
from bs4 import BeautifulSoup

from IPython.testing.globalipapp import get_ipython
import pytest

def setup_module():
    get_ipython()

def test_can_create_with_default_url():
    mumuki = IMumuki("token", "es")
    assert mumuki._url == "https://mumuki.io"

def test_reports_failed_visits_en(capsys):
    mumuki = IMumuki("token", "en", "http://localhost")
    mumuki.visit("nonexistent", 100)

    captured = capsys.readouterr()
    assert captured.out == "Could not access exercise 100. Please visit http://localhost/nonexistent/exercises/100 and verify the instructions\n"

def test_reports_failed_visits_es(capsys):
    mumuki = IMumuki("token", "es", "http://localhost")
    mumuki.visit("nonexistent", 100)

    captured = capsys.readouterr()
    assert captured.out == "No se pudo acceder al ejercicio 100. Visitá http://localhost/nonexistent/exercises/100 y verificá las instrucciones\n"

def test_reports_failed_visits_pt(capsys):
    mumuki = IMumuki("token", "pt", "http://localhost")
    mumuki.visit("nonexistent", 100)

    captured = capsys.readouterr()
    assert captured.out == "Não foi possível acessar o exercício 100. Visite http://localhost/nonexistent/exercises/100 e verifique as instruções\n"



def test_is_never_offline():
    mumuki = IMumuki("token", "es")
    assert not mumuki._offline()

def test_test_fails_if_there_is_no_magic_cell_en():
    mumuki = IMumuki("token", "en")
    with pytest.raises(RuntimeError) as e:
      mumuki.test()

    assert "Please ensure to mark you solution cell with %%solution" in str(e.value)

def test_test_fails_if_there_is_no_magic_cell_es():
    mumuki = IMumuki("token", "es")
    with pytest.raises(RuntimeError) as e:
      mumuki.test()

    assert "Asegurate de marcar tu celda de solución con %%solution" in str(e.value)


def test_test_fails_if_there_is_no_magic_cell_pt():
    mumuki = IMumuki("token", "pt")
    with pytest.raises(RuntimeError) as e:
      mumuki.test()

    assert "Certifique-se de marcar sua célula de solução com %%solution" in str(e.value)


def test_makes_links_open_in_new_window():
    body = soup(
        """
        <a class="btn btn-complementary w-100" role="button"
          href="https://mumuki.io/central/exercises/1"><span
            class="fa5-text-r">Siguiente Ejercicio: Ejemplo</span><i
            class="fas fa-chevron-right"></i>
        </a>
        """
    )
    assert body == BeautifulSoup(
        """
        <a class="btn btn-complementary w-100" role="button"
          href="https://mumuki.io/central/exercises/1" target="_blank"><span
            class="fa5-text-r">Siguiente Ejercicio: Ejemplo</span><i
            class="fas fa-chevron-right"></i>
        </a>
        """,
        "html.parser",
    )


def test_leaves_download_links_as_is():
    body = soup(
        """
        <a download="solution.py"
          href="data:application/octet-stream,content">
          <i class="fas fa-download"></i>
          <span class="fa5-text">Descargá lo que hiciste</span>
        </a>
        """
    )
    assert body == BeautifulSoup(
        """
        <a download="solution.py"
          href="data:application/octet-stream,content">
          <i class="fas fa-download"></i>
          <span class="fa5-text">Descargá lo que hiciste</span>
        </a>
        """,
        "html.parser",
    )

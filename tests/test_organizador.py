import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from organizador import categoria_do_arquivo, organizar


class TestOrganizador(unittest.TestCase):
    def test_categorias(self):
        self.assertEqual(categoria_do_arquivo(Path("foto.JPG")), "Imagens")
        self.assertEqual(categoria_do_arquivo(Path("aula.pdf")), "Documentos")
        self.assertEqual(categoria_do_arquivo(Path("xyz.abc")), "Outros")

    def test_organiza_e_nao_perde_arquivos(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            (pasta / "a.png").write_text("1")
            (pasta / "b.pdf").write_text("2")
            organizar(pasta)
            self.assertTrue((pasta / "Imagens" / "a.png").exists())
            self.assertTrue((pasta / "Documentos" / "b.pdf").exists())

    def test_simular_nao_move(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            (pasta / "a.png").write_text("1")
            organizar(pasta, simular=True)
            self.assertTrue((pasta / "a.png").exists())

    def test_nome_repetido_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            (pasta / "Imagens").mkdir()
            (pasta / "Imagens" / "a.png").write_text("antigo")
            (pasta / "a.png").write_text("novo")
            organizar(pasta)
            self.assertEqual((pasta / "Imagens" / "a.png").read_text(), "antigo")
            self.assertEqual((pasta / "Imagens" / "a (1).png").read_text(), "novo")


if __name__ == "__main__":
    unittest.main()

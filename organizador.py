"""
Organizador de Arquivos em Python
Autor: Thyago Ferreira (https://github.com/thyagodev021)

Separa os arquivos de uma pasta em subpastas por tipo (Imagens, Documentos,
Vídeos...). Tem modo de simulação (--simular) para ver o que seria feito
antes de mover qualquer coisa.

Uso:
    python organizador.py CAMINHO_DA_PASTA
    python organizador.py CAMINHO_DA_PASTA --simular
"""

import argparse
import shutil
import sys
from pathlib import Path

CATEGORIAS = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audios": {".mp3", ".wav", ".flac", ".ogg", ".m4a"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Codigo": {".py", ".java", ".js", ".html", ".css", ".c", ".cpp", ".rs", ".go", ".php", ".sql"},
    "Programas": {".exe", ".msi", ".apk", ".dmg"},
}


def categoria_do_arquivo(arquivo: Path) -> str:
    """Devolve o nome da categoria de acordo com a extensão do arquivo."""
    extensao = arquivo.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"


def destino_sem_conflito(destino: Path) -> Path:
    """Se já existir um arquivo com o mesmo nome, cria 'nome (1).ext', 'nome (2).ext'..."""
    if not destino.exists():
        return destino
    contador = 1
    while True:
        novo = destino.with_name(f"{destino.stem} ({contador}){destino.suffix}")
        if not novo.exists():
            return novo
        contador += 1


def organizar(pasta: Path, simular: bool = False) -> dict:
    """Organiza os arquivos da pasta e devolve a contagem por categoria."""
    resumo: dict = {}

    for arquivo in sorted(pasta.iterdir()):
        if not arquivo.is_file() or arquivo.name.startswith("."):
            continue

        categoria = categoria_do_arquivo(arquivo)
        destino = destino_sem_conflito(pasta / categoria / arquivo.name)

        print(f"{arquivo.name}  ->  {categoria}/{destino.name}")
        if not simular:
            destino.parent.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino))

        resumo[categoria] = resumo.get(categoria, 0) + 1

    return resumo


def main() -> int:
    parser = argparse.ArgumentParser(description="Organiza os arquivos de uma pasta por tipo.")
    parser.add_argument("pasta", help="caminho da pasta que será organizada")
    parser.add_argument("--simular", action="store_true",
                        help="apenas mostra o que seria feito, sem mover nada")
    args = parser.parse_args()

    pasta = Path(args.pasta).expanduser()
    if not pasta.is_dir():
        print(f"Erro: '{pasta}' não é uma pasta válida.")
        return 1

    resumo = organizar(pasta, simular=args.simular)

    if not resumo:
        print("Nenhum arquivo para organizar.")
        return 0

    total = sum(resumo.values())
    modo = "seriam movidos" if args.simular else "movidos"
    print(f"\n{total} arquivo(s) {modo}:")
    for categoria, quantidade in sorted(resumo.items()):
        print(f"  {categoria}: {quantidade}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

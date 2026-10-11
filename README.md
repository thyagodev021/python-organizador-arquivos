# 🗂️ Organizador de Arquivos em Python

Script de terminal que organiza uma pasta bagunçada (como o Downloads) separando os arquivos em subpastas por tipo: Imagens, Documentos, Vídeos, Áudios, Compactados, Código, Programas e Outros.

## Funcionalidades

- Organiza por extensão do arquivo
- Modo `--simular`: mostra o que seria feito sem mover nada
- Não sobrescreve arquivos: se o nome já existir, cria `nome (1).ext`
- Mostra um resumo no final
- Testes automáticos com `unittest`

## Como usar

Requisito: Python 3.8 ou superior (sem bibliotecas externas).

```bash
git clone https://github.com/thyagodev021/python-organizador-arquivos.git
cd python-organizador-arquivos

# 1) veja primeiro o que vai acontecer
python organizador.py "C:\Users\SeuUsuario\Downloads" --simular

# 2) se estiver certo, organize de verdade
python organizador.py "C:\Users\SeuUsuario\Downloads"
```

## Rodar os testes

```bash
python -m unittest discover tests
```

## Conceitos usados

- `pathlib` e `shutil` para mexer em arquivos
- `argparse` para criar o comando de terminal
- Dicionários e conjuntos para as categorias
- Testes com `unittest` e pastas temporárias

## Autor

Thyago Ferreira - [@thyagodev021](https://github.com/thyagodev021)

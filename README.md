# TP1: Composição Musical Algorítmica

**Aluno:** Eduardo Correia<br>
**Disciplina:** IA Generativa para Música - DCC/UFMG<br>
**Método Escolhido:** Gramáticas Generativas Não-Determinísticas<br>
**Restrição Estilística/Temática:** Estrutura de música Pop/Hip Hop<br>

---

## Descrição dos entregáveis do repositório
- **`main.py`**: Código-fonte responsável por gerar as peças musicais de ponta a ponta a partir da gramática.
- **`requirements.txt`**: Lista de dependências exatas para reprodução do ambiente.
- **`Relatorio_TP1_EduardoCorreia.pdf`**: Relatório científico em formato ISMIR.
- **`musica1_lofi_hop/`**: Pasta com música (MP3 e MID) gerada com baixa densidade de chimbais ($D_h = 0.2$).
- **`musica2_boom_bap/**: Pasta com música (MP3 e MID) gerada com densidade de chimbais intermediária ($D_h = 0.6$).
- **`musica3_trap_style/`**: Pasta com música (MP3 e MID) gerada com alta densidade de chimbais ($D_h = 1.0$).
- **Arquivos `.png`**: Representações visuais (*Piano Roll*) das execuções.

---

## Instruções

1. Clone o repositório e acesse a pasta:
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o script
```bash
python main.py
```

Obs: Alguns computadores usam `python3` ao inves de `python` no terminal.

### Declaração de uso de IA

Foi usada ferramentas de IA nos seguintes pontos do trabalho:

- [Uso do Gemini para explicar como implementar os instrumentos de Hip Hop em específico](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221s3v4e9nTz2odpZSBxaUK8KZTB6N6UG53%22%5D,%22action%22:%22open%22,%22userId%22:%22116616997490077501144%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
- [Uso do Gemini para resolver problemas do template do relatório e revisão do texto](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221TC2G_rtTYnqFiAXelKsJNA1rEqyh7ED5%22%5D,%22action%22:%22open%22,%22userId%22:%22116616997490077501144%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)


### Observação final
Foram feitas mudanças muito pontuais no template ISMIR, apenas para consistência de linguagem e formatação.

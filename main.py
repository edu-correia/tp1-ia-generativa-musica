import random
import pretty_midi
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def gramatica_hip_hop(hihat_density):
    """Retorna a gramática com base no hiperparametro"""
    return {
        'MUSICA': {
            'expansions': [
                ['INTRO', 'CHORUS', 'VERSE', 'CHORUS', 'OUTRO'],
                ['INTRO', 'VERSE', 'CHORUS', 'CHORUS', 'OUTRO']
            ],
            'weights': [0.6, 0.4]
        },
        'INTRO':  {'expansions': [['BAR_Am', 'BAR_F']], 'weights': [1.0]},
        'OUTRO':  {'expansions': [['BAR_Am', 'CRASH_ON', 'TS', 'TS', 'TS', 'TS']], 'weights': [1.0]},
        'VERSE':  {'expansions': [['BAR_Am', 'BAR_Am', 'BAR_F', 'BAR_G']], 'weights': [1.0]},
        'CHORUS': {'expansions': [['BAR_Am', 'BAR_F', 'BAR_C', 'BAR_G']], 'weights': [1.0]},

        'BAR_Am': {'expansions': [['BEAT_KICK_A', 'BEAT_SNARE', 'BEAT_KICK_A_SYNC', 'BEAT_SNARE']], 'weights': [1.0]},
        'BAR_F':  {'expansions': [['BEAT_KICK_F', 'BEAT_SNARE', 'BEAT_KICK_F_SYNC', 'BEAT_SNARE_FILL']], 'weights': [1.0]},
        'BAR_C':  {'expansions': [['BEAT_KICK_C', 'BEAT_SNARE', 'BEAT_KICK_C_SYNC', 'BEAT_SNARE']], 'weights': [1.0]},
        'BAR_G':  {'expansions': [['BEAT_KICK_G', 'BEAT_SNARE', 'BEAT_KICK_G_SYNC', 'BEAT_SNARE_FILL']], 'weights': [1.0]},

        'BEAT_KICK_A':      {'expansions': [['K_ON', 'B_A2_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_A_SYNC': {'expansions': [['H_STEP', 'B_A2_ON', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_F':      {'expansions': [['K_ON', 'B_F2_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_F_SYNC': {'expansions': [['H_STEP', 'B_F2_ON', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_C':      {'expansions': [['K_ON', 'B_C3_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_C_SYNC': {'expansions': [['H_STEP', 'B_C3_ON', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_G':      {'expansions': [['K_ON', 'B_G2_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_KICK_G_SYNC': {'expansions': [['H_STEP', 'B_G2_ON', 'TS', 'K_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'K_ON', 'H_STEP', 'TS']], 'weights': [1.0]},

        'BEAT_SNARE':       {'expansions': [['S_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'H_STEP', 'TS', 'H_STEP', 'TS']], 'weights': [1.0]},
        'BEAT_SNARE_FILL':  {
            'expansions': [
                ['S_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'S_ON', 'H_STEP', 'TS', 'S_ON', 'H_STEP', 'TS'],
                ['S_ON', 'H_STEP', 'TS', 'H_STEP', 'TS', 'H_STEP', 'TS', 'H_STEP', 'TS']
            ],
            'weights': [0.4, 0.6]
        },

        # HIPERPARÂMETRO: Densidade de Chimbal (Hi-hat)
        'H_STEP': {
            'expansions': [['H_ON'], ['']],
            'weights': [hihat_density, 1.0 - hihat_density]
        }
    }


def expandir_gramatica(simbolo, gramatica):
    """Expande recursivamente os simbolos"""
    if simbolo not in gramatica: return [simbolo]
    
    regra_escolhida = random.choices(
        population=gramatica[simbolo]['expansions'], 
        weights=gramatica[simbolo]['weights'], k=1)[0]
    
    resultado = []
    for s in regra_escolhida:
        if s != '': resultado.extend(expandir_gramatica(s, gramatica))
    return resultado


def tokens_para_midi(tokens, nome_arquivo, bpm=90):
    """Processa os tokens unidimensionais em um arquivo MIDI"""
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)

    # Instrumentos
    bateria = pretty_midi.Instrument(program=25, is_drum=True, name="808 Drums")
    baixo_synth = pretty_midi.Instrument(program=38, name="Sub Bass")
    pad_eletronico = pretty_midi.Instrument(program=90, name="Polysynth Layer")

    # Reverb
    pad_eletronico.control_changes.append(pretty_midi.ControlChange(91, 127, 0.0))
    bateria.control_changes.append(pretty_midi.ControlChange(91, 40, 0.0))

    tempo_atual = 0.0
    duracao_ts = (60.0 / bpm) / 4.0

    DICC_NOTAS = {
        'K_ON': 36, 'S_ON': 38, 'H_ON': 42, 'CRASH_ON': 49,
        'B_A2_ON': 45, 'B_F2_ON': 41, 'B_C3_ON': 48, 'B_G2_ON': 43
    }

    for token in tokens:
        if token == 'TS':
            tempo_atual += duracao_ts
        elif token in DICC_NOTAS:
            pitch = DICC_NOTAS[token]

            if token.startswith('B_'):
                # Layering
                nota_grave = pretty_midi.Note(velocity=115, pitch=pitch - 12, start=tempo_atual, end=tempo_atual + (duracao_ts * 2))
                baixo_synth.notes.append(nota_grave)

                nota_metalica = pretty_midi.Note(velocity=75, pitch=pitch + 12, start=tempo_atual, end=tempo_atual + (duracao_ts * 2))
                pad_eletronico.notes.append(nota_metalica)
            else:
                # Percussao
                vel = 120 if token == 'K_ON' else (100 if token == 'S_ON' else random.randint(70, 90))
                nota = pretty_midi.Note(velocity=vel, pitch=pitch, start=tempo_atual, end=tempo_atual + 0.1)
                bateria.notes.append(nota)

    midi.instruments.extend([bateria, baixo_synth, pad_eletronico])
    midi.write(nome_arquivo)
    return midi


def salvar_piano_roll(midi_data, titulo, nome_imagem):
    """Gera e salva o gráfico do piano roll em png"""
    plt.figure(figsize=(12, 4))
    cores = ['red', 'darkblue', 'cyan']
    nomes = ['Bateria 808', 'Sub Grave', 'Synth c/ Reverb']

    for idx, inst in enumerate(midi_data.instruments):
        for note in inst.notes:
            plt.plot([note.start, note.end], [note.pitch, note.pitch], color=cores[idx], linewidth=3)

    plt.title(titulo)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Pitch (MIDI Note)")
    plt.grid(True, alpha=0.3)

    custom_lines = [Line2D([0], [0], color=cores[i], lw=4) for i in range(3)]
    plt.legend(custom_lines, nomes, loc='upper right')
    
    plt.tight_layout()
    plt.savefig(nome_imagem)
    plt.close()


if __name__ == "__main__":
    print("Iniciando...\n")

    configuracoes = [
        {"nome": "musica1_lofi_hop", "hihat_density": 0.2, "desc": "Lo-Fi (Chimbal Esparso - 20%)"},
        {"nome": "musica2_boom_bap", "hihat_density": 0.6, "desc": "Classico/BoomBap (Chimbal Regular - 60%)"},
        {"nome": "musica3_trap_style", "hihat_density": 1.0, "desc": "Trap (Chimbal Frenetico - 100%)"}
    ]

    for config in configuracoes:
        densidade = config["hihat_density"]
        nome_base = config["nome"]
        
        print(f"Gerando {nome_base}.mid | {config['desc']}")

        # Expandir gramatica
        gramatica = gramatica_hip_hop(hihat_density=densidade)
        tokens_gerados = expandir_gramatica('MUSICA', gramatica)

        # Sintetizar MIDI
        arquivo_midi = f"{nome_base}.mid"
        midi_obj = tokens_para_midi(tokens_gerados, arquivo_midi)

        # gerar imagem do Piano roll
        arquivo_img = f"{nome_base}.png"
        salvar_piano_roll(midi_obj, titulo=f"Piano Roll: {config['desc']}", nome_imagem=arquivo_img)

    print("\nGeração concluída com sucesso!")
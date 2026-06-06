"""
=============================================================================
Análise de Resfriamento — Cold Plate Aviônico 3U VPX
Dados CHT extraídos do Ansys Fluent
Autor: Engenheiro de Dados / Python Developer Sênior
=============================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D

# =============================================================================
# 1. ESTRUTURAÇÃO DOS DADOS (Ansys Fluent — CHT Simulation)
# =============================================================================
data = {
    'Vazao_Massica_kgs': [0.01, 0.03, 0.05],
    'Temp_FPGA_K':        [311.90784, 304.28266, 302.16741],
    'Temp_Fluido_K':      [298.10,    294.60,    294.00],
}
df = pd.DataFrame(data)

print("=" * 55)
print("   DADOS DE SIMULAÇÃO — COLD PLATE 3U VPX (CHT)")
print("=" * 55)
print(df.to_string(index=False))
print("=" * 55)

# =============================================================================
# 2. CONFIGURAÇÃO DE ESTILO PROFISSIONAL
# =============================================================================
plt.style.use('seaborn-v0_8-whitegrid')

# Paleta de cores controlada
COR_FPGA    = '#C0392B'   # Vermelho escuro — componente térmico crítico
COR_FLUIDO  = '#1A6FA8'   # Azul técnico — coolant
COR_TITULO  = '#1C2833'
COR_LIMITE  = '#E67E22'   # Laranja — linha de referência de alerta
COR_TEXTO   = '#2C3E50'

# =============================================================================
# 3. CRIAÇÃO DA FIGURA E EIXO PRINCIPAL
# =============================================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('#FDFEFE')

# =============================================================================
# 4. PLOTAGEM DAS CURVAS
# =============================================================================

# --- Curva 1: Temperatura Média do FPGA ---
ax.plot(
    df['Vazao_Massica_kgs'], df['Temp_FPGA_K'],
    color=COR_FPGA,
    linewidth=2.4,
    linestyle='-',
    marker='o',
    markersize=10,
    markeredgewidth=1.6,
    markeredgecolor='#922B21',
    markerfacecolor='#E74C3C',
    label='Temperatura Média — FPGA',
    zorder=5,
)

# --- Curva 2: Temperatura de Saída do Fluido ---
ax.plot(
    df['Vazao_Massica_kgs'], df['Temp_Fluido_K'],
    color=COR_FLUIDO,
    linewidth=2.4,
    linestyle='-',
    marker='s',
    markersize=10,
    markeredgewidth=1.6,
    markeredgecolor='#154360',
    markerfacecolor='#2E86C1',
    label='Temperatura de Saída — Coolant',
    zorder=5,
)

# =============================================================================
# 5. ANOTAÇÃO ESTRATÉGICA — Ponto Ótimo em 0.03 kg/s
# =============================================================================
ponto_x = df.loc[1, 'Vazao_Massica_kgs']   # 0.03 kg/s
ponto_y = df.loc[1, 'Temp_FPGA_K']          # 304.28 K

ax.annotate(
    'Ponto Otimo Estimado\n   m = 0.03 kg/s\n   (Retornos Decrescentes)',
    xy=(ponto_x, ponto_y),
    xytext=(0.033, 308.6),
    fontsize=10.5,
    color=COR_TITULO,
    fontweight='bold',
    fontstyle='normal',
    arrowprops=dict(
        arrowstyle='-|>',
        color='#2C3E50',
        lw=1.8,
        connectionstyle='arc3,rad=-0.25',
        mutation_scale=14,
    ),
    bbox=dict(
        boxstyle='round,pad=0.55',
        facecolor='#FEFEFE',
        edgecolor='#AEB6BF',
        linewidth=1.2,
        alpha=0.95,
    ),
    zorder=10,
)

# Destaque visual no ponto ótimo (halo)
ax.scatter(
    [ponto_x], [ponto_y],
    s=180, color='none',
    edgecolors='#C0392B', linewidths=2.0,
    zorder=6,
)

# =============================================================================
# 6. LINHA DE REFERÊNCIA — Limite Máximo de Operação do FPGA
# =============================================================================
T_LIMITE = 313.15   # 40°C (temperatura ambiente típica de operação aviônica)
ax.axhline(
    y=T_LIMITE,
    color=COR_LIMITE,
    linewidth=1.2,
    linestyle=(0, (6, 3)),   # traço-ponto
    alpha=0.75,
    label=f'Limite Operacional FPGA  ({T_LIMITE:.2f} K / 40 °C)',
    zorder=3,
)

# =============================================================================
# 7. FORMATAÇÃO DOS EIXOS
# =============================================================================
ax.set_xlabel(
    'Vazão Mássica do Coolant  ṁ  (kg/s)',
    fontsize=13,
    fontweight='bold',
    labelpad=14,
    color=COR_TEXTO,
)
ax.set_ylabel(
    'Temperatura  T  (K)',
    fontsize=13,
    fontweight='bold',
    labelpad=14,
    color=COR_TEXTO,
)
ax.set_title(
    'Análise de Resfriamento — Cold Plate Aviônico 3U VPX\n'
    'Temperatura vs. Vazão Mássica do Coolant  |  CFD · Ansys Fluent (CHT)',
    fontsize=14,
    fontweight='bold',
    color=COR_TITULO,
    pad=18,
    loc='center',
)

# Limites e ticks
ax.set_xlim(0.004, 0.062)
ax.set_ylim(291.5, 315.0)

ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.tick_params(axis='both', labelsize=11, colors=COR_TEXTO, length=4)

# Eixo X secundário em unidades g/s para leitura rápida
ax2 = ax.secondary_xaxis('top',
    functions=(lambda x: x * 1000, lambda x: x / 1000))
ax2.set_xlabel('Vazão Mássica  ṁ  (g/s)', fontsize=10.5,
               labelpad=10, color='#717D7E')
ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
ax2.tick_params(labelsize=10, colors='#717D7E')

# =============================================================================
# 8. LEGENDA
# =============================================================================
ax.legend(
    fontsize=11,
    loc='upper right',
    framealpha=0.97,
    edgecolor='#CCD1D1',
    fancybox=True,
    shadow=False,
    handlelength=2.2,
    labelspacing=0.6,
)

# =============================================================================
# 9. GRADE E ACABAMENTOS VISUAIS
# =============================================================================
ax.grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.65, color='#CCD1D1')
ax.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)
ax.minorticks_on()

# Bordas do gráfico
for spine in ax.spines.values():
    spine.set_edgecolor('#AEB6BF')
    spine.set_linewidth(0.9)

# Anotações dos valores nos pontos de dados
for i, row in df.iterrows():
    offset_y_fpga   = 0.55 if i != 1 else -1.2
    offset_y_fluido = 0.55

    ax.text(
        row['Vazao_Massica_kgs'], row['Temp_FPGA_K'] + offset_y_fpga,
        f"{row['Temp_FPGA_K']:.2f} K",
        ha='center', va='bottom',
        fontsize=8.5, color='#922B21',
        fontweight='semibold',
    )
    ax.text(
        row['Vazao_Massica_kgs'], row['Temp_Fluido_K'] + offset_y_fluido,
        f"{row['Temp_Fluido_K']:.2f} K",
        ha='center', va='bottom',
        fontsize=8.5, color='#1A5276',
        fontweight='semibold',
    )

# Rodapé com assinatura técnica
fig.text(
    0.5, -0.02,
    'Simulação CHT (Conjugate Heat Transfer)  ·  Ansys Fluent  '
    '·  Standard 3U VPX (VITA 46.0)',
    ha='center', va='bottom',
    fontsize=8.5, color='#AAB7B8',
    fontstyle='italic',
)

# =============================================================================
# 10. LAYOUT FINAL E EXPORTAÇÃO
# =============================================================================
plt.tight_layout(pad=1.8)

output_path = '/mnt/user-data/outputs/curva_resfriamento_3uvpx.png'
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches='tight',
    facecolor='white',
    edgecolor='none',
)

print(f"\n✅ Gráfico exportado com sucesso em 300 DPI:")
print(f"   → {output_path}")
plt.show()

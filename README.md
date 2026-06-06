# 🧊 Cold Plate Térmico — Aviônicos 3U VPX
### Análise CHT (Conjugate Heat Transfer) com Ansys Fluent

<div align="center">

![Ansys Fluent](https://img.shields.io/badge/Ansys_Fluent-2026_R1-FFB71B?style=for-the-badge&logo=ansys&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)
</div>

---

## Sobre o Projeto

<table>
<tr>
<td width="55%">

Este repositório documenta a **otimização termofluidodinâmica** de um *cold plate* no padrão **3U VPX**, desenvolvida como parte da formação em Engenharia Aeroespacial na Universidade de Brasília.

O objetivo central foi encontrar o **ponto de equilíbrio ideal** entre eficiência de resfriamento de um FPGA de alta potência e o esforço de bombeamento do fluido — uma troca fundamental em sistemas embarcados aeroespaciais, onde cada watt da bomba compete com a missão.

> *"Com o aumento da densidade de potência nos sistemas embarcados, a dissipação de calor deixou de ser um detalhe de projeto para se tornar o próprio* gating factor *do desenvolvimento."*

</td>
<td width="45%" align="center">

<!-- 🖼️ VISUAL 1 — GRADIENTE TÉRMICO (visão geral)
     Screenshot do Ansys mostrando a placa completa com o mapa de temperatura.
     Dá a primeira impressão visual e técnica do projeto.
     → Salve em: assets/thermal_overview.png -->
<img src="Media/Plate/temp placa 0.01.png" width="100%" alt="Visão geral do gradiente térmico da placa"/>
<sub><i>Distribuição de temperatura no cold plate simulado no Ansys Fluent</i></sub>

</td>
</tr>
</table>

---

## Metodologia

<table>
<tr>
<td width="50%">

| Etapa | Ferramenta | Detalhes |
|---|---|---|
| Modelagem | Ansys | Cold plate com microcanais internos |
| Solver CFD | Ansys Fluent 2026 R1 | CHT — Conjugate Heat Transfer |
| Turbulência | k-ω SST | Escoamentos em canais confinados |
| Pós-processamento | Python | Curvas e análise de convergência |

Foram testadas **três vazões mássicas** para mapear o comportamento do sistema:

```
ṁ₁ = 0.01 kg/s  →  baixo bombeamento
ṁ₂ = 0.03 kg/s  →  ponto ótimo ✅
ṁ₃ = 0.05 kg/s  →  retornos decrescentes
```

</td>
<td width="50%" align="center">

<!-- 🖼️ VISUAL 2 — CONTORNO TÉRMICO NA FACE INFERIOR (Figura 2 do relatório)
     Screenshot do Ansys Fluent com o mapa de calor na face de contato com o FPGA.
     Mostra claramente a zona de concentração térmica — é o visual mais impactante.
     → Salve em: assets/thermal_contour.png -->
<img src="Media/Plate/temp placa 0.05 baixo.png" width="100%" alt="Gradiente térmico na face de contato com o FPGA"/>
<sub><i>Zona de concentração de calor na base de contato direto com o FPGA</i></sub>

</td>
</tr>
</table>

---

## Resultados

### Temperaturas de Equilíbrio

<table>
<tr>
<td width="45%">

| Vazão (kg/s) | FPGA (K) | Fluido Saída (K) |
|:---:|:---:|:---:|
| 0.01 | 311.91 | 298.10 |
| **0.03** | **304.28** | **294.60** |
| 0.05 | 302.17 | 294.00 |

> **Limite do FPGA:** 313.15 K (40 °C)

Ao dobrar a vazão de **0.01 → 0.03 kg/s**, a temperatura do FPGA cai **7.63 K**. Já de **0.03 → 0.05 kg/s**, a queda é de apenas **2.11 K** — um ganho marginal que não justifica o consumo extra da bomba.

</td>
<td width="55%" align="center">

<!-- 🖼️ VISUAL 3 — CURVA DE RESFRIAMENTO (Figura 1 do relatório)
     O gráfico Python de Temperatura × Vazão Mássica com as duas séries
     (FPGA e saída do fluido) e a marcação do ponto ótimo.
     É o visual mais importante do projeto — mostra o "joelho" da curva.
     → Salve em: assets/cooling_curve.png  (exporte em 300 dpi) -->
<img src="Media/Graphics/curva_resfriamento_3uvpx.png" width="100%" alt="Curva de resfriamento — Temperatura vs. Vazão Mássica"/>
<sub><i>Curva de resfriamento: o achatamento após 0.03 kg/s define o ponto ótimo de operação</i></sub>

</td>
</tr>
</table>

---

### Convergência do Solver

<table>
<tr>
<td width="55%" align="center">

<!-- 🖼️ VISUAL 4 — MONITOR DE CONVERGÊNCIA (Figura 3 do relatório)
     Screenshot do monitor do Ansys Fluent mostrando a estabilização da
     temperatura de saída da água ao longo das iterações (ṁ = 0.03 kg/s).
     → Salve em: assets/convergence_monitor.png -->
<img src="Media/Data/temp saida agua 0.03.png" width="100%" alt="Monitor de convergência do Ansys Fluent"/>
<sub><i>Estabilização da temperatura de saída para ṁ = 0.03 kg/s</i></sub>

</td>
<td width="45%">

**Sobre a convergência:**

O solver estabilizou a temperatura de saída do fluido em torno de **294.60 K** após aproximadamente 200 iterações para a vazão ótima.

A curva suave de estabilização confirma que o modelo k-ω SST capturou adequadamente o regime de escoamento turbulento nos microcanais, sem oscilações numéricas significativas.

</td>
</tr>
</table>

---

## Conclusão

A análise comprovou que **0.03 kg/s é a vazão ideal** para este cold plate: entrega resfriamento eficaz ao FPGA — bem abaixo do limite operacional de 313.15 K — sem sobrecarregar a hidrodinâmica da aeronave.

Aumentar para 0.05 kg/s proporciona apenas ~2 K de alívio adicional, o que **não justifica o custo energético extra da bomba** em um sistema embarcado onde cada recurso é crítico.

---

## Stack Técnica

- **Ansys Fluent 2026 R1** — CFD solver e CHT
- **Python 3.11 + Matplotlib / NumPy** — pós-processamento e visualização
---

<div align="center">
<sub>Desenvolvido como projeto acadêmico de termodinâmica computacional aplicada à engenharia aeroespacial.</sub>
</div>

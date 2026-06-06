# 🧊 Cold Plate Térmico — Aviônicos 3U VPX
### Análise CHT (Conjugate Heat Transfer) com Ansys Fluent

<div align="center">

![Ansys Fluent](https://img.shields.io/badge/Ansys_Fluent-2026_R1-FFB71B?style=for-the-badge&logo=ansys&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)
![UnB](https://img.shields.io/badge/UnB-Eng._Aeroespacial-003DA5?style=for-the-badge)

</div>

---

## 📖 Sobre o Projeto

<table>
<tr>
<td width="55%">

Este repositório documenta a **otimização termofluidodinâmica** de um *cold plate* no padrão **3U VPX**, desenvolvida como parte da formação em Engenharia Aeroespacial na Universidade de Brasília.

O objetivo central foi encontrar o **ponto de equilíbrio ideal** entre eficiência de resfriamento de um FPGA de alta potência e o esforço de bombeamento do fluido — uma troca fundamental em sistemas embarcados aeroespaciais, onde cada watt da bomba compete com a missão.

> *"Com o aumento da densidade de potência nos sistemas embarcados, a dissipação de calor deixou de ser um detalhe de projeto para se tornar o próprio* gating factor *do desenvolvimento."*

</td>
<td width="45%" align="center">

<!-- 🖼️ IMAGEM — FLUIDO (visão geral)
     Contorno de velocidade ou pressão do fluido nos microcanais — visão isométrica.
     Dá a primeira impressão visual e técnica do projeto.
     → Salve em: assets/fluid_overview.png -->
<img src="assets/fluid_overview.png" width="100%" alt="Visão geral do escoamento nos microcanais"/>
<sub><i>Escoamento do fluido refrigerante nos microcanais internos</i></sub>

</td>
</tr>
</table>

---

## ⚙️ Metodologia

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

<!-- 🖼️ IMAGEM — FLUIDO (detalhe dos canais)
     Contorno de temperatura ou velocidade do fluido em corte transversal,
     mostrando como o fluido percorre os microcanais.
     → Salve em: assets/fluid_channels.png -->
<img src="assets/fluid_channels.png" width="100%" alt="Detalhe do escoamento nos microcanais"/>
<sub><i>Distribuição do fluido nos microcanais — corte transversal</i></sub>

</td>
</tr>
</table>

---

## 🎬 Escoamento em Movimento

<!-- 🎬 VÍDEO 1 — ANIMAÇÃO DO FLUIDO (visão geral)
     Animação do Ansys mostrando a evolução do escoamento ao longo das iterações
     ou um path-line animado do fluido percorrendo os canais.
     GitHub suporta vídeos .mp4 diretamente no README (tamanho máx: 10 MB).
     → Salve em: assets/fluid_flow_overview.mp4 -->
<video src="assets/fluid_flow_overview.mp4" controls width="100%"></video>

<table>
<tr>
<td width="50%" align="center">

<!-- 🎬 VÍDEO 2 — ANIMAÇÃO DO FLUIDO (detalhe / ângulo alternativo)
     Segundo vídeo com outro ângulo ou variável (ex: pressão, temperatura do fluido).
     → Salve em: assets/fluid_flow_detail.mp4 -->
<video src="assets/fluid_flow_detail.mp4" controls width="100%"></video>
<sub><i>Detalhe do escoamento — variável: [pressão / temperatura / velocidade]</i></sub>

</td>
<td width="50%">

**O que os vídeos mostram:**

As animações exibem a **evolução transiente do escoamento** nos microcanais, geradas pelo Ansys Fluent a partir da solução CHT convergida.

É possível observar a formação do **perfil de velocidade** nos canais, o transporte de energia térmica pelo fluido e a homogeneização progressiva da temperatura à medida que o fluido percorre a placa.

</td>
</tr>
</table>

---

## 📊 Resultados

### Temperaturas de Equilíbrio

<table>
<tr>
<td width="45%">

| Vazão (kg/s) | FPGA (K) | Fluido Saída (K) |
|:---:|:---:|:---:|
| 0.01 | 311.91 | 298.10 |
| **0.03** | **304.28** | **294.60** |
| 0.05 | 302.17 | 294.00 |

> 🔴 **Limite do FPGA:** 313.15 K (40 °C)

Ao dobrar a vazão de **0.01 → 0.03 kg/s**, a temperatura do FPGA cai **7.63 K**. Já de **0.03 → 0.05 kg/s**, a queda é de apenas **2.11 K** — um ganho marginal que não justifica o consumo extra da bomba.

</td>
<td width="55%" align="center">

<!-- 🖼️ IMAGEM — CURVA DE RESFRIAMENTO (Figura 1 do relatório)
     Gráfico Python de Temperatura × Vazão Mássica com as duas séries
     (FPGA e saída do fluido) e a marcação do ponto ótimo em 0.03 kg/s.
     É o visual mais importante do projeto — mostra claramente o "joelho" da curva.
     → Salve em: assets/cooling_curve.png  (exporte em 300 dpi para boa legibilidade) -->
<img src="assets/cooling_curve.png" width="100%" alt="Curva de resfriamento — Temperatura vs. Vazão Mássica"/>
<sub><i>O achatamento após 0.03 kg/s define o ponto ótimo de operação</i></sub>

</td>
</tr>
</table>

---

### 📉 Convergência do Solver

<table>
<tr>
<td width="55%" align="center">

<!-- 🖼️ IMAGEM — MONITOR DE CONVERGÊNCIA (Figura 3 do relatório)
     Screenshot do monitor do Ansys Fluent mostrando a estabilização da
     temperatura de saída da água ao longo das ~400 iterações (ṁ = 0.03 kg/s).
     → Salve em: assets/convergence_monitor.png -->
<img src="assets/convergence_monitor.png" width="100%" alt="Monitor de convergência do Ansys Fluent"/>
<sub><i>Estabilização da temperatura de saída para ṁ = 0.03 kg/s</i></sub>

</td>
<td width="45%">

**Sobre a convergência:**

O solver estabilizou a temperatura de saída do fluido em **294.60 K** após aproximadamente 200 iterações para a vazão ótima.

A curva suave confirma que o modelo k-ω SST capturou adequadamente o regime de escoamento turbulento nos microcanais, sem oscilações numéricas significativas.

</td>
</tr>
</table>

---

## 💡 Conclusão

A análise comprovou que **0.03 kg/s é a vazão ideal** para este cold plate: entrega resfriamento eficaz ao FPGA — bem abaixo do limite operacional de 313.15 K — sem sobrecarregar a hidrodinâmica da aeronave.

Aumentar para 0.05 kg/s proporciona apenas ~2 K de alívio adicional, o que **não justifica o custo energético extra da bomba** em um sistema embarcado onde cada recurso é crítico.

---

## 🛠️ Stack Técnica

- **Ansys Fluent 2026 R1** — CFD solver e CHT
- **Python 3.11 + Matplotlib / NumPy** — pós-processamento e visualização

---

<div align="center">
<sub>Desenvolvido como projeto acadêmico de termodinâmica computacional aplicada à engenharia aeroespacial.</sub>
</div>

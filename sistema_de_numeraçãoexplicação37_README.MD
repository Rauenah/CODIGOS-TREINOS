
# 📘 README VISUAL — Sistemas de Numeração  
### *Guia rápido para relembrar sem esforço*

---

## 🎯 VISÃO GERAL

| Sistema | Base | Símbolos | Para que serve |
|--------|------|----------|----------------|
| **Decimal** | 10 | 0–9 | Nosso dia a dia |
| **Binário** | 2 | 0–1 | Computadores |
| **Octal** | 8 | 0–7 | Representação compacta de binário |
| **Hexadecimal** | 16 | 0–9 + A–F | Representação compacta e legível |

---

## 🔢 1. Sistema Decimal (base 10)

### ✔ O que lembrar
- É o sistema que usamos naturalmente.  
- Tem **10 símbolos**: 0 a 9.  
- Cada posição vale uma potência de 10.

### 🧩 Visual
```
  3    4    5
(centena)(dezena)(unidade)
```

```
345 = 3×100 + 4×10 + 5×1
```

---

## ⚡ 2. Sistema Binário (base 2)

### ✔ O que lembrar
- Só usa **0 e 1**.  
- É a “linguagem” do computador.  
- Cada posição vale uma potência de 2.

### 🧩 Visual
```
  1    0    1
(4)  (2)  (1)
```

```
101₂ = 5₁₀
```

---

## 🟦 3. Sistema Octal (base 8)

### ✔ O que lembrar
- Usa **0 a 7**.  
- Cada dígito octal representa **3 bits** em binário.  
- É um jeito mais curto de escrever binário.

### 🧩 Visual
```
Binário:  101 010
Octal:      5   2
```

---

## 🔶 4. Sistema Hexadecimal (base 16)

### ✔ O que lembrar
- Usa **0 a 9** e **A a F**  
  - A=10, B=11, C=12, D=13, E=14, F=15  
- Cada dígito hex representa **4 bits**.  
- Muito usado porque é compacto e fácil de ler.

### 🧩 Visual
```
Binário:  1111 1111
Hex:        F    F
```

```
FF₁₆ = 255₁₀
```

---

## 🔁 5. Conversões rápidas (ideia visual)

### Decimal → Binário/Octal/Hex  
Use Python:
```
bin(n)  → binário
oct(n)  → octal
hex(n)  → hexadecimal
```

### Binário → Octal  
Agrupe em **3 bits**:
```
101 110 → 5 6
```

### Binário → Hexadecimal  
Agrupe em **4 bits**:
```
1101 1110 → D E
```

---

## 🎯 6. O que realmente importa lembrar

- Decimal = base 10  
- Binário = base 2  
- Octal = base 8  
- Hexadecimal = base 16  
- Hex usa A–F porque precisa representar valores acima de 9  
- Binário é a base de tudo  
- Hex é binário “abreviado”  




# 📌 Estruturas Aninhadas em Python

**Estrutura aninhada** é quando colocamos uma estrutura **dentro de outra**.  
É como ter uma **caixa dentro de outra caixa**.

Em Python, isso acontece quando usamos, por exemplo:

- listas dentro de listas  
- dicionários dentro de dicionários  
- `if` dentro de `if`  
- loops dentro de loops  

Ou seja: **uma estrutura que vive dentro de outra**.

---

# 🧩 Exemplos Simples

## ✔️ Lista dentro de lista
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
```
Aqui cada linha é uma lista, e todas juntas formam uma lista maior.

---

## ✔️ Dicionário dentro de dicionário
```python
pessoa = {
    "nome": "Ana",
    "endereco": {
        "rua": "Rua A",
        "numero": 123
    }
}
```
O campo **endereco** é outro dicionário dentro do dicionário principal.

---

# 🛠️ Onde isso é usado?

- Para representar **tabelas**, **matrizes**, **grades** (como em jogos e planilhas)  
- Para organizar dados mais complexos, como **JSON** de APIs  
- Para percorrer estruturas em camadas usando **loops dentro de loops**  
- Para tomar decisões mais detalhadas com **ifs aninhados**


#Desafios 36 a 45
# Notação de números

## Objetivo 
Um projeto pequeno para testar conversão de números em formato mais legível 
Ex: 1000000000 = 1.0bi ou 1.0b

## Como usar?
A função de conversão se chama ```transformNum``` e possui **3** parâmetros:
### **1# - Passe um número ou string em formato numérico**
(```"100000"```) ✅ <br> 
(```"100.000"```) ❌

### **2# - Precisão do número**

Ex: <br>
```transformNum(1234567, 0)``` ➡️ 1mi <br>
```transformNum(1234567, 1)``` ➡️ 1.2mi (Padrão) <br>
```transformNum(1234567, 2)``` ➡️ 1.23mi <br>

### **3# - Sufixo extenso (padrão) ou curto**

**Extenso:** <br>
```transformNum(1234567, 2)``` ➡️ 123.45mi <br>
```transformNum(1234567, 2, False)``` ➡️ 123.45mi <br>

**Curto:** <br>
```transformNum(1234567, 2, True)``` ➡️ 123.45m <br>

## Outros arquivos
- [Atualizações do projeto](/markdown/CHANGELOG.md) <br>
- [Problemas/desconfortos conhecidos](/markdown/BUGS.md) <br>
- [Ideias/Objetivos futuros](/markdown/ROADMAP.md) <br>

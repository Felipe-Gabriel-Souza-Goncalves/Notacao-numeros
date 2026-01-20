# Notação de números

## Objetivo 
Um projeto pequeno para testar conversão de números em formato mais legível 
Ex: 1000000000 = 1.0bi ou 1.0b

## Como usar?
A função de conversão se chama ```transformNum``` e possui **3** parâmetros:
### **1# - Passe SOMENTE número ou string do número**
```transformNum(100000)``` ✅ (Desejável) <br> 
```transformNum(-100000)``` ✅ <br>
```transformNum(100.000)``` ✅ <br>
```transformNum("100.000")``` ✅ <br>

```transformNum("meu número é 1000")``` ❌ <br>
```transformNum("onze mil")``` ❌ <br>
  
### **2# - Precisão do número**

Ex: <br>
```transformNum(2345678, 0)``` ➡️ 2 milhões <br>
```transformNum(2345678, 1)``` ➡️ 2.3 milhões (Padrão) <br>
```transformNum(2345678, 2)``` ➡️ 2.34 milhões <br>

_Caso a precisão seja maior que o número, o restante dos números serão 0_

### **3# - Sufixo extenso  ou curto**

**Extenso:** (padrão) <br> 
```transformNum(2345678, 1)``` ➡️ 2.3 milhões <br>
```transformNum(2345678, 1, False)``` ➡️ 2.3 milhões <br>

**Curto:** <br>
```transformNum(2345678, 1, True)``` ➡️ 2.3mi <br>

## Outros arquivos
- [Atualizações do projeto](/markdown/CHANGELOG.md) <br>
- [Problemas/desconfortos conhecidos](/markdown/BUGS.md) <br>
- [Ideias/Objetivos futuros](/markdown/ROADMAP.md) <br>

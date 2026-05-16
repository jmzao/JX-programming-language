# JX IDE - Linux Edition

## 🚀 IDE Completa para Linguagem JX

IDE nativa para Linux (ARM64 e x86_64) com suporte completo à linguagem JX v0.1.

### ✨ Funcionalidades

- **📝 Editor de código** integrado
- **🖥️ Interpretador JX** embutido
- **📁 Gerenciador de arquivos** .jx
- **💾 Exportação** para Downloads
- **🎨 Interface colorida** com ANSI
- **📚 Documentação** integrada

### 🆕 Novos Comandos

- `back.line(n)` - Volta para linha `n` descartando estados
- `back.linesave(n)` - Volta para linha `n` salvando estados

### 📦 Instalação

```bash
# Extrai o pacote
tar -xzf jx-ide-linux.tar.gz
cd JX_LinuxIDE

# Executa
./jx-ide
```

### 🔧 Requisitos

- Python 3.6+
- Linux (ARM64 ou x86_64)
- Terminal com suporte a cores ANSI

### 📖 Uso

```bash
./jx-ide
# ou
python3 bin/jx_ide.py
```

### 🎯 Comandos da IDE

1. Listar arquivos
2. Abrir arquivo
3. Criar novo arquivo
4. Editar arquivo atual
5. Executar código
6. Exportar arquivo (.jx)
7. Documentação
0. Sair

### 📝 Exemplo de Código JX

```jx
# Hello World
Console.display("Ola, Mundo!")

# Variáveis e concatenação
nome = "Desenvolvedor"
Console.display("Ola, " + nome + "!")

# Renderização avançada
Console.display("Linha 1")
Console.display("Linha 2")
back.line(1)
Console.display(">>> Atualizado!")
```

### 🏗️ Estrutura

```
JX_LinuxIDE/
├── bin/jx_ide.py    # Interpretador principal
├── jx-ide           # Script launcher
└── README.md        # Este arquivo
```

### 🎨 Recursos da Linguagem JX

- Case insensitive
- Comentários com `#`
- Tipos: int, sel(max), boolean, comando
- Operadores: ==, #=, <, >, +, -, *, /
- Estruturas: Loop { }, stop(), Wait.frame()

---
**Desenvolvido para a comunidade JX** 🚀

# 🚀 JX Web IDE

IDE completa para a linguagem JX que roda diretamente no navegador.

## ✨ Recursos

### 🌐 Multiplataforma
- **Linux** (ARM64, x86_64)
- **Android** (navegador comum ou Termux)
- **Windows/macOS**
- **iOS**

### 💾 Gerenciamento de Arquivos
- **Salvar Local**: Armazena arquivos no localStorage do navegador
- **Baixar .jx**: Exporta arquivos para o gerenciador de arquivos do sistema
  - No Android: Salva na pasta Downloads
  - No Linux: Usa o download padrão do navegador
- **Criar/Editar**: Gerencie múltiplos arquivos .jx
- **Auto-save**: Salvamento automático enquanto digita

### 🎯 Funcionalidades
- Editor com syntax highlighting básico
- Console interativo com logs coloridos
- Execução em tempo real (Ctrl+Enter)
- Múltiplos arquivos (abas)
- Documentação integrada
- Responsivo para mobile

## 🆕 Comandos Implementados

### back.line(n)
Volta para a linha `n`, **descartando todos os estados salvos**.

```jx
Console.display("Linha 1")
Console.display("Linha 2")
back.line(1)  # Volta para linha 1, descarta estados
```

### back.linesave(n)
Volta para a linha `n`, **salvando o estado atual antes**.

```jx
Console.display("Linha 1")
back.linesave(1)  # Salva estado e volta para linha 1
```

### Concatenação de Strings
Agora totalmente funcional:

```jx
var nome = "JX"
var versao = "0.1"
Console.display("Bem-vindo à " + nome + " versão " + versao)
# Saída: Bem-vindo à JX versão 0.1
```

## 🚀 Como Usar

### Opção 1: Abrir Diretamente
Arraste o arquivo `src/index.html` para seu navegador.

### Opção 2: Servidor Local
```bash
cd JX_WebIDE
python3 -m http.server 8080
```
Acesse: `http://localhost:8080/src/index.html`

### Atalhos de Teclado
- **Ctrl+Enter**: Executar código
- **Ctrl+S**: Salvar arquivo

## 📁 Estrutura

```
JX_WebIDE/
├── src/
│   └── index.html      # IDE completa (único arquivo)
├── examples/           # Exemplos de código
├── docs/               # Documentação adicional
├── themes/             # Temas futuros
└── README.md           # Este arquivo
```

## 📋 Exemplos Incluídos

1. **hello_world.jx** - Primeiro programa
2. **render_demo.jx** - Demo de back.line/back.linesave
3. **concat_demo.jx** - Demonstração de concatenação

## 🔧 Compatibilidade

| Sistema | Navegador | Status |
|---------|-----------|--------|
| Linux ARM64 | Firefox/Chrome | ✅ |
| Android | Chrome/Firefox | ✅ |
| Windows | Edge/Chrome | ✅ |
| macOS | Safari/Chrome | ✅ |
| iOS | Safari | ✅ |

## 📝 Notas

- Os arquivos são salvos no **localStorage** do navegador
- Use **Baixar .jx** para exportar para o gerenciador de arquivos
- Funciona offline após carregamento inicial

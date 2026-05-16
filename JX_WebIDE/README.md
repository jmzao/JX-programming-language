# 🚀 JX Web IDE v0.1

Uma IDE completa para a linguagem **JX** que roda diretamente no seu navegador! Sem necessidade de instalação, compatível com Linux ARM64, Android e qualquer dispositivo com navegador moderno.

## ✨ Recursos

- **🌐 100% Web**: Roda em qualquer navegador (Chrome, Firefox, Safari, Edge)
- **📱 Multiplataforma**: Linux ARM64, Android, iOS, Windows, macOS
- **💾 Armazenamento Local**: Seus arquivos são salvos no localStorage do navegador
- **🎨 Interface Moderna**: Tema escuro com cores ANSI
- **📚 Documentação Integrada**: Acesso rápido à documentação da linguagem JX
- **🖥️ Console Interativo**: Execute código e veja os resultados em tempo real
- **📁 Gerenciador de Arquivos**: Crie, edite e organize seus projetos JX
- **🔧 Interpretador Embutido**: Executa código JX diretamente no navegador

## 🆕 Novos Comandos Suportados

### Renderização Avançada

- **`back.line(n)`**: Volta para a linha `n`, **descartando todos os estados salvos**
- **`back.linesave(n)`**: Volta para a linha `n`, **salvando os estados antes de voltar**

Exemplo:
```jx
Console.display("Linha 1")
Console.display("Linha 2")
Console.display("Linha 3")

# Volta para linha 1 descartando estados
back.line(1)
Console.display("Linha 1 atualizada")

# Volta para linha 2 salvando estado
back.linesave(2)
Console.display("Linha 2 com estado salvo")
```

## 🚀 Como Usar

### Opção 1: Abrir Diretamente
Basta abrir o arquivo `src/index.html` no seu navegador:

```bash
# Linux/Mac
xdg-open src/index.html  # Linux
open src/index.html      # Mac

# Ou arraste o arquivo para o navegador
```

### Opção 2: Servidor Web Local
```bash
# Python 3
python3 -m http.server 8080

# Acesse: http://localhost:8080/src/index.html
```

### Opção 3: GitHub Pages / Netlify / Vercel
Faça deploy em qualquer serviço de hospedagem estática!

## 📁 Estrutura do Projeto

```
JX_WebIDE/
├── src/
│   └── index.html          # IDE completa (único arquivo)
├── examples/               # Exemplos de código JX
├── docs/                   # Documentação adicional
├── themes/                 # Temas personalizados (futuro)
└── README.md              # Este arquivo
```

## 💻 Funcionalidades da IDE

### Editor de Código
- Syntax highlighting básico
- Auto-save enquanto digita
- Suporte a múltiplos arquivos (tabs)
- Atalhos: `Ctrl+S` (salvar), `Ctrl+Enter` (executar)

### Gerenciador de Arquivos
- Criar novos arquivos `.jx`
- Navegar entre arquivos
- Exemplos pré-carregados
- Persistência no localStorage

### Console
- Saída colorida (info, warning, error, success)
- Histórico de execução
- Botão para limpar console
- Logs detalhados de execução

### Documentação
- Painel lateral com todos os comandos JX
- Referência rápida de sintaxe
- Exemplos de uso

## 📖 Linguagem JX

A JX é uma linguagem de programação com sintaxe própria, case insensitive, projetada para ser simples e poderosa.

### Tipos de Dados
- `int` - números inteiros
- `sel(max)` - números limitados
- `boolean` - verdadeiro/falso
- `comando` - armazena comandos

### Comandos Principais

#### Saída
- `Console.display()` - mostra no console

#### Entrada
- `Console.input()` - recebe entrada
- `input.detect()` - detecta teclas (w, a, s, d, enter, space, escape)

#### Loop
- `Loop {}` - estrutura de loop
- `stop()` - para o loop
- `Wait()` - espera tempo
- `Wait.frame()` - espera frames

#### Renderização
- `Console.back.backspace` - volta um caractere
- `Console.back.enter` - volta uma linha
- `back.line(n)` - volta para linha n (descarta estados)
- `back.linesave(n)` - volta para linha n (salva estados)

#### Transformação
- `transform.int()` - converte para inteiro
- `Replace(var) to "valor"` - substitui valor

#### Operadores
- `==` (igual), `#=` (diferente)
- `<`, `>` (menor/maior)
- `+`, `-`, `*`, `/` (matemáticos)

## 🎯 Exemplos Incluídos

1. **hello_world.jx** - Primeiro programa em JX
2. **render_demo.jx** - Demonstração dos comandos de renderização
3. **variables_demo.jx** - Uso de variáveis e tipos

## 🔧 Desenvolvimento

A IDE é construída com:
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna com variáveis CSS
- **JavaScript ES6+** - Lógica da IDE e interpretador JX
- **localStorage** - Persistência de dados

### Arquitetura

```javascript
// Classes principais
- JXInterpreter    // Interpretador da linguagem JX
- FileSystem       // Gerenciamento de arquivos (localStorage)
- IDE              // Controlador principal da interface
```

## 🌍 Compatibilidade

Testado e funcionando em:
- ✅ Chrome/Chromium (Linux, Android, Windows)
- ✅ Firefox (todas plataformas)
- ✅ Safari (iOS, macOS)
- ✅ Edge (Windows)
- ✅ Navegadores móveis

### Requisitos Mínimos
- Navegador com suporte a ES6+
- JavaScript habilitado
- localStorage disponível

## 📝 Próximos Recursos

- [ ] Real-time collaboration
- [ ] Exportar projetos como .zip
- [ ] Temas personalizáveis
- [ ] Debugger integrado
- [ ] Autocomplete inteligente
- [ ] Suporte a bibliotecas externas
- [ ] Compilador para WebAssembly

## 🤝 Contribuindo

Sinta-se à vontade para:
1. Reportar bugs
2. Sugerir novas funcionalidades
3. Enviar pull requests
4. Melhorar a documentação

## 📄 Licença

Este projeto é open source e pode ser usado livremente para aprender e desenvolver com a linguagem JX.

---

**Desenvolvido com ❤️ para a comunidade JX**

*Versão: 0.1 | Última atualização: 2024*

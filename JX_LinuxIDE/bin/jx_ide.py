#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JX IDE - Linux ARM64/x86_64"""

import os
from pathlib import Path

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

class JXInterpreter:
    def __init__(self):
        self.variables = {}
        self.console_history = []
        self.line_states = {}
        self.current_line = 0
        
    def log(self, message, color=Colors.WHITE):
        print(f"{color}{message}{Colors.RESET}")
        self.console_history.append(message)
        
    def back_line(self, line_num):
        if line_num in self.line_states:
            del self.line_states[line_num]
        self.current_line = line_num
        print(f"\033[{line_num + 2}G", end="")
        
    def back_line_save(self, line_num):
        self.line_states[self.current_line] = {
            'variables': self.variables.copy(),
            'history': self.console_history.copy()
        }
        self.current_line = line_num
        print(f"\033[{line_num + 2}G", end="")
        
    def evaluate_expression(self, expr):
        """Avalia expressoes incluindo concatenacao de strings"""
        expr = expr.strip()
        
        # Se tem +, faz concatenacao
        if '+' in expr:
            result = ""
            current_part = ""
            in_string = False
            string_char = None
            
            for char in expr:
                if char in '"\'':
                    if not in_string:
                        in_string = True
                        string_char = char
                        current_part += char
                    elif char == string_char:
                        in_string = False
                        current_part += char
                        string_char = None
                    else:
                        current_part += char
                elif char == '+' and not in_string:
                    part = current_part.strip()
                    if part:
                        if len(part) >= 2 and ((part[0] == '"' and part[-1] == '"') or (part[0] == "'" and part[-1] == "'")):
                            result += part[1:-1]
                        elif part in self.variables:
                            result += str(self.variables[part])
                        else:
                            try:
                                result += str(eval(part, {"__builtins__": {}}, self.variables))
                            except:
                                result += part
                    current_part = ""
                else:
                    current_part += char
            
            # Ultima parte
            if current_part:
                part = current_part.strip()
                if len(part) >= 2 and ((part[0] == '"' and part[-1] == '"') or (part[0] == "'" and part[-1] == "'")):
                    result += part[1:-1]
                elif part in self.variables:
                    result += str(self.variables[part])
                else:
                    try:
                        result += str(eval(part, {"__builtins__": {}}, self.variables))
                    except:
                        result += part
            
            return result
        
        # Sem +, trata como literal ou variavel
        if len(expr) >= 2 and ((expr[0] == '"' and expr[-1] == '"') or (expr[0] == "'" and expr[-1] == "'")):
            return expr[1:-1]
        if expr in self.variables:
            return self.variables[expr]
        try:
            return eval(expr, {"__builtins__": {}}, self.variables)
        except:
            return expr
            
    def execute(self, code):
        lines = code.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            if not line or line.startswith('#'):
                i += 1
                continue
                
            try:
                if line.startswith('Console.display('):
                    content = line[16:-1]
                    content = self.evaluate_expression(content)
                    self.log(str(content), Colors.GREEN)
                    
                elif line.startswith('back.line('):
                    line_num = int(line[10:-1])
                    self.back_line(line_num)
                    
                elif line.startswith('back.linesave('):
                    line_num = int(line[14:-1])
                    self.back_line_save(line_num)
                    
                elif '=' in line and '==' not in line and '#=' not in line:
                    parts = line.split('=', 1)
                    var_name = parts[0].strip()
                    value = parts[1].strip()
                    self.variables[var_name] = self.evaluate_expression(value)
                    
                elif line == 'stop()':
                    self.log("Loop stopped", Colors.YELLOW)
                    return
                    
            except Exception as e:
                self.log(f"Error on line {i+1}: {str(e)}", Colors.RED)
                
            i += 1


class FileManager:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
    def list_files(self, ext='.jx'):
        return [f.name for f in self.base_dir.glob(f'*{ext}')]
        
    def read_file(self, filename):
        filepath = self.base_dir / filename
        return filepath.read_text() if filepath.exists() else None
        
    def write_file(self, filename, content):
        (self.base_dir / filename).write_text(content)
        return True


class JXIDE:
    def __init__(self):
        self.home_dir = Path.home() / '.jx_ide'
        self.file_manager = FileManager(self.home_dir / 'projects')
        self.interpreter = JXInterpreter()
        self.current_file = None
        self.current_content = ""
        (self.home_dir / 'examples').mkdir(parents=True, exist_ok=True)
        self.create_examples()
        
    def create_examples(self):
        self.file_manager.write_file('hello_world.jx', '''# Hello World em JX
Console.display("Ola, Mundo!")
nome = "Desenvolvedor"
Console.display("Ola, " + nome + "!")
mensagem = "JX eh " + "incrivel"
Console.display(mensagem)
''')
        self.file_manager.write_file('render_demo.jx', '''# Demo de Renderizacao
Console.display("=== Demo back.line ===")
Console.display("Linha 1")
Console.display("Linha 2")
back.line(1)
Console.display(">>> Atualizado com back.line(1)")
''')
        
    def show_menu(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}╔════════════════════════════════════╗")
        print(f"║      {Colors.WHITE}JX IDE - Linux Edition{Colors.CYAN}        ║")
        print(f"╠════════════════════════════════════╣")
        print(f"║  {Colors.GREEN}1.{Colors.WHITE} Listar arquivos              {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}2.{Colors.WHITE} Abrir arquivo                 {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}3.{Colors.WHITE} Criar novo arquivo            {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}4.{Colors.WHITE} Editar arquivo atual          {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}5.{Colors.WHITE} Executar codigo               {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}6.{Colors.WHITE} Exportar arquivo (.jx)        {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}7.{Colors.WHITE} Documentacao                  {Colors.CYAN}║")
        print(f"║  {Colors.GREEN}0.{Colors.WHITE} Sair                          {Colors.CYAN}║")
        print(f"╚════════════════════════════════════╝{Colors.RESET}\n")
        
    def list_files(self):
        files = self.file_manager.list_files()
        if not files:
            self.interpreter.log("Nenhum arquivo encontrado.", Colors.YELLOW)
            return
        print(f"\n{Colors.BOLD}Arquivos .jx:{Colors.RESET}")
        for i, f in enumerate(files, 1):
            marker = "*" if f == self.current_file else " "
            print(f"  {marker} {i}. {f}")
            
    def open_file(self, filename):
        content = self.file_manager.read_file(filename)
        if content:
            self.current_file = filename
            self.current_content = content
            self.interpreter.log(f"Arquivo '{filename}' aberto.", Colors.GREEN)
            return content
        self.interpreter.log(f"Arquivo '{filename}' nao encontrado.", Colors.RED)
        return None
        
    def create_file(self, filename):
        if not filename.endswith('.jx'):
            filename += '.jx'
        self.file_manager.write_file(filename, '# Novo arquivo JX\n')
        self.open_file(filename)
        
    def edit_file_interactive(self):
        if not self.current_file:
            self.interpreter.log("Nenhum arquivo aberto.", Colors.RED)
            return
        print(f"\n{Colors.CYAN}Editando: {self.current_file}{Colors.RESET}")
        print(f"{Colors.YELLOW}(Digite o codigo. Digite 'EOF' para salvar){Colors.RESET}\n")
        lines = []
        while True:
            try:
                line = input()
                if line == 'EOF':
                    break
                lines.append(line)
            except EOFError:
                break
        self.current_content = '\n'.join(lines)
        self.file_manager.write_file(self.current_file, self.current_content)
        self.interpreter.log("Arquivo salvo!", Colors.GREEN)
        
    def run_code(self):
        if not self.current_content:
            self.interpreter.log("Nenhum codigo para executar.", Colors.RED)
            return
        print(f"\n{Colors.BOLD}{Colors.BLUE}=== Executando {self.current_file or 'codigo'} ==={Colors.RESET}\n")
        self.interpreter.execute(self.current_content)
        print(f"\n{Colors.GREEN}=== Execucao concluida ==={Colors.RESET}\n")
        
    def export_file(self):
        if not self.current_file:
            self.interpreter.log("Nenhum arquivo aberto.", Colors.RED)
            return
        import shutil
        from datetime import datetime
        export_dir = Path.home() / 'Downloads'
        export_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        export_name = f"{self.current_file.replace('.jx', '')}_{timestamp}.jx"
        export_path = export_dir / export_name
        shutil.copy2(self.home_dir / 'projects' / self.current_file, export_path)
        self.interpreter.log(f"Arquivo exportado para: {export_path}", Colors.GREEN)
        
    def show_docs(self):
        print(f"""
{Colors.BOLD}{Colors.CYAN}=== DOCUMENTACAO JX v0.1 ==={Colors.RESET}

{Colors.BOLD}COMANDOS DE RENDERIZACAO:{Colors.RESET}
  * Console.display(texto)  - Mostra texto no console
  * back.line(n)            - Volta para linha n (descarta estados)
  * back.linesave(n)        - Volta para linha n (salva estados)

{Colors.BOLD}VARIAVEIS:{Colors.RESET}
  * Sintaxe: nome = valor
  * Tipos: int, sel(max), boolean, comando

{Colors.BOLD}OPERADORES:{Colors.RESET}
  * == (igual), #= (diferente)
  * <, >, +, -, *, /
  * Concatenacao: "texto" + var + "mais"

{Colors.BOLD}ESTRUTURAS:{Colors.RESET}
  * Loop {{ }} - Laco de repeticao
  * stop() - Para o loop
  * Wait.frame() - Espera 1 frame

{Colors.BOLD}COMENTARIOS:{Colors.RESET}
  * # Este eh um comentario

{Colors.YELLOW}Dica: A linguagem eh case insensitive{Colors.RESET}
""")
        
    def run(self):
        self.interpreter.log("JX IDE iniciada!", Colors.GREEN)
        self.interpreter.log(f"Diretorio de projetos: {self.home_dir / 'projects'}", Colors.CYAN)
        
        while True:
            self.show_menu()
            try:
                choice = input(f"{Colors.BOLD}Escolha uma opcao: {Colors.RESET}").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n")
                break
                
            if choice == '1':
                self.list_files()
            elif choice == '2':
                self.list_files()
                try:
                    idx = int(input("Numero do arquivo: "))
                    files = self.file_manager.list_files()
                    if 1 <= idx <= len(files):
                        self.open_file(files[idx-1])
                except (ValueError, IndexError):
                    self.interpreter.log("Opcao invalida.", Colors.RED)
            elif choice == '3':
                name = input("Nome do arquivo (sem .jx): ").strip()
                self.create_file(name)
            elif choice == '4':
                self.edit_file_interactive()
            elif choice == '5':
                self.run_code()
            elif choice == '6':
                self.export_file()
            elif choice == '7':
                self.show_docs()
            elif choice == '0':
                self.interpreter.log("Ate logo!", Colors.GREEN)
                break
            else:
                self.interpreter.log("Opcao invalida!", Colors.RED)


if __name__ == '__main__':
    ide = JXIDE()
    ide.run()

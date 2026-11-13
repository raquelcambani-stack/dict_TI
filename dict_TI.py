import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QTextBrowser, QListWidget, 
                             QLabel, QPushButton, QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

# Banco de dados inicial com mais de 50 termos de TI
DICIONARIO_TI = {
    "API": "Application Programming Interface. Conjunto de rotinas e padrões estabelecidos por uma aplicação para que outras possam utilizar suas funcionalidades.",
    "Algoritmo": "Sequência finita de instruções lógicas e bem definidas que resolvem um problema ou executam uma tarefa.",
    "Backend": "Parte de um sistema web ou software que roda no servidor, invisível para o usuário final, cuidando de dados e regras de negócio.",
    "Frontend": "A interface gráfica de um sistema com a qual o usuário interage diretamente. Construído com HTML, CSS e JavaScript.",
    "Fullstack": "Profissional ou sistema que domina e atua tanto no desenvolvimento Frontend quanto no Backend.",
    "Database": "Banco de dados. Conjunto estruturado de arquivos ou informações armazenadas eletronicamente em um sistema de computador.",
    "Docker": "Plataforma de código aberto que automatiza a implantação de aplicativos dentro de containers de software de forma isolada.",
    "Kubernetes": "Ferramenta de orquestração de containers de código aberto que automatiza a implantação, o dimensionamento e a gestão de aplicações.",
    "Git": "Sistema de controle de versão distribuído, amplamente utilizado no desenvolvimento de software para rastrear alterações no código.",
    "GitHub": "Plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git.",
    "DevOps": "Cultura e conjunto de práticas que integram o desenvolvimento de software (Dev) e as operações de infraestrutura (Ops).",
    "Agile": "Metodologia ágil de desenvolvimento de software baseada em iterações curtas, colaboração e adaptabilidade.",
    "Scrum": "Framework ágil para gestão de projetos complexos, focado em entregas incrementais chamadas Sprints.",
    "Cloud Computing": "Computação em nuvem. Entrega de serviços de computação (servidores, armazenamento, redes) pela internet.",
    "AWS": "Amazon Web Services. A plataforma de computação em nuvem mais adotada e abrangente do mundo.",
    "Azure": "Plataforma e serviço de computação em nuvem da Microsoft para gerenciamento de aplicativos.",
    "Machine Learning": "Aprendizado de Máquina. Subcampo da IA que permite que sistemas aprendam e melhorem a partir de dados sem programação explícita.",
    "Deep Learning": "Aprendizado Profundo. Ramo do Machine Learning baseado em redes neurais artificiais com muitas camadas (profundas).",
    "Inteligência Artificial": "Campo da ciência da computação dedicado a criar sistemas capazes de realizar tarefas que exigiriam inteligência humana.",
    "Big Data": "Área do conhecimento que estuda como tratar, analisar e obter informações de conjuntos de dados grandes ou complexos demais.",
    "Data Science": "Ciência de Dados. Estudo detalhado de informações e dados, sua origem, o que representam e como podem se transformar em valor.",
    "SQL": "Structured Query Language. Linguagem padrão para gerenciamento e manipulação de bancos de dados relacionais.",
    "NoSQL": "Termo genérico para bancos de dados não relacionais, que armazenam dados em formatos diferentes de tabelas (ex: JSON).",
    "Python": "Linguagem de programação de alto nível, interpretada, com foco em legibilidade de código e multiparadigma.",
    "JavaScript": "Linguagem de programação de alto nível, interpretada, essencial para o desenvolvimento web moderno e dinâmico.",
    "TypeScript": "Superset do JavaScript desenvolvido pela Microsoft que adiciona tipagem estática opcional à linguagem.",
    "Linux": "Núcleo (kernel) de sistema operacional de código aberto e gratuito, base para distribuições como Ubuntu, Debian e Fedora.",
    "Kernel": "O componente central de um sistema operacional, que serve de ponte entre os aplicativos e o processamento real de dados.",
    "Framework": "Conjunto de códigos predefinidos que fornece uma estrutura básica para o desenvolvimento de aplicações.",
    "Biblioteca": "Coleção de subrotinas, funções ou classes usadas para desenvolver software, sem impor a estrutura do app como o framework.",
    "Compilador": "Programa que traduz o código-fonte escrito em uma linguagem de alto nível para linguagem de máquina.",
    "Interpretador": "Programa que executa o código-fonte linha por linha, sem a necessidade de compilação prévia em um arquivo binário.",
    "Cibersegurança": "Prática de proteger sistemas, redes e programas contra ataques digitais, roubo de dados ou danos.",
    "Firewall": "Dispositivo de segurança de rede que monitora o tráfego de entrada e saída com base em regras de segurança predefinidas.",
    "Criptografia": "Prática de codificar dados para que apenas o destinatário pretendido possa lê-los e processá-los.",
    "VPN": "Virtual Private Network. Rede de comunicações privada construída sobre uma rede pública, mascarando a identidade digital.",
    "Phishing": "Tipo de ataque cibernético de engenharia social usado para roubar dados confidenciais através de mensagens enganosas.",
    "Ransomware": "Tipo de malware que criptografa os dados da vítima e exige um pagamento (resgate) para restabelecer o acesso.",
    "Malware": "Software malicioso projetado especificamente para danificar, perturbar ou obter acesso não autorizado a um computador.",
    "QA": "Quality Assurance. Garantia de Qualidade. Processo sistemático para garantir que o software atenda aos requisitos especificados.",
    "Refatoração": "Processo de reestruturação de um código-fonte existente sem alterar seu comportamento externo, melhorando sua legibilidade.",
    "Clean Code": "Filosofia de desenvolvimento que defende a escrita de códigos fáceis de ler, entender e manter.",
    "Open Source": "Código Aberto. Software cujo código-fonte é disponibilizado publicamente para modificação e distribuição.",
    "SaaS": "Software as a Service. Modelo de distribuição onde o software é hospedado na nuvem e acessado via internet por assinatura.",
    "CI/CD": "Continuous Integration e Continuous Delivery. Prática de automatizar a integração e a entrega de alterações de código.",
    "Microserviços": "Abordagem de arquitetura de software onde o app é estruturado como uma coleção de serviços independentes e modulares.",
    "Monólito": "Arquitetura de software tradicional onde todo o sistema e suas funções são construídos e implantados como uma única unidade.",
    "HTTP": "Hypertext Transfer Protocol. Protocolo de comunicação base da World Wide Web, usado para transferir dados na internet.",
    "REST": "Representational State Transfer. Estilo arquitetural para design de APIs de rede baseado no protocolo HTTP.",
    "JSON": "JavaScript Object Notation. Formato leve de intercâmbio de dados, fácil de ler para humanos e fácil de processar para máquinas.",
    "IDE": "Integrated Development Environment. Ambiente de Desenvolvimento Integrado, software que reúne ferramentas para programar.",
    "SDK": "Software Development Kit. Conjunto de ferramentas de desenvolvimento de software que permite a criação de aplicações para um sistema.",
    "UX": "User Experience. Experiência do Usuário. Como uma pessoa se sente ao interagir com um sistema digital.",
    "UI": "User Interface. Interface do Usuário. Os elementos visuais com os quais as pessoas interagem em um aplicativo ou site."
}

# Lista de palavras-chave para validar se um novo termo pertence à área de TI
PALAVRAS_CHAVE_TI = [
    "codigo", "program", "software", "hardware", "web", "dados", "rede", "computa", "sistema", "internet",
    "desenvolv", "app", "cloud", "nuvem", "seguran", "cripto", "banco", "server", "servidor", "api", "framework",
    "tech", "tecnologia", "ia", "ai", "data", "cyber", "virtual", "digital", "stack", "script", "autom"
]

class DicionarioTIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu dicionário de TI!")
        self.setMinimumSize(900, 600)
        self.init_ui()

    def init_ui(self):
        # Estilização Master (QSS) - Dark Cyberpunk theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0d0f12;
            }
            QLabel {
                color: #00ffcc;
                font-family: 'Segoe UI', Arial;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #1a1f26;
                color: #ffffff;
                border: 2px solid #1f2d3d;
                border-radius: 8px;
                padding: 12px;
                font-size: 15px;
                font-family: 'Segoe UI';
            }
            QLineEdit:focus {
                border: 2px solid #00ffcc;
            }
            QListWidget {
                background-color: #14181f;
                border: 1px solid #1f2d3d;
                border-radius: 8px;
                color: #a0aec0;
                padding: 5px;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
                border-bot\tom: 1px solid #1a1f26;
                border-radius: 4px;
            }
            QListWidget::item:hover {
                background-color: #1e2530;
                color: #00ffcc;
            }
            QListWidget::item:selected {
                background-color: #00ffcc;
                color: #0d0f12;
                font-weight: bold;
            }
            QTextBrowser {
                background-color: #14181f;
                border: 2px solid #1f2d3d;
                border-radius: 8px;
                color: #e2e8f0;
                padding: 20px;
                font-size: 16px;
                line-height: 1.6;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00ffcc, stop:1 #0099ff);
                color: #0d0f12;
                border: none;
                border-radius: 6px;
                padding: 12px 24px;
                font-weight: bold;
                font-size: 14px;
                text-transform: uppercase;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #33ffdd, stop:1 #33aaff);
            }
            QPushButton:pressed {
                background: #00b399;
            }
        """)

        # Widget Central e Layout Principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # SEÇÃO ESQUERDA (Busca e Lista de Termos)
        left_panel = QVBoxLayout()
        
        brand_label = QLabel("⚡Dicionário dos Informáticos!")
        brand_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
        left_panel.addWidget(brand_label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Digite o termo que deseja buscar...")
        self.search_bar.textChanged.connect(self.filtrar_termos)
        self.search_bar.returnPressed.connect(self.buscar_termo_direto)
        left_panel.addWidget(self.search_bar)

        self.term_list = QListWidget()
        self.term_list.itemClicked.connect(self.exibir_significado)
        left_panel.addWidget(self.term_list)
        
        main_layout.addLayout(left_panel, stretch=2)

        # SEÇÃO DIREITA (Exibição do Significado)
        right_panel = QVBoxLayout()
        
        detail_title = QLabel("// DEFINIÇÃO DO TERMO")
        detail_title.setFont(QFont("Segoe UI", 11))
        right_panel.addWidget(detail_title)

        self.definition_display = QTextBrowser()
        self.definition_display.setHtml("<span style='color: #4a5568;'>Selecione ou busque um termo para ver sua definição...</span>")
        right_panel.addWidget(self.definition_display)
        
        # Botão para adicionar manualmente, se desejado
        self.btn_add = QPushButton("Sugerir Novo Termo")
        self.btn_add.clicked.connect(self.adicionar_termo_manual)
        right_panel.addWidget(self.btn_add)

        main_layout.addLayout(right_panel, stretch=3)

        # Carregar dados
        self.atualizar_lista_termos()

    def atualizar_lista_termos(self, filtro=""):
        self.term_list.clear()
        termos_ordenados = sorted(DICIONARIO_TI.keys())
        for termo in termos_ordenados:
            if filtro.lower() in termo.lower():
                self.term_list.addItem(termo)

    def filtrar_termos(self):
        filtro = self.search_bar.text()
        self.atualizar_lista_termos(filtro)

    def exibir_significado(self, item):
        termo = item.text()
        significado = DICIONARIO_TI.get(termo)
        html_content = f"""
            <h1 style="color: #00ffcc; margin-bottom: 10px; font-family: 'Segoe UI';">{termo}</h1>
            <hr style="border: 0; height: 1px; background: #1f2d3d; margin-bottom: 20px;">
            <p style="font-size: 16px; color: #e2e8f0; font-family: 'Segoe UI'; line-height: 1.6;">{significado}</p>
        """
        self.definition_display.setHtml(html_content)

    def buscar_termo_direto(self):
        termo_buscado = self.search_bar.text().strip()
        if not termo_buscado:
            return

        # Busca exata (case insensitive)
        termo_encontrado = next((t for t in DICIONARIO_TI if t.lower() == termo_buscado.lower()), None)

        if termo_encontrado:
            # Seleciona o item na lista gráfica e exibe
            items = self.term_list.findItems(termo_encontrado, Qt.MatchExactly)
            if items:
                self.term_list.setCurrentItem(items[0])
                self.exibir_significado(items[0])
        else:
            self.propor_insercao_termo(termo_buscado)

    def propor_insercao_termo(self, termo):
        # Caixa de diálogo estilizada perguntando se deseja adicionar
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("TERMO NÃO ENCONTRADO")
        msg_box.setText(f"O termo '{termo}' não está no banco de dados.")
        msg_box.setInformativeText("Deseja incluir este termo no dicionário de TI?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)
        
        # Customização rápida da janela de mensagem interna
        msg_box.setStyleSheet("""
            QMessageBox { background-color: #14181f; }
            QLabel { color: #ffffff; font-size: 14px; font-weight: normal;}
            QPushButton { background-color: #1f2d3d; color: #ffffff; padding: 6px 15px; border-radius: 4px;}
            QPushButton:hover { background-color: #00ffcc; color: #0d0f12; }
        """)

        resultado = msg_box.exec_()

        if resultado == QMessageBox.Yes:
            self.processar_adicao_termo(termo)

    def processar_adicao_termo(self, termo):
        # Input dialog para pegar a definição
        definicao, ok = QInputDialog.getMultiLineText(
            self, "ADICIONAR TERMO", f"Insira a definição técnica para '{termo}':"
        )
        
        if ok and definicao.strip():
            texto_para_validar = (termo + " " + definicao).lower()
            
            # Validação se pertence à TI
            e_ti = any(palavra in texto_para_validar for palavra in PALAVRAS_CHAVE_TI)
            
            if e_ti:
                DICIONARIO_TI[termo] = definicao.strip()
                self.atualizar_lista_termos()
                self.search_bar.clear()
                
                # Auto-seleciona o item recém adicionado
                items = self.term_list.findItems(termo, Qt.MatchExactly)
                if items:
                    self.term_list.setCurrentItem(items[0])
                    self.exibir_significado(items[0])
            else:
                QMessageBox.warning(
                    self, "ACESSO NEGADO", 
                    "O termo ou a definição fornecida não parecem ter relação estrita com a área de Tecnologia da Informação (TI)."
                )

    def adicionar_termo_manual(self):
        termo, ok = QInputDialog.getText(self, "NOVO TERMO", "Digite o nome do termo técnico:")
        if ok and termo.strip():
            # Se o termo já existir, avisa
            if any(t.lower() == termo.strip().lower() for t in DICIONARIO_TI):
                QMessageBox.information(self, "Aviso", "Este termo já existe no dicionário.")
                return
            self.processar_adicao_termo(termo.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Configuração de paleta escura padrão do sistema para as caixas de diálogo nativas
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#0d0f12"))
    palette.setColor(QPalette.WindowText, QColor("#ffffff"))
    palette.setColor(QPalette.Base, QColor("#14181f"))
    palette.setColor(QPalette.AlternateBase, QColor("#1a1f26"))
    palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
    palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
    palette.setColor(QPalette.Text, QColor("#ffffff"))
    palette.setColor(QPalette.Button, QColor("#1f2d3d"))
    palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
    app.setPalette(palette)

    ex = DicionarioTIApp()
    ex.show()
    sys.exit(app.exec_())
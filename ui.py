class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        try:
            num1 = float(self.view.le1.text())
            num2 = float(self.view.le2.text())
            operator =self.view.cb.currentText()
        
            if operator == '+':
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} - {num2} = {self.sub(num1, num2)}'
            elif operator == '*':
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} / {num2} = {self.div(num1, num2)}'
            elif operator == '^':
                return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
            elif operator == '%':
                return f'{num1} % {num2} = {self.mod(num1, num2)}'
            else :
                return "Calculation Error"
        
        except:
            return "Calculation Error"
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)
        
    def sum(self, a, b):
        return a+b
        
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        try:
            if(b==0):
                raise Exception("Divisor Error")
            
        except Exception as e:
            return e
        
        return a/b
    
    def pow(self, a, b):
        try:
           if (a==0):
                raise Exception("Base Error")
            
        except Exception as e:
            return e
        
        return pow(a, b)   
    
    def mod(self, a, b):
        try:
            if(b==0):
                raise Exception("Divisor Error")
            
        except Exception as e:
            return e
        
<<<<<<< HEAD
        return a%b
    
=======
        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)
        self.le1.selectAll()
        
        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/', '^', '%'])
        
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
        
    def setDisplay(self, text):
        self.te1.appendPlainText(text)
        
    def clearMessage(self):
        self.te1.clear()
>>>>>>> 8f2761c (Modify ui.py to add % operator in Qcombobox)

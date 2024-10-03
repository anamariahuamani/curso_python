### ejempos de banco

class banco:
    def_init_(self,name,lastname,cui,acount,amaut):
    """ funcion inicializafdora
Argumentos:
    name (string): numbre del usuario
    lastnamew (string):apellido del usuario
    cui(int):numro de identificacion dni
    acount (int):numero de cuenta
    amount (int):sald o monto de usuario
"""
self.name=name
self.lastname=lastname
self.cui=cui
self.acount=acount
self.amount=amount


python
class Banco:
    def __init__(self,name,lastname,cui,acount,amount):
        self.name=name
        self.lastname=lastname
        self.cui=cui
        self.acount=acount
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        
    def remove_cash(self,amount):
        if amount > self.amount:
            #este mensaje debe ser manejado por otro metodo
            return "no cuentas con saldo suficiente"
        self.amount-=amount
        
    def status_acount(self):
        #este mensaje deberia mostrar el historial de depositos y retiros
        response=f"""
        ------BIENVENIDO AL BANCO "TEPINCHA Y ESTAFA"------
        Cliente: {self.name}, {self.lastname}  NroCuenta:{self.acount}.
        En estos momentos tienes un saldo de : s/.{self.amount},
        fin del voucher:
        ___________________________________________________________________
        """
        return response

cliente_miguel=Banco("Miguelito","Barraza",784512963,4545,30)
print(cliente_miguel.status_acount())
cliente_miguel.deposit(100)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
`

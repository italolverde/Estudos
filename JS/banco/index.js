valor = 0

tabelaclientes = document.getElementById('clientes')

class Cliente {
    constructor(nome, saldoinicial, id) {
        this.nome = nome
        this.saldo = saldoinicial
        this.id = id
    }

    csacar(valor, cliente) {
        this.saldo -= valor
        console.log(`Foram sacados R$${valor} da conta de ${clientes[cliente].nome}, novo saldo: R$${this.saldo}`)
        document.getElementById('valor').value = null    
    }
    cdepositar(valor) {
        this.saldo += valor
        console.log(`Foram depositados R$${valor} da conta de ${clientes[cliente].nome}, novo saldo: R$${this.saldo}`)    
    }
}
clienteslista = [0]
clientes = [0]
console.log(clientes)
function sacar() {
    cliente = Number(document.getElementById('cliente').value)
    valor = Number(document.getElementById('valor').value)
    clientes[cliente].csacar(valor,cliente)
}
function depositar() {
    cliente = Number(document.getElementById('cliente').value)
    valor = Number(document.getElementById('valor').value)
    clientes[cliente].cdepositar(valor,cliente)
}

function cadastrar() {
    nome = document.getElementById('nomecadastro').value
    document.getElementById('nomecadastro').value = null
    clientes.push(new Cliente(nome, 100, clientes.length))
    console.log(clientes)
    linha = document.createElement("tr")
    linha.appendChild("td")
    linha.appendChild("td")
    linha.appendChild("td")
    clienteslista.push(linha)
    clienteslista[1].innerHTML = 'aaaaaaaaa'
}
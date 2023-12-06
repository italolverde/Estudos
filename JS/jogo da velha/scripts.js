changeplayers()
    rodada = 0
    a1 = document.getElementById("a1")
    a2 = document.getElementById("a2")
    a3 = document.getElementById("a3")
    b1 = document.getElementById("b1")
    b2 = document.getElementById("b2")
    b3 = document.getElementById("b3")
    c1 = document.getElementById("c1")
    c2 = document.getElementById("c2")
    c3 = document.getElementById("c3")
    paragrafo = document.getElementById("para")
    paragrafo.style.color = 'white'
    telinha = document.getElementById("tela")
    function clicar(coord) {
        a = document.getElementsByClassName("but")[coord]
        if(paragrafo.style.color == 'white') { if(a.innerText != 'X' && a.innerText != 'O') {
        if (rodada%2 == 0) {
            a.innerText = 'X'
            a.style.color = "blue"
        } else {
            a.innerText = 'O'
            a.style.color = "red"
        
        } rodada++ }}
    }
    
    function restart() {
        a1.innerText = a2.innerText = a3.innerText = null
        b1.innerText = b2.innerText = b3.innerText = null
        c1.innerText = c2.innerText = c3.innerText = null
        paragrafo.style.color = 'white' 
        paragrafo.innerText = null
        rodada = 0
    }
    function check() {
        if (rodada > 4) {
            if(a1.innerText == a2.innerText && a2.innerText == a3.innerText && a3.innerText == 'X') {
                winmsg(1)
            } else if(a1.innerText == b1.innerText && b1.innerText == c1.innerText && c1.innerText == 'X') {
                winmsg(1)
            } else if(a2.innerText == b2.innerText && b2.innerText == c2.innerText && c2.innerText == 'X') {
                winmsg(1)
            } else if(a3.innerText == b3.innerText && b3.innerText == c3.innerText && c3.innerText == 'X') {
                winmsg(1)
            } else if(b1.innerText == b2.innerText && b2.innerText == b3.innerText && b3.innerText == 'X') {
                winmsg(1)
            } else if(c1.innerText == c2.innerText && c2.innerText == c3.innerText && c3.innerText == 'X') {
                winmsg(1)
            } else if(b2.innerText == 'X') {
                if(a1.innerText == c3.innerText && c3.innerText == 'X') {
                    winmsg(1)
                } else if(c1.innerText == a3.innerText && a3.innerText == 'X') {
                    winmsg(1)
                }
            } else if (rodada > 8){ 
                paragrafo.innerText = 'Empate'
                paragrafo.style.color = 'black'
            }
            if(a1.innerText == a2.innerText && a2.innerText == a3.innerText && a3.innerText == 'O') {
                winmsg(2)
            } else if(a1.innerText == b1.innerText && b1.innerText == c1.innerText && c1.innerText == 'O') {
                winmsg(2)
            } else if(a2.innerText == b2.innerText && b2.innerText == c2.innerText && c2.innerText == 'O') {
                winmsg(2)
            } else if(a3.innerText == b3.innerText && b3.innerText == c3.innerText && c3.innerText == 'O') {
                winmsg(2)
            } else if(b1.innerText == b2.innerText && b2.innerText == b3.innerText && b3.innerText == 'O') {
                winmsg(2)
            } else if(c1.innerText == c2.innerText && c2.innerText == c3.innerText && c3.innerText == 'O') {
                winmsg(2)
            } else if(b2.innerText == 'O') {
                if(a1.innerText == c3.innerText && c3.innerText == 'O') {
                    winmsg(2)
                } else if(c1.innerText == a3.innerText && a3.innerText == 'O') {
                    winmsg(2)
                }
            }  else if (rodada > 8){ 
                paragrafo.innerText = 'Empate'
                paragrafo.style.color = 'black'  
        } 
    }
}
    function winmsg(player) {
        if (player == 1) {
            paragrafo.innerText = `${jogador1} venceu a partida!`
            paragrafo.style.color = 'black'
        } else {
            paragrafo.innerText = `${jogador2} venceu a partida!`
            paragrafo.style.color = 'black'
        }
    }
    function changeplayers() {
        jogador1 = prompt('Nome do jogador que usará o simbolo "X"')
    jogador1 = jogador1.trim()
    if (jogador1 == '') {
        while (jogador1 == '') {
        alert('Nome de jogador invalido, por favor, insira novamente.')
        jogador1 = prompt('Nome do jogador que usará o simbolo "X"')
        jogador1 = jogador1.trim()
    }}
    jogador2 = prompt('Nome do jogador que usará o simbolo "O"')
    jogador2 = jogador2.trim()
    if (jogador2 == '') {
        while (jogador2 == '') {
            alert('Nome de jogador invalido, por favor, insira novamente.')
            jogador2 = prompt('Nome do jogador que usará o simbolo "O"')
            jogador2 = jogador2.trim()
        }
    }
}
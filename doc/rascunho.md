Cliente e Servidor

Sala (uma partida)

[conexão]
Cliente->Servidor
Eu sou o usuario X
<- Ok
<- Err(usuário X já esta conectado)

[conexão com a sala]
Cliente->Servidor
Conectar na sala Y
<- Ok
<- Err(sala fechada)

[na sala]
Cliente->Servidor
Definir baralho(ids)
Pronto()

[na partida]
Cliente->Servidor
**JogarCarta(detalhes) // terreno
MoverCriatura(detalhes) // mesma coisa que atacar
EvoluirCriatura(detalhes)
**EncerrarTurno(detalhes)
Servidor->Cliente
ComeçarTurno()
MoverCriaturaNoTabuleiro()
ColocarCriaturaNoTabuleiro()
ColocarTerreno()
ExcluirCarta()
AdicionaCartaNaMão(detalhes)
FimDePartida



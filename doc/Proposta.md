# Natureza
Um jogo sobre evolução e eventos naturais.

## Grupo 13

- Emanuel Lima		    9009493
- Victor Tsutsumiuchi   7275747
- Vitor Silva           10263531

## Proposta
Em `Natureza` dois jogadores se confrontam num combate de domínio de territórios usando criaturas que evoluem e interagem com os ambientes.

O jogo acontece num tabuleiro 4x4 inicialmente vazio e cada jogador com um deck de 42 cartas embaralhadas saca 5 cartas.

O jogo se passa em turnos alternados entre os jogadores com a seguinte estrutura de fases:
- saque (o jogador saca uma carta)
- ação (o jogador realiza suas ações)
- encerramento (as cartas que sofreram dano recuperam o dano sofrido)

O jogador que começar o jogo não saca no primeiro turno.

Dentre os tipos de cartas que existem no jogos temos:
- terrenos
- criaturas básicas
- criaturas evoluídas
- adaptações
- eventos naturais

## Terrenos

Os terrenos são usados para preencher os campos vazios do tabuleiro. Cada jogador pode colocar apenas um terreno por turno e uma criatura precisa estar sobre ele no turno em que ele foi colocado para ser fixado, caso não tenha uma criatura no terreno a ser fixado no fim do turno ele é removido do jogo.

Todos os terrenos possuem tipos primário e tipos secundários.
Os tipos primários são:
- Planície*
- Montanha*
- Floresta
- Deserto
- Pantano*
- Mar*
- Rio*

(* ainda não estarão disponíveis na v0.1.0)

Atualmente os tipos secudários são:
- Básico

Além dos tipos terrenos podem possuir efeitos, como dar bônus de ataque para as criaturas que estão nele, e possuem uma capacidade de criaturas.

## Criaturas básicas

As criaturas possuem atributos de resistência e ataque. O jogador pode colocar 1 criatura básica por turno e ela precisa ser colocada num terreno fixado de controle do jogador que tenha o tipo primário da criatura (se o terreno tiver mais de um tipo, ele aceita criatura dos tipos primários que ele possui).

Caso o terreno em que a criatura for colocada tiver uma ou mais criaturas, o jogador precisa definir em que posição da pilha de criaturas ela é colocada (as criaturas possuem uma ordem quando estão num terreno).

Criaturas básicas possuem um tipo primário dentre os tipos primários de terreno e possuem categorias como:
- sapo
- macado
- peixe
- guerreiro
- arvore
- etc...

Criaturas básicas não possuem efeito e depois do primeiro turno que foram colocadas elas podem 1 vez por turno na fase de ação mover para um terreno adjacente (Norte, Sul, Leste, Oeste) que tenha espaço livre de criatura ou (exclusivo) evoluir. Tal como quando invocado, se mover para um terreno com uma ou mais criaturas o jogador deve definir em que posição ele entra na pilha de criaturas. Ela também pode mover na pilha do terreno, apenas se reordenando na pilha.

Caso o jogador tente mover a criatura para um terreno inimigo sem criaturas esse terreno no fim do turno passa a ser controlado pelo jogador.

Caso o jogador tente mover a criatura para um terreno inimigo com criaturas, ela combate a criatura do topo da pilha e caso sobreviva e a pilha de criaturas do terreno estiver a criatura se move para o terreno que passa a ser controlada pelo jogador no fim do turno.

O combate é feito subtraindo o ataque da criatura inimiga da resistência da criatura atacante e o ataque da criatura da atacante da resistência da criatura inimiga. Caso uma criatura fique com 0 ou menos de resistência ela é removida do jogo.

Na fase de encerramento, as criaturas regeneram o dano de resistência.

Caso a criatura evolua, ela é substituída por uma carta de evolução compatível com as suas categorias e mantém os efeitos aplicados.

Por fim criaturas podem ter terrenos letais, no caso da criatura estar num terreno do tipo letal dela ela é removida do jogo (peixe no deserto por exemplo).

## Criaturas evoluídas

As criaturas evoluídas também atributos de resistência e ataque bem como categorias, tipos primário e terrenos letais.

Para evoluir, a criatura básica em campo precisa ter a mesma categoria da criatura evoluida na mão do jogador. Exceto pelo turno em que a criatura evoluida entrou no campo, ela pode realizar as ações de mover e procriar.

Criaturas podem exigir além da categoria da criatura que ela evoluiu, outros critérios como acontecer num terreno de tipo primário específico (Por exemplo, a criatura básica `girino` é do tipo `rio`, porém o `sapo` precisa que o `girino` esteja num terreno de `floresta`, `planície` e ou `montanha` para evoluir).

Criaturas evoluídas podem possuir efeitos e além disso, caso duas criaturas evoluídas estejam no mesmo terreno e possuírem a mesma criatura básica como base (mesmo nome), o jogador pode realizar a ação de procriar caso o terreno tenha 1 espaço livre. O jogador coloca uma criatura do tipo básico das criaturas no terreno, essa criatura básica não pode realizar ações nem durante este turno nem o próximo turno.

## Adaptações

São cartas aplicadas a criatura e terrenos. Elas causam efeitos dos mais diversos e podem ser apenas usadas no turno do jogador.

## Eventos naturais

São cartas que podem ser usadas no turno do jogador, bem como no turno do oponente. Elas podem ser ativadas em momentos em que algum jogador inimigo realiza alguma ação ou como uma ação no turno do jogador.

Dentre os eventos naturais temos como exemplo `desertificação` onde o terreno alvo tem seu tipo primário substituído pelo tipo deserto.

## Objetivo do jogo

O objetivo dos jogadores é dominar o terreno inicial do jogador inimigo. Duas quinas opostas do jogo são consideradas especiais. Nelas o terreno colocado é fixado imediatamente e o jogador é obrigado a colocar um terreno no seu primeiro turno, senão ele perde o jogo. Esse terreno é denominado terreno inicial e não pode ser alvo de efeitos que removam o terreno (ao remover um terreno com criaturas, elas são removidas do jogo também).
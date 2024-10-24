Padrão de Design: Abstract Factory
O padrão de design Abstract Factory foi escolhido para este projeto por sua capacidade de fornecer uma interface para a criação de famílias de objetos relacionados, sem especificar suas classes concretas. Esse padrão é particularmente adequado para um projeto como o simulador de corridas da Uber, pois há diferentes componentes (motoristas, passageiros e corridas) que podem ser criados de forma independente, mas que devem funcionar em conjunto para compor o sistema.

Motivos para a escolha do Abstract Factory:
Escalabilidade e Flexibilidade:

O projeto pode crescer e incluir novas entidades (como diferentes tipos de motoristas ou passageiros) sem que seja necessário modificar o código existente. Basta adicionar novas fábricas que herdam da interface abstrata e implementam a criação dos novos tipos de objetos.
Exemplo prático: poderíamos facilmente adicionar diferentes tipos de corridas (por exemplo, "corridas de luxo" ou "corridas compartilhadas") simplesmente criando uma nova implementação da fábrica de corridas.
Desacoplamento:

Com o Abstract Factory, as classes que consomem os objetos criados (por exemplo, a lógica de gerenciamento de corridas) não precisam saber quais classes específicas estão sendo instanciadas. Isso reduz o acoplamento entre os componentes do sistema, facilitando a manutenção.
Isso é importante em sistemas grandes como o Uber, onde diferentes módulos podem ser atualizados ou substituídos independentemente.
Organização e Manutenibilidade:

O padrão ajuda a organizar o código de maneira clara, separando as responsabilidades de criação de objetos da lógica de negócios. Isso facilita a manutenção e legibilidade do código, além de promover uma arquitetura mais modular.
As fábricas centralizam a criação dos objetos, mantendo o código de criação em um lugar específico, ao invés de espalhá-lo pela aplicação.
Facilidade para Testes:

O Abstract Factory torna os testes unitários mais simples, pois podemos criar facilmente objetos falsos ou mockados para testes ao invés de instanciar diretamente classes concretas.
Com o uso de fábricas, podemos simular diferentes comportamentos ou cenários com pouco esforço, substituindo implementações de fábricas em diferentes contextos de testes.
Aplicação no Projeto
No contexto deste simulador de corridas, o Abstract Factory foi aplicado da seguinte forma:

DriverFactory: É responsável por criar os motoristas (objetos da classe Driver), garantindo que os detalhes sobre os motoristas sejam encapsulados e criados de maneira consistente.

PassengerFactory: Cuida da criação dos passageiros (objetos da classe Passenger), que, assim como os motoristas, podem ter variações em uma implementação futura.

RideFactory: Lida com a criação de corridas (objetos da classe Corrida), encapsulando a lógica que relaciona motoristas e passageiros para formar uma corrida.

Essa abordagem mantém o código altamente extensível e facilita a adaptação do sistema caso haja necessidade de incluir novas funcionalidades ou entidades no futuro.

Conclusão
A escolha do padrão Abstract Factory neste projeto possibilitou a criação de uma aplicação modular, escalável e fácil de manter. A separação das responsabilidades entre a lógica de criação e a lógica de negócios facilitou o desenvolvimento e teste da aplicação, permitindo futuras expansões sem a necessidade de grandes mudanças no código base.

Como rodar o projeto

    1. Clone o repositório:
        git clone https://github.com/PedroSbardelotto/Uber_simulator.git

    2. Instale as dependências:
        pip install -r requirements.txt 
    
    3. Execute os testes:
        python -m unittest discover
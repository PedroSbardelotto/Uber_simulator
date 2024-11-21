# Padrão de Design: Abstract Factory
O padrão de design Abstract Factory foi escolhido para este projeto por sua capacidade de fornecer uma interface para a criação de famílias de objetos relacionados, sem especificar suas classes concretas. Esse padrão é particularmente adequado para um projeto como o simulador de corridas da Uber, pois há diferentes componentes (motoristas, passageiros e corridas) que podem ser criados de forma independente, mas que devem funcionar em conjunto para compor o sistema.

## Motivos para a escolha do Abstract Factory:

### Escalabilidade e Flexibilidade:

O projeto pode crescer e incluir novas entidades (como diferentes tipos de motoristas ou passageiros) sem que seja necessário modificar o código existente. Basta adicionar novas fábricas que herdam da interface abstrata e implementam a criação dos novos tipos de objetos.
Exemplo prático: poderíamos facilmente adicionar diferentes tipos de corridas (por exemplo, "corridas de luxo" ou "corridas compartilhadas") simplesmente criando uma nova implementação da fábrica de corridas.
Desacoplamento:

Com o Abstract Factory, as classes que consomem os objetos criados (por exemplo, a lógica de gerenciamento de corridas) não precisam saber quais classes específicas estão sendo instanciadas. Isso reduz o acoplamento entre os componentes do sistema, facilitando a manutenção.
Isso é importante em sistemas grandes como o Uber, onde diferentes módulos podem ser atualizados ou substituídos independentemente.

### Organização e Manutenibilidade:

O padrão ajuda a organizar o código de maneira clara, separando as responsabilidades de criação de objetos da lógica de negócios. Isso facilita a manutenção e legibilidade do código, além de promover uma arquitetura mais modular.
As fábricas centralizam a criação dos objetos, mantendo o código de criação em um lugar específico, ao invés de espalhá-lo pela aplicação.

### Facilidade para Testes:

O Abstract Factory torna os testes unitários mais simples, pois podemos criar facilmente objetos falsos ou mockados para testes ao invés de instanciar diretamente classes concretas.
Com o uso de fábricas, podemos simular diferentes comportamentos ou cenários com pouco esforço, substituindo implementações de fábricas em diferentes contextos de testes.

### Aplicação no Projeto
No contexto deste simulador de corridas, o Abstract Factory foi aplicado da seguinte forma:

**DriverFactory:** É responsável por criar os motoristas (objetos da classe Driver), garantindo que os detalhes sobre os motoristas sejam encapsulados e criados de maneira consistente.

**PassengerFactory:** Cuida da criação dos passageiros (objetos da classe Passenger), que, assim como os motoristas, podem ter variações em uma implementação futura.

**RideFactory:** Lida com a criação de corridas (objetos da classe Corrida), encapsulando a lógica que relaciona motoristas e passageiros para formar uma corrida.

Essa abordagem mantém o código altamente extensível e facilita a adaptação do sistema caso haja necessidade de incluir novas funcionalidades ou entidades no futuro.

## Conclusão
A escolha do padrão Abstract Factory neste projeto possibilitou a criação de uma aplicação modular, escalável e fácil de manter. A separação das responsabilidades entre a lógica de criação e a lógica de negócios facilitou o desenvolvimento e teste da aplicação, permitindo futuras expansões sem a necessidade de grandes mudanças no código base.

# Uso do Padrão Proxy na Criação do Passageiro
No projeto, adotamos o Padrão Proxy na criação de um novo passageiro para adicionar uma camada extra de controle e flexibilidade no processo de criação de objetos. A principal motivação para a escolha desse padrão foi a necessidade de desacoplar a lógica de criação do passageiro da lógica principal do controlador e permitir a inserção de funcionalidades adicionais de forma transparente.

## Benefícios do Proxy:
**Encapsulamento de Lógica Extra:** O Proxy permite que adicionemos funcionalidades como validação, autenticação, logging ou auditoria no momento da criação do passageiro, sem modificar o código da classe original (PassengerService). Isso mantém a classe PassengerService focada na responsabilidade de criar e gerenciar passageiros, enquanto o Proxy lida com aspectos transversais, como validações ou logs.

**Centralização de Regras de Negócio:** Caso precisemos adicionar regras de negócios adicionais (como verificar se o passageiro já existe, validar o formato dos dados ou registrar eventos em logs), podemos implementá-las facilmente dentro do Proxy. Isso evita a duplicação de código e facilita a manutenção futura.

**Desacoplamento:** Ao utilizar o Proxy, a camada de controle (no caso, o controlador de criação do passageiro) fica desacoplada da lógica de criação efetiva do passageiro. Isso facilita a alteração do comportamento da criação de passageiros sem impactar diretamente o fluxo de controle da aplicação, promovendo maior flexibilidade e facilidade de teste.

**Extensibilidade:** O padrão Proxy permite que, futuramente, outras funcionalidades possam ser inseridas na criação de passageiros sem precisar modificar o código do controlador ou da classe PassengerService. Por exemplo, podemos introduzir verificações de segurança ou integrações com outros sistemas, sem alterar a estrutura de código já existente.

## Como Funciona
Quando a criação de um passageiro é requisitada, o controlador utiliza o PassengerProxy para interceptar a criação. O Proxy valida e processa a solicitação, e só então delega a criação real do passageiro para o PassengerService. O uso do Proxy também facilita o controle de erros, pois é possível tratar exceções ou problemas antes de finalizar a criação do passageiro.

Em resumo, o uso do Proxy traz flexibilidade e controle, permitindo que possamos adicionar funcionalidades extras à criação do passageiro de maneira escalável e organizada, sem afetar o código já existente e garantindo que as responsabilidades estejam bem divididas entre as camadas da aplicação.

 ### Por que usar o padrão Template Method?

O padrão Template Method é uma abordagem poderosa para definir o esqueleto de um algoritmo em uma classe base abstrata, permitindo que subclasses personalizem partes específicas desse algoritmo sem alterar sua estrutura geral. Ele promove a reutilização de código ao encapsular os passos comuns do processo, reduzindo duplicação e facilitando a manutenção. Além disso, o Template Method segue o princípio de projeto "Open/Closed" (aberto para extensão, fechado para modificação), pois permite que novas funcionalidades sejam adicionadas através de subclasses sem impactar o código existente. No contexto deste projeto, ele é usado para criar corridas de diferentes tipos (econômica e luxo), garantindo que todas sigam um fluxo comum de criação, mas permitindo que regras específicas sejam aplicadas para cada tipo. Isso torna o código mais organizado, flexível e fácil de expandir.

### Criadores:
Pedro Sbardelotto. 
Jonatas Davi Nascimento da Silva.




## Como rodar o projeto

    1. Clone o repositório:
        git clone https://github.com/PedroSbardelotto/Uber_simulator.git

    2. Instale as dependências:
        pip install -r requirements.txt 
    
    3. Execute os testes:
        python -m unittest discover

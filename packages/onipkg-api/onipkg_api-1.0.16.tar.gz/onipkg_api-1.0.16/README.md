# OniDev's Helper Para Consumo das API's

Retorna objeto json da requisição das API's trabalhadas até o momento.

## Como testar sua contribuíção antes de enviar uma PR
Primeiramente faça a desinstalação do pacote presente em sua `venv`.

```bash
pip uninstall onipkg_api
```

Após a desinstalação, instale o pacote atráves do código fonte modificado.

```bash
pip install -e <path>/onipkg_api/
```

Teste a implementação feita em um projeto terceiro ou até mesmo usando os códigos de teste disponíveis. Após testar o código atual faça a desinstalação do pacote novamente.

```bash
pip uninstall onipkg_api
```

Após o teste crie sua PR e envie para avaliação.
Se deseja que sua PR vire uma nova release, não se esqueça de mudar no `setup.py` na opção version adicione o nome da
próxima versão proposta para o pacote.

## Como criar uma nova release do projeto
Uma vez que sua contribuição for aprovada via PR você está preparado para criar uma nova release do projeto.

O primeiro passo é criar uma nova tag com base no commit que foi aprovado. Para isso na branch master execute o comando:

```bash
git tag -a <tag_name> -m "<comentário descritivo da tag>"
```

Exemplos de `tag_name`: `v1.2`, `v1.2.3` ou `v1.2-beta`

Com a tag criada faça o seu envio para o repositório no `GitHub`.

```bash
git push origin <tag_name>
```

Com a tag enviada podemos seguir para a criação de uma release.
Essa pode ser criada diretamente pelo github com os seguintes passos:
 - Vá no repositório do projeto no GitHub na aba Code.
 - Acesse o menu Releases presente, normalmente, no lado direito.
 - Clique na opção Tags para ver a listagem de tags.
 - Clique nos três pontinhos a direita na tag que você acabou de criar.
 - Selecione a opção create release.
 - Adicione um nome na release (pode ser o mesmo nome da tag) e uma descrição para as novas features da tag.

## **Introdução à linguagem estruturada de consulta (SQL)**

### **1. O que é Linguagem estruturada de Consulta** - *Structured Query Language (SQL)?*

SQL é uma linguagem de consulta utilizada para tratar, elaborar, consultar e alterar banco de dados relacionais (tabular). De sintaxe simples e acessível, SQL se tornou uma linguagem comum aos que trabalham com data, banco de dados, desenvolvimento de softwares, etc e aos que, ocasionamente, precisam extrair, transformar e carregar (ETL) algum tipo de dado em bancos estruturados, contudo não exercem uma função na área. 

### **2. Estrutura do SQL:**

  * *Data Definiton Language* (DDL)
  	Compõe processos de criação, alteração e remoção de dados estruturados.
  * *Data Query Language* (DQL)
  	Consultar dados.
  * *Data Manipulation Language* (DML)
  	Inserir, atualizar e deletar os dados;
  * *Data Control Language* (DCL)
  	Conceder e revogar permissões de acesso à diferentes usuários, e;
  * *Data Transaction Language* (DTL)
  	Gerenciar alterações por DML e permite agrupar as declarações em transações lógicas.


### **2.1 Linguagem de definção de dados (DDL)**

Subconjunto de SQL que compõe os comandos de criação e manutenção dos objetos do BD. Por exemplo: Esquemas, tabelas, índices, chaves, colunas, visões, restrições de integridade.


Comando | Função
------------------------ | -------------------------
CREATE *objeto* | Criar objetos (tabelas, por exemplo) no BD
ALTER *objeto* | Alterar a estrutura ou configuração de um objeto no BD
DROP *objeto* | Excluir um objeto no BD


Esses são os principais objetos do DDL, dado as variantes entre fabricantes de SBGDs.
* Principais objetos: DATABASE, TABLE, INDEX, CONSTRAINT (PRIMARY KEY, FOREIGN KEY, UNIQUE KEY), ROLE, USER, PROCEDURE, FUNCTION, TRIGGER and VIEW.   

	OBS para etapa abaixo:
1. **Criação de BD:**
	CREATE **OBJETO** **NOME_DE_OBJETO;** (<restrição_da_coluna>)- Objeto = DATABASE, por exemplo
2. **Exclusão de BD:**
	DROP **OBJETO** **NOME_DE_OBJETO;** - Objeto = DATABASE, por exemplo
OBS: drop database elimina TODO o DB e seus objetos (CUIDADO). Not build in function
3. **Alteração de tabela:**
	ALTER **OBJETO** **NOME_DE_OBJETO** - Objeto = TABLE, por exemplo
4. **Eliminar dados:**
	TRUNCATE **OBJETO** **NOME_DE_OBJETO** - Objeto = TABLE, por exemplo
5. **Restrições de coluna:**
	NOT NULL, DEFAULT value e CHECK(conditional)
6. **Restrições de tabela:** **TROQUE ( POR [**
-	PRIMARY KEY - (<Coluna(s)_da_chave_primária>)
-	UNIQUE (<Coluna(s)_da_chave_candidata>)
-	FOREIGN KEY (<Colunas_da_chave_estrangeira>)
-	REFERENCES tableref {(<chave_primária>) (<ações>)}
7. **Ações Restrições de tabela**
-	ON DELETE | ON UPDATE
-	CASCADE | SET NULL | SET DEFAULT
-	CHECK(conditional)
8. **Alteração de tabela**
-	ALTER TABLE tabela <ação>;
9. **Ações Restrições de alteração**
-	ADD atributo/novacoluna tipo <restrições_de_coluna>
-	ADD (CONSTRAINT nome) <restrições_de_tabela>
-	DROP atributo/coluna (CASCADE | RESTRICT)
-	DROP CONSTRAINT nome
-	ALTER coluna DROP DEFAULT;
-	ALTER coluna SET DEFAULT <value>;

* CASCADE: Todas as visões e restrições (constraints) que referenciam o atributo são removidas automaticamente.
* RESTRICT: Atributo só é removido se não houver nenhuma visão ou restrição que o referencie.

10. **CREATE VIEW** <nome_da_view> AS <comando_DQL_para_criar_visão>;
DROP VIEW <nome_da_view>;
FAcilita acesso as visões


### **2.2 Linguagem de Manipulação de dados (DML)**

Subconjunto do SQL que trata de operações de manipulação de dados que inclui (INSERT), altera (UPDATE) e deleta (DELETE).

1. **Inclusão ou inserção de dados:**


-	INSERT INTO nome_tabela (<lista_atributos>)
	VALUES (lista_valores_atributos) (lista_valores_atributos)

2. **Alteração de dados:**

-	UPDATE nome_tabela
-	SET nome_atributo_1 = valor
	({nome_atributo_1 = valor})
	WHERE conditional

3. **Exclusão de dados:**

-	DELETE FROM nome_tabela
	WHERE conditional


### **2.3 Linguagem de consulta de dados (DQL)**

Compõe o subconjunto do SQL que realiza a leitura dos da tabela avaliada. É composta por SELECT (selecionar todos os dados ou parte dele), FROM (localização no banco de dados)

1. **Seleção geral ou específica:**
Seleciona todos ou parte do conjunto de dados/colunas de uma tabela.

-	 SELECT * FROM nome_banco.nome_tabela ou

-	SELECT coluna1, coluna2 FROM nome_banco.nome_tabela

2. **Seleção de distintos:**
Apresenta a tabela com valores não duplicados (distintos).

-	 SELECT DISTINCT coluna1, coluna2... FROM nome_banco.nome_tabela (ou) nome_tabela

3. **Seleção ordenada:**
Ordena as colunas conforme descrito geral ou individual para cada coluna (ascendente ou descendente).

-	SELECT coluna1, coluna2... FROM nome_tabela ORDER BY coluna1, coluna2 ASC|DESC;

-	SELECT coluna1, coluna2... FROM nome_tabela ORDER BY coluna1 ASC, coluna2 DESC;

4. **Seleção por filtro (condicional):**
Seleciona uma parte dos dados que estão ou não dentro do especificado(=, >, <, <>, <= e >=).

-	SELECT coluna1... FROM nome_tabela WHERE condição;

-	SELECT coluna1... FROM nome_tabela WHERE NOT condição;

5. **Seleção por filtro de valor nulo:**
Seleciona uma parte dos dados que estão ou não dentro do especificado (Nulo ou não nulo)

-	SELECT coluna1... FROM nome_tabela WHERE coluna1 IS NULL;

-	SELECT coluna1... FROM nome_tabela WHERE coluna1 IS NOT NULL;

6. **Seleção por filtro com operadores lógicos:**

-	SELECT coluna1... FROM nome_tabela WHERE coluna1 IS NULL AND (coluna2 = 0 OR coluna3 = TRUE);

7. **Seleção e funções de agregação:**
Seleção por funções de agregação são viáveis via comando de consulta. Há MIN (mínimo), MAX (máximo), COUNT(conte), AVG(média), SUM(soma), etc.

-	SELECT MIN(coluna1), MAX(coluna2), COUNT(coluna3), AVG(coluna4), SUM(coluna5) FROM nome_tabela WHERE condição;

8. **Seleção por filtro de funções de agrupamento:**
Agrupa e impõe condições ao valor.

-	SELECT coluna1 FROM nome_tabela WHERE condição GROUP BY coluna1 HAVING condição;

9. **Seleção por operador *BETWEEN*:**
Seleção entre *range* de valores.

-	SELECT * FROM nome_tabela WHERE coluna_$ BETWEEN 500 AND 100;

10. **Seleção por operador *LIKE*:**
Compara partes de uma sequência de caracteres.

-	Atributo LIKE %STRING% ou *STRING* compara qualquer substring
-	Atributo LIKE _STRING__ compara qualquer caracter (diferencia maísculo, etc - *case sensitive*)


#### **2.3.1 Consultas aninhadas**

É possível desenvolver comandos utilizando subconsultas *subqueries*
Exemplo: SELECT colunas FROM tabela ou lista de tabelas WHERE coluna operador subquery;

*	**Operadores:** IN, NOT IN, EXIST, NOT EXIST, ALL, SOME, ANY e operadores aritméticos.

-	SELECT * FROM tabela1 WHERE col1 IN (SELECT DISTINCT col2 FROM tabela2

#### **2.3.2 Junções, mesclas ou acréscimos**

Junções *joins* são consultas usadas para recuperar dados de várias tabelas em apenas uma consulta. Operadores *joins* utilizam duas relações e retornam outra relação como resultado. Para isso, faz-se uso do chaves estrangeiras ou *FOREIGN KEY*.

Há quatro tipos de JOINS:
1. **INNER JOIN ou apenas JOIN:**
Retorna apenas registros que existem em ambas as tabelas;

2. **LEFT JOIN ou LEFT OUTER JOIN:**
Retorna os registros que existem na tabela da esquerda e os que a intersectam na direita.

3. **RIGHT JOIN ou RIGHT OUTER JOIN:**   
Retorna os registros que existem na tabela da direita e os que a intersectam na esquerda.

4. **FULL JOIN ou FULL OUTER JOIN:**
Retorna todos os registros das tabelas esquerda e direita (indiferente se há intersecção)

-	SELECT * FROM tabela 1 LEFT JOIN tabela 2 ON tabela1.coluna1 = tabela2.coluna2


### **2.4 Linguagem de controle de acesso a dados (DCL)**

Foca na manutenção da segurança interna do banco de dados e seus objetos, evitando acessos não alterizados e modificações indesejadas. A função do DCL é conceder e revogar permissões de acesso dos usuários ao banco de dados.

-	GRANT (concessão) e REVOKE (revogar)
-	CREATE USER/ROLE (criar regra ou usuário) ou ALTER USER/ROLE (alterar regra ou usuário)

1. **CREATE ROLE:**
Criar nova regra ou papel.
CREATE ROLE 'developer';

2. **DROP ROLE:**
Remover regra ou papela.
DROP ROLE nome_regra lista de roles;

3. **CREATE USER:**
Cria usuários e define seu host e senha.
CREATE USER user IDENTIFIED BY password
CREATE USER user@localhost IDENTIFIED BY password

4. **DROP USER**
Exclui um usuário.
DROP USER user(@se houver host)

#### **2.4.1 Permissões**
Libera ou restringe o que pode ser realizado por usuário específico e onde.

1. **GRANT:**
Concede privilégios para usuário/role.
GRANT lista de privilégios ON objeto
TO lista de usuários/roles (public = para todo mundo) WITH GRANT OPTION (propaga a permissão ou não?) GRANTED BY autoridade;

* GRANT ALL PRIVILEGES ON database.table TO 'dba (ao banco de dados
* GRANT SELECT ON database.* TO 'read'
* GRANT INSERT, UPDATE, DELETE ON database.*/table TO 'write'; (dá permissões a roles que podem ser reaplicadas)
* GRAND 'read_write' to 'developer';
* SHOW GRANTS FOR 'developer';
* GRANT 'developer' TO user2;

2. **REVOKE**
Revoga privilégios para usuário/role.
REVOKE GRANT OPTION FOR lista de privilégios ON objeto FROM usuário/roles RESTRICT/CASCADE;

* REVOKE DELETE FROM 'read_write' (remove de role)
* REVOKE 'read' FROM user3
* REVOKE INSERT, UPDATE, DELETE ON database.* FROM user1

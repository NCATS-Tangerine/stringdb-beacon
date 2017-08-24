CREATE CONSTRAINT ON (protein:Protein) ASSERT protein.stringId IS UNIQUE;

// ---- Load Actions ---- //

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///9606.protein.actions.v10.5.txt" AS row FIELDTERMINATOR '\t'
WITH DISTINCT row.item_id_a as id_a, row.item_id_b as id_b
MERGE (a:Protein {stringId: id_a})
MERGE (b:Protein {stringId: id_b});

// Added 11021 labels, created 11021 nodes, set 11021 properties, statement executed in 183588 ms.

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///9606.protein.actions.v10.5.txt" AS row FIELDTERMINATOR '\t'
MATCH (a:Protein {stringId: row.item_id_a})
MATCH (b:Protein {stringId: row.item_id_b})
MERGE (a)-[relation:ACTION {mode: row.mode}]-(b)
ON CREATE SET
  relation.action = row.action,
  relation.is_directional = row.is_directional,
  relation.a_is_acting = row.a_is_acting,
  relation.score = row.score;

// Set 4912039 properties, created 1190742 relationships, statement executed in 639046 ms.

// ---- Load Aliases ---- //

USING PERIODIC COMMIT 1000
LOAD CSV WITH HEADERS FROM "file:///9606.protein.aliases.v10.5.txt" AS row FIELDTERMINATOR '\t'
MATCH (p:Protein {stringId: row.string_protein_id})
SET p.alias = row.alias, p.source = row.source;

// Set 4111558 properties, statement executed in 169111 ms.

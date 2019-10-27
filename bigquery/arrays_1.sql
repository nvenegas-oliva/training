
-- Resource https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays

-- OFFSET es el el normal, ie, seq[0] = seq[OFFSET(0)]
WITH sequences AS
  (SELECT [0, 1, 1, 2, 3, 5] AS some_numbers
   UNION ALL SELECT [2, 4, 8, 16, 32] AS some_numbers
   UNION ALL SELECT [5, 10] AS some_numbers)
SELECT some_numbers,
       some_numbers[OFFSET(1)] AS offset_1,
       some_numbers[ORDINAL(1)] AS ordinal_1
FROM sequences;


WITH seq AS (
    SELECT [1, 2, 3, 5] AS some_numbers
    UNION ALL SELECT [1, 2, 3] AS some_numbers
    UNION ALL SELECT [1] AS some_numbers)
SELECT some_numbers, ARRAY_LENGTH(some_numbers) AS len
FROM seq;


-- Flattening arrays
SELECT *
FROM UNNEST(['foo', 'bar', 'baz', 'qux', 'corge', 'garply', 'waldo', 'fred'])
  AS element
WITH OFFSET AS offset
ORDER BY offset;

-- UNNSET destruye el orden del array. Para reconstruirlo, utilizar 'WITH OFFSET'.
SELECT *
FROM UNNEST([3, 1, 3, 4]) AS numbers
WITH OFFSET AS offset
ORDER BY offset DESC;

-- Crea y muestra el contenido de una lista de tipo STRUCT
SELECT *, struct_value
FROM UNNEST(ARRAY<STRUCT<x INT64, y STRING>>[(1, 'foo'), (3, 'bar')])
       AS struct_value;

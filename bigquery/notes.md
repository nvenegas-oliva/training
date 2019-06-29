# GCP - Notes

###  Serverless Data Analysis with Google BigQuery and Cloud Dataflow

##### - Advanced Capabilities in BigQuery (video)

![](img/1.png)

* Los arrays en este contexto correponden a una lista ordenada de elementos del mismo tipo.


```sql
WITH
  WashingtonStations AS (
  SELECT
    weather.stn AS station_id,
    ANY_VALUE(station.name) AS name
  FROM
    `bigquery-public-data.noaa_gsod.stations` AS station
  INNER JOIN
    `bigquery-public-data.noaa_gsod.gsod2015` AS weather
  ON
    station.usaf = weather.stn
  WHERE
    station.state = 'WA'
    AND station.usaf != '999999'
  GROUP BY
    station_id)
SELECT
  washington_stations.name,
  (
  SELECT
    COUNT(*)
  FROM
    `bigquery-public-data.noaa_gsod.gsod2015` AS weather
  WHERE
    washington_stations.station_id = weather.stn
    AND prcp > 0
    AND prcp <99 ) AS rainy_days
FROM
  WashingtonStations AS washington_stations
ORDER BY
  rainy_days DESC;
```

* La subquery hace match con el resultado del WITH.

* Podemos organizar los datos de distintas formas (columnar, ortientado a filas etc), pero los enfoques que se utilicen tendrán un impacto en el rendimiento según la consulta. Puede que el método escogido no pueda hacerse de forma paralela.

![](img/2.png)

* Se pueden organizar los datos de distintas formas. Los enfoques tendrán un rendimiento diferente según la consulta. Puede que el método escogido no pueda hacerse de forma paralela.

![](img/3.png)

* La desnormalización requiere más espacio ya que están los datos duplicados, sin embargo, las queries se pueden procesar de una manera más eficaz y en paralelo con el procesamiento por columnas.

![](img/4.png)

##### - Arrays and Structures (video)

* Queremos conseguir top 2 títulos en función del score para la tabla `stories`.

1. Crear array de (`titles`, `scores`)
2. Extraer la fecha de `time_ts`
3. Agrupar por la fecha
* Entonces, la query es:

```sql
SELECT
    ARRAY_AGG(STRUCT(title, score)) AS titles,
    EXTRACT(DATE FROM time_ts) AS date
FROM `bigquery-public-data.hacker_news.stories`
WHERE
    score IS NOT NULL
    AND title IS NOT NULL
GROUP BY date
```
y el resultado correspondiente:

![](img/5.png)

* La query final corresponde a:
```sql
WITH TitlesAndScores AS (
    SELECT
        ARRAY_AGG(STRUCT(title, score)) AS titles,
        EXTRACT(DATE FROM time_ts) AS date
FROM `bigquery-public-data.hacker_news.stories`
WHERE
    score IS NOT NULL
    AND title IS NOT NULL
GROUP BY date)
SELECT date,
    ARRAY(
        SELECT AS STRUCT
            title,
            score FROM
            UNNEST(titles)
        ORDER BY score DESC
        LIMIT 2) AS top_articles
FROM TitlesAndScores;
```

* Donde `ARRAY(SELECT AS STRUCT ...`:
    1. Desarma el array de la cláusula `WITH` utilizando `UNNEST` function.
    2. Los ordena por el `score` tomando los top 2.
    3. Crea un nuevo array con los resultados obtenidos.
* La query externa:
    1. Proyecta la columna `date`.
    2. Proyecta el array.


Resultado correspondiente es:

![](img/6.png)


##### - Join condition and Window Functions (video)


```sql
SELECT
    name,
    SUM(number) AS occurrences
FROM `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY name
ORDER BY occurrences DESC LIMIT 100
```


```sql
WITH TopNames AS (
    SELECT
        name,
        SUM(number) AS occurrences
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    GROUP BY name
    ORDER BY occurrences DESC LIMIT 100
)
SELECT name, SUM(word_count) AS frequency
FROM TopNames
JOIN `bigquery-public-data.samples.shakespeare`
ON STARTS_WITH(word, name)
GROUP BY name
ORDER BY frequency DESC
LIMIT 100
```

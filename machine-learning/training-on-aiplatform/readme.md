#### Local

Construir la imagen de docker y probarla de forma local.

```
docker build -t gcr.io/spike-sandbox/docker-gcp-demo .
docker run gcr.io/spike-sandbox/docker-gcp-demo --ntrees 100 \
                --learning_rate 0.01 \
                --subsample 0.8 \
                --max_depth 5
```

#### GCP

1) Pushear a container registry (o usar cloud-build)
2) Mandar el job a `ai-platform`

```
docker push gcr.io/spike-sandbox/docker-gcp-demo
gcloud ai-platform jobs submit training prueba_ai_docker \
  --region us-east1 \
  --master-image-uri gcr.io/spike-sandbox/docker-gcp-demo \
  -- \
  --ntrees 100 \
  --learning_rate 0.01 \
  --subsample 0.8 \
  --max_depth 5
```
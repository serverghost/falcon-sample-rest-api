# falcon-sample-rest-api

Demo de un API REST en Python usando Falcon.

## Requerimientos

- Python 3
- Usar un virtualenv de preferencia
- Cuenta en GCP (Opcional)
- CLI gcloud (opcional)

## Instalación Local

Para probar localmente solo se debe ejecutar el comando.

`pip install -r requirements.txt`

## Deploy en Kubernetes

### Build Imagen

`docker build --pull --rm -f "Dockerfile" -t falconsamplerestapi:latest "."`

### Auth GCP

`gcloud auth configure-docker`

### Tag Imagen

`docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]`

### Push Imagen

`docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE]`

### Obtener kubeconfig de GKE

`gcloud container clusters get-credentials task1-cluster-gke --region us-central1`

### Deploy con kubectl

- Crea deplyoment
- Crea service
- Crea ingress

`kubectl apply -f ./`
# Application exemple en Python



## Doc API - Swagger 
https://app.swaggerhub.com/apis/vanessakovalsky/IT-Management/1.0.0#/

## WebHook Relay 
https://webhookrelay.com/blog/2017/11/23/github-jenkins-guide

## Build et lancement de l'image docker 

```sh
docker build -t my-image-python .
docker run -it --rm --name my-app my-image-python
```

## Envoi de l'image Docker 

```sh

 docker tag my-image-python vanessakovalsky/my-image-python:latest
 docker push vanessakovalsky/my-image-python
```

## Execution des tests unitaires :
```
python -m unittest test/unit/test.py 
```

## Execution des tests systèmes : 
* Installer les packages pythons robotframework et robotframework-requests
* Lancer la commande 
```
robot test/system/machine.robot
```

## Création d'un pod kubernetes

```sh
kubectl apply -f manifest-k8s
```

## Utiliser ansible pour créer le cluster K8s

* Télécharger les rôles
```sh
ansible-galaxy install -r requirements.yml -p ./roles
```

 # Demo Github Action

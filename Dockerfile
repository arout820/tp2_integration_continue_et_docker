# Utilisez l'image Jenkins de base
FROM jenkins/jenkins:lts-jdk11

# Passe en utilisateur root pour installer les paquets
USER root

# Définit le mot de passe root
RUN echo "root:mdp" | chpasswd

# Ajoute l'alias "ll" pour la commande "ls -la"
RUN echo "alias ll='ls -la'" >> /etc/bash.bashrc

# Mise à jour des paquets et installation des paquets requis
RUN apt-get update && \
    apt-get install -y python-is-python3 2to3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Repasse à l'utilisateur Jenkins
USER jenkins


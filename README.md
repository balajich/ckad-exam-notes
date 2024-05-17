# ckad-exam-notes
Exam notes of Certified Kubernetes Application Developer (CKAD)
# Setting up cluster
## Prerequisites
- VirtualBox  (https://www.virtualbox.org/wiki/Downloads)
- Vagrant Download (https://developer.hashicorp.com/vagrant/downloads)
## Start the cluster
```bash
git clone https://github.com/scriptcamp/vagrant-kubeadm-kubernetes.git
cd vagrant-kubeadm-kubernetes
vagrant up
```
# Access the cluster
```bash
cd C:\github\vagrant-kubeadm-kubernetes
vagrant ssh controlplane
```
# Core Concepts
- Important commands
- Get Pods
```bash
kubectl get pods
kubectl get pods --all-namespaces
kubectl get pods -n kube-system
kubectl get pods -o wide
```
- Get Nodes
```bash
kubectl get nodes
```
- Get Namespaces
```bash
kubectl get namespaces
```
- Create a namespace
```bash
kubectl create namespace my-namespace
```
- Get all pods in a namespace
```bash
kubectl get pods -n my-namespace
```
- Get all pods in all namespaces
```bash
kubectl get pods --all-namespaces
```
- Create a pod named tomcat using the image tomcat:9.0 in the namespace my-namespace
```bash
kubectl run tomcat --image=tomcat:9.0 -n my-namespace
```
- Get all resources in a namespace
```bash
kubectl get all -n my-namespace
```

# References
- [Practice Environment] (https://github.com/techiescamp/vagrant-kubeadm-kubernetes)
- [CKAD Exercises] (https://github.com/dgkanatsios/CKAD-exercises)
- [Kubernetes Documentation] (https://kubernetes.io/docs/home/)
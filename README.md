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
- The password for vagrant user is vagrant
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
kubectl create namespace mynamespace
```
- Get all pods in a namespace
```bash
kubectl get pods -n mynamespace
```
- Get all pods in all namespaces
```bash
kubectl get pods --all-namespaces
```
- Get all resources in a namespace
```bash
kubectl get all -n mynamespace
```
- Create a pod named tomcat using the image tomcat:9.0 in the namespace my-namespace
```bash
kubectl run tomcat --image=tomcat:9.0 -n mynamespace
```
- Create the above pod using a manifest file
```bash
kubectl run tomcat92 --image=tomcat:9.0 --dry-run=client -o yaml > tomcatpod.yaml
kubectl create -f tomcatpod.yaml -n mynamespace
```
- Create a pod named tomcat from tomcat 9.0 image and run java version command init, delete the pod once the command is executed
```bash
kubectl run tomcat --image=tomcat:9.0 --restart=Never --it --rm -- java -version
```
- Get a namespace definition file called myns with out actually creating it
```bash
kubectl create namespace myns --dry-run=client -o yaml > myns.yaml
```
# References
- [CKAD Curriculum] (https://github.com/cncf/curriculum/blob/master/CKAD_Curriculum_v1.30.pdf)
- [Practice Environment] (https://github.com/techiescamp/vagrant-kubeadm-kubernetes)
- [CKAD Exercises] (https://github.com/dgkanatsios/CKAD-exercises)
- [Kubernetes Documentation] (https://kubernetes.io/docs/home/)
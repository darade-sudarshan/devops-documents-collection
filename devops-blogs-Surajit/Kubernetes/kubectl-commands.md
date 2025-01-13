# Kubernetes - kubectl commands

kubectl get nodes					<--- Getting worker nodes status

---
kubectl get nodes -o wide			<--- Getting worker node status with IP.

---
kubectl run <pod-name> --image <dockerhub-account/container-image> --generator=run-pod/v1   			<-- create a pod. --generator=run-pod/v1 will create a pod with a deployment.

---
kubectl get pods			<---- get list of running pods

---
kubectl get pods -o wide    <--- get list of running pods with other detailed info like IP and all.

---
kubectl describe pod <pod-name>    <--- describe pod, required during troubleshooting.

---
kubectl delete pod <pod-name> 	  <--- deleting the pod.

---
kubectl expose pod <pod-name> --type=NodePort --port=80 --name=<service-name>			<--- exposing the application externally. http://<node1-public-ip>:<node-port>

---
kubectl get svc 			<--- to get the service info

---
kubectl logs <pod-name>		<--- to view the pod access logs. we can use -f to view the log on runtime.

---
kubectl exec -it <pod-name> /bin/bash		<---to login to the container in a pod.

---
kubectl exec -it <pod-name> ls				<-- Running individual command in a container.

---
kubectl get all -A				<--- it provides list of all running resources. -A specifies all namespaces.

---
kubectl delete svc <svc-name>	<--- deleting the service from default namespace.

---
kubectl delete pod <pod-name> 	<--- deleting the pod from default namespace.

---
kubectl get rs			<--- getting list of replicasets.

---
kubectl describe rs <rs-name> 	<--- describing the replicaset

---
kubectl expose rs <rs-name> --type=NodePort --port=80 --target-port=8080 --name=<service-name-to-be-created>		<--- exposing rs as a service.

---
kubectl delete rs <ReplicaSet-Name>		<--- delete the replicaset

---
kubectl create deployment <deployment-name> --image=<dockerhub-id/image-name>:<version> 	<--- create deployment.

---
kubectl get deployment		<--- shows list of all deployment.

---
kubectl describe deployment <deployment-name>		<--- describing the deployment

---
kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>		<-- update the replicas.

---
kubectl expose deployment <deployment-name> --type=NodePort --port=80 --target-port=80 --name=<service-name-to-be-created>		<--- exposing deployment to external world.

---
kubectl edit deployment <deployment-name> --record=true 	<--- updating the deployment lets say from v1 to v2.

---
kubectl rollout status deployment/<deployment-name>			<--- checking the deployment status

---
kubectl rollout history deployment/<deployment-name>		<--- verifying rollout history

---
kubectl rollout undo deployment/<deployment-name>			<--- rollback of the deployment to the prior version.

---
kubectl rollout undo deployment/<deployment-name> --to-revision=3		<-- rollback to specific version.

---

kubectl rollout restart deployment/<deployment-name>				<--- Rolling restarts will kill the existing pods and recreate new pods in a rolling fashion

---
kubectl rollout pause deployment/<Deployment-Name>

kubectl set image deployment/<deployment-name> image=<dockerhub-id/image-name>:<version>  --record=true

kubectl set resources deployment/<deployment-name> -c=<container-name> --limits=cpu=20m,memory=30Mi

kubectl rollout resume deployment/<deployment-name>

  |

  |
	
  -----> Pause and resume deployment steps.

---

kubectl get pods -w  		<--- This command can be used while deploying app, to chk if all the pods are properly getting up or stucks in error.

---
kubectl apply -f deployment.yaml	<--- Used to deploy  the deployment.yaml file.

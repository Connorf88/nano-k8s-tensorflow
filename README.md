# Terminal-Based TensorFlow Serving on Kubernetes

This project demonstrates how to deploy a TensorFlow model locally using Docker, TensorFlow Serving, and Kubernetes via Minikube. All components — Python script, Dockerfile, and Kubernetes manifests — are authored directly in the terminal using `nano`.

> 💡 Use case: zero-cost AI inference workflow for MLOps experimentation and GitOps-ready infrastructure.

---

## 📁 Project Structure

tf-k8s-serve/ ├── model/ │ └── 1/ │ ├── saved_model.pb │ └── variables/ ├── export_model.py ├── Dockerfile ├── deployment.yaml ├── service.yaml


---

## ⚙️ Prerequisites

- Python 3.x with TensorFlow installed
- Docker (with local build access)
- Minikube (Kubernetes cluster)
- Terminal with `nano` editor

---

## 🧪 Step 1: Export a TensorFlow Model

Use the included Python script:

```bash
python3 export_model.py
This will train a basic Keras model and export it to model/1/ in TensorFlow SavedModel format.

🐳 Step 2: Build Docker Image
Build your serving image from the root directory:

bash
docker build -t tfmodel:latest .
Ensure that .dockerignore does not exclude the model/ directory during build.

☸️ Step 3: Deploy to Kubernetes
Start Minikube and point Docker to its daemon:

bash
minikube start
eval $(minikube docker-env)
Apply your Kubernetes manifests:

bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Check that your pod is running:

bash
kubectl get pods
🌐 Step 4: Access the Model Endpoint
Expose the service via Minikube:

bash
minikube service tfmodel-service
Or hit it directly:

bash
curl http://$(minikube ip):30007/v1/models/tfmodel
You should see model status output confirming it's served.

🧱 Architecture Diagram
[ Keras Model Export (Python) ]
            │
            ▼
  [ Local SavedModel Format ]
            │
            ▼
    [ Docker Image Build ]
            │
            ▼
[ TensorFlow Serving Container ]
            │
            ▼
   [ Kubernetes Deployment ]
            │
            ▼
  [ NodePort Service → curl ]
📝 Notes
Model directory must follow TensorFlow Serving’s versioned format (model/1/saved_model.pb)

All files and configurations were created using nano in the terminal — no IDE used

Can serve as a local GitOps lab foundation or be extended into CI/CD-based MLOps

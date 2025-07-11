# Projeto Kubernetes: Deploy Fullstack com React + Flask + PostgreSQL

## 👥 Integrantes da Equipe
- Amanda Laryssa Rodrigues de Mattos
- José Wilquer Nascimento de Lima
## 🎯 Objetivo do Projeto

Realizar o deploy completo de uma aplicação fullstack em um cluster Kubernetes, composta por:

- Frontend: React
- Backend: Flask (API REST)
- Banco de dados: PostgreSQL
- Comunicação via IngressController (NGINX)
- Alta disponibilidade com múltiplas réplicas
- Configuração via ConfigMap e Secrets
- Persistência de dados via PVC

---

## 🧱 Estrutura do Repositório

```
projeto-k8s-deploy/
├── README.md
├── namespace.yaml
├── frontend/
│   └── deployment.yaml
├── backend/
│   ├── deployment.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── database/
│   ├── pvc.yaml
│   ├── statefulset.yaml
│   └── secret.yaml
└── ingress/
    └── ingress.yaml
```

---

## 🚀 Como Executar

> ⚠️ Pré-requisitos:
> - Kubernetes (Minikube, Kind ou cluster real)
> - kubectl configurado
> - Docker com acesso ao DockerHub

### 1. Clone o repositório
```bash
git clone https://github.com/seuusuario/projeto-k8s-deploy.git
cd projeto-k8s-deploy
```

### 2. Crie os namespaces
```bash
kubectl apply -f namespace.yaml
```

### 3. Banco de dados PostgreSQL
```bash
kubectl apply -f database/secret.yaml
kubectl apply -f database/pvc.yaml
kubectl apply -f database/statefulset.yaml
```

### 4. Backend Flask
```bash
kubectl apply -f backend/configmap.yaml -n app
kubectl apply -f backend/secret.yaml -n app
kubectl apply -f backend/deployment.yaml -n app
```

### 5. Frontend React
```bash
kubectl apply -f frontend/deployment.yaml -n app
```

### 6. Ingress Controller
#### Para Minikube:
```bash
minikube addons enable ingress
```

#### Para Kind:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/kind/deploy.yaml
```

### 7. Ingress
```bash
kubectl apply -f ingress/ingress.yaml -n app
```

---

## 🌐 Acesso à Aplicação

Após tudo aplicado, acesse no navegador:

- **Frontend:** [http://localhost/](http://localhost/)
- **API Backend:** [http://localhost/api/messages](http://localhost/api/messages)

> 🔁 Teste também com `curl`:
```bash
curl http://localhost/api/messages
```

---

## ⚙️ Arquitetura Resumida

- **Frontend React:** Deployment com 2 réplicas, acessa o backend via `/api`
- **Backend Flask:** Deployment com 2 réplicas, expõe `/api/messages`
- **PostgreSQL:** StatefulSet com PVC e Secret
- **Ingress NGINX:** Redireciona `/` para o frontend e `/api` para o backend
- **ConfigMap:** Variáveis do Flask e React
- **Secrets:** Usuário e senha do banco, protegidos por `Secret`

---

## ✅ Requisitos Atendidos

- [x] Deploy completo e funcional dos 3 serviços
- [x] ConfigMap e Secrets corretamente utilizados
- [x] Ingress com caminhos `/` e `/api`
- [x] PVC para persistência dos dados do banco
- [x] 2 réplicas para frontend e backend (alta disponibilidade)
- [x] Documentação clara e passo a passo

---

## 💡 Dicas Finais

- Para depurar, use:
```bash
kubectl logs deploy/backend -n app
kubectl exec -it pod/postgres-0 -n database -- psql -U admin -d mensagens
```

- Use `port-forward` para testar localmente:
```bash
kubectl port-forward svc/backend 5000 -n app
```

---

## 🌟 Bonus (não obrigatório)
- [ ] Configurar TLS com cert-manager
- [ ] readiness/liveness probes
- [ ] Horizontal Pod Autoscaling (HPA)

---

**Desenvolvido como parte da disciplina de Avaliação de Desempenho em Redes - IFPB 🏫**

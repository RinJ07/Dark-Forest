
# System Architecture — Barangay Complaint System

## Overview
The Barangay Complaint System is a web-based application built using a modern JAMstack architecture. It consists of a React frontend, Firebase backend, and is deployed on Vercel.

---

# Architecture Diagram

```text
┌─────────────────────────────────────────────────────┐
│                    CLIENT LAYER                     │
│                                                     │
│   ┌─────────────┐         ┌─────────────────────┐   │
│   │  Resident   │         │   Admin (Browser)  │   │
│   │  (Browser)  │         │                     │   │
│   └──────┬──────┘         └──────────┬──────────┘   │
└──────────┼──────────────────────────┼───────────────┘
           │                          │
           ▼                          ▼
┌─────────────────────────────────────────────────────┐
│                  FRONTEND LAYER                     │
│                                                     │
│         React + Vite (Deployed on Vercel)           │
│                                                     │
│   ┌──────────────┐  ┌───────────┐ ┌─────────────┐  │
│   │ FileComplaint│  │ Dashboard │ │ Complaint   │  │
│   │     Page     │  │    Page   │ │ Details Page│  │
│   └──────────────┘  └───────────┘ └─────────────┘  │
│                                                     │
│   ┌──────────────┐  ┌───────────────────────────┐  │
│   │  Login Page  │  │ ProtectedRoute Component │  │
│   └──────────────┘  └───────────────────────────┘  │
└─────────────────────────────┬──────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────┐
│                   BACKEND LAYER                     │
│                                                     │
│       Firebase (Google Cloud - asia-southeast1)     │
│                                                     │
│   ┌──────────────────┐ ┌─────────────────────────┐ │
│   │    Firestore     │ │      Firebase Auth      │ │
│   │                  │ │                         │ │
│   │ complaints/      │ │   Email/Password Auth  │ │
│   │ ├── id           │ │   Admin Account        │ │
│   │ ├── name         │ │                         │ │
│   │ ├── phone        │ └─────────────────────────┘ │
│   │ ├── address      │                             │
│   │ ├── category     │                             │
│   │ ├── description  │                             │
│   │ ├── status       │                             │
│   │ └── date         │                             │
│   └──────────────────┘                             │
└─────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────┐
│                    CI/CD LAYER                      │
│                                                     │
│                 GitHub Actions                      │
│     push to main → Test → Build → Smoke Test       │
│                                                     │
│                       Vercel                        │
│          Auto-deploy on push to main branch         │
└─────────────────────────────────────────────────────┘
```

---

# Data Flow

## Resident Filing a Complaint

1. Resident opens `/file-complaint` page  
2. User fills out the complaint form:
   - Name
   - Phone Number
   - Address
   - Category
   - Description
3. React frontend sends `addDoc()` request to Firestore  
4. Firestore generates a unique complaint ID  
5. Complaint status is automatically set to `"Pending"`  
6. Resident is redirected to the confirmation page  

---

## Admin Managing Complaints

1. Admin opens `/login` page  
2. Firebase Authentication verifies credentials  
3. Auth token stored in browser session  
4. Admin redirected to Dashboard  
5. Dashboard fetches complaints from Firestore  
6. Admin updates complaint status through dropdown  
7. Firestore updates data in real time  

---

# Tech Stack Summary

| Layer | Technology |
|---|---|
| Frontend | React 19 + Vite 6 |
| Styling | Tailwind CSS 3 |
| Routing | React Router DOM 7 |
| Database | Firebase Firestore |
| Authentication | Firebase Auth |
| Hosting | Vercel |
| CI/CD | GitHub Actions |
| Testing | Vitest + React Testing Library |

---

# Key Features

- Resident complaint submission system
- Admin authentication and authorization
- Real-time complaint management
- Protected admin routes
- Responsive web interface
- Automated deployment pipeline
- Scalable cloud-based backend

---

# Deployment Workflow

```text
Developer Pushes Code to GitHub
              │
              ▼
      GitHub Actions CI
   (Test → Build → Validate)
              │
              ▼
          Vercel Deploy
              │
              ▼
      Production Web App
```

---

# Security Measures

- Firebase Authentication for admin access
- Protected admin dashboard routes
- Firestore security rules
- Input validation on forms
- Secure HTTPS deployment via Vercel

---

# Scalability Considerations

- Serverless Firebase backend
- Real-time Firestore database synchronization
- Stateless frontend architecture
- Automatic scaling through Vercel and Firebase infrastructure
- Modular React component structure

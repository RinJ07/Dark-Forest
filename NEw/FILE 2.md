# DevOps Practices — Barangay Complaint System

## 1. Automation

### CI/CD Pipeline (GitHub Actions)

- Automatically runs on every push to `main`
- Pipeline flow:
  - Test
  - Build
  - Smoke Test
- Prevents broken code from reaching production
- All 15 unit tests execute automatically

### Auto Deployment (Vercel)

- Vercel detects every push to `main`
- Automatically builds and deploys the application
- No manual deployment steps required
- Rollback available through Vercel dashboard

---

## 2. Collaboration

### Git Workflow

- All changes go through Pull Requests (PRs)
- Branch naming convention:
  - `feature/`
  - `bugfix/`
  - `hotfix/`
- PR template enforces:
  - Summary
  - Screenshots
  - Testing evidence
- Minimum of one reviewer required before merge

### Issue Tracking

- Bug reports managed through GitHub Issues
- Feature requests managed through GitHub Issues
- Issue templates ensure consistency
- Issues linked to PRs for traceability

### Documentation

- All technical decisions documented in `/docs`
- Weekly deliverables tracked in separate folders
- Backlog and sprint plans maintained throughout development

---

## 3. Monitoring

### Application Logging

- Custom logger implemented in `firebase.js`
- Supports:
  - INFO
  - ERROR
  - WARN
- Logs include timestamps
- Logs visible through browser DevTools console
- Firebase Console tracks database read/write operations

### Uptime Monitoring

- Smoke tests verify HTTP `200 OK` on every deployment
- Vercel dashboard provides deployment history
- Firebase Console monitors database activity

---

## 4. Feedback Loop

### Development Cycle

```text
Plan (Backlog)
      │
      ▼
Code (Feature Branch)
      │
      ▼
Test (Vitest + Manual)
      │
      ▼
Review (Pull Request)
      │
      ▼
Deploy (Vercel Auto)
      │
      ▼
Monitor (Console + Firebase)
      │
      ▼
Improve (Next Sprint)
```

### Cloud/DevOps Improvements Implemented

- Added GitHub Actions CI/CD pipeline for automated testing
- Added smoke tests to verify live deployment after every push
- Added GitHub environment secrets for secure builds
- Implemented structured logging for improved observability

---

## 5. Cloud Integration

| Service | Purpose |
|---|---|
| Firebase Firestore | NoSQL cloud database with auto-scaling |
| Firebase Auth | Managed authentication service |
| Vercel | Serverless deployment platform |
| GitHub Actions | Cloud-based CI/CD runner |

---

## DevOps Workflow Diagram

```text
Developer Pushes Code
          │
          ▼
    GitHub Repository
          │
          ▼
   GitHub Actions CI
(Test → Build → Smoke Test)
          │
          ▼
     Vercel Deployment
          │
          ▼
   Production Web App
          │
          ▼
 Monitoring & Logging
(Firebase + DevTools)
```

---

## Security and Reliability Practices

- Environment variables secured through GitHub Secrets
- Firebase Authentication protects admin access
- Automated testing before deployment
- Smoke testing validates production availability
- Rollback support through Vercel deployment history

---

## Summary

The Barangay Complaint System follows modern DevOps practices by automating testing and deployment, enforcing collaborative code reviews through Pull Requests, monitoring application health through logging and smoke tests, and maintaining a continuous feedback loop using sprint planning and iterative improvements.

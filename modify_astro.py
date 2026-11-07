import re

with open('aman-malviya-portfolio/src/pages/index.astro', 'r') as f:
    content = f.read()

# Update experience
new_experience = """const experience = [
  { period: 'Aug 2025 — Sep 2026', company: 'NIUM', role: 'Software Development Engineer I', place: 'Mumbai', bullets: [
    'Engineered core payment microservices with Java 17, Spring Boot, and AWS EKS (Kubernetes), orchestrating 100K+ daily transactions across 50+ global banking partners while maintaining 99.99%+ availability.',
    'Automated payment-validation pre-checks and routing rules, boosting transaction success rates by 15% and reducing manual operational intervention by 40%.',
    'Engineered fault-tolerant messaging using Amazon SQS redrive policies (maxReceiveCount tuned from 5 to 1) and Dead Letter Queue (DLQ) isolation, eliminating 80% of unproductive retry cycles.',
    'Built a Claude-powered Model Context Protocol (MCP) server unifying Grafana logs, DB diagnostics, and Bitbucket context, reducing production root-cause investigation time by 30%.',
    'Migrated banking partner reference data into a centralized Amazon Neptune (graph database) backed by Redis caching, simplifying partner onboarding and accelerating high-traffic routing lookups.'
  ]},
  { period: 'Apr 2025 — Aug 2025', company: 'Blacklight Studio', role: 'Associate Backend Developer (Contract)', place: 'Noida', bullets: [
    'Developed modular backend microservices and low-latency RESTful APIs using Java, Spring Boot, and Spring Data JPA (Hibernate) to power high-throughput core platform workflows.',
    'Redesigned API response serialization and implemented distributed Redis caching, reducing average API response latency from 200 ms to 50 ms (75% reduction).',
    'Optimized complex PostgreSQL/MySQL queries, composite indexing, and HikariCP connection pools; authored comprehensive unit/integration test suites using JUnit 5 and Mockito.'
  ]},
  { period: 'Oct 2024 — Feb 2025', company: 'Inorg (VivaOps)', role: 'Software Engineer (Internship)', place: 'Pune', bullets: [
    'Developed backend microservices using Java and Spring Boot, containerizing applications with Docker for orchestrated deployment on Kubernetes.',
    'Implemented automated Jenkins CI/CD pipelines integrated with Git webhooks and automated testing gates, reducing manual build and deployment effort by 70%.',
    'Provisioned cloud infrastructure across AWS (EC2, S3, RDS, VPC) using Terraform and Ansible, cutting environment setup time from 45 minutes to 5 minutes (89% reduction).'
  ]}
];"""

content = re.sub(r'const experience = \[.*?\];', new_experience, content, flags=re.DOTALL)

with open('aman-malviya-portfolio/src/pages/index.astro', 'w') as f:
    f.write(content)

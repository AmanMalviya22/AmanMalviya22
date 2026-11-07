import re

with open('aman-malviya-portfolio/src/pages/index.astro', 'r') as f:
    content = f.read()

# Update skillGroups
new_skillGroups = """const skillGroups = [
  { title: 'Languages', items: ['Java (17, 11, 8)', 'SQL', 'C++', 'JavaScript', 'Bash'] },
  { title: 'Java & Backend', items: ['Spring Boot', 'Spring MVC', 'Spring Data JPA', 'Hibernate', 'Spring Cloud', 'Spring Security', 'REST APIs', 'Multithreading'] },
  { title: 'Data & Messaging', items: ['PostgreSQL', 'MySQL', 'Amazon Neptune', 'MongoDB', 'Redis', 'Apache Kafka', 'Amazon SQS', 'RabbitMQ'] },
  { title: 'Cloud & DevOps', items: ['AWS', 'EKS', 'EC2', 'RDS', 'S3', 'VPC', 'Docker', 'Kubernetes', 'Jenkins', 'Terraform', 'Linux'] },
  { title: 'Testing & Tools', items: ['JUnit 5', 'Mockito', 'Git', 'Bitbucket', 'Maven', 'Gradle', 'Postman', 'Grafana'] },
  { title: 'AI Engineering', items: ['Claude API', 'MCP', 'LLM Integration', 'Prompt Engineering', 'Agile/Scrum'] }
];"""

content = re.sub(r'const skillGroups = \[.*?\];', new_skillGroups, content, flags=re.DOTALL)

with open('aman-malviya-portfolio/src/pages/index.astro', 'w') as f:
    f.write(content)

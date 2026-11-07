import re

with open('aman-malviya-portfolio/src/pages/index.astro', 'r') as f:
    content = f.read()

# Replace the projects array with the new one containing SlotMind
new_projects = """const projects = [
  {
    title: 'SlotMind — AI-Powered Event-Driven Appointment Re-Scheduling Engine',
    type: 'SOLO PROJECT',
    company: 'Cleared Zycus Hackathon Evaluation',
    text: 'Architected a scalable appointment rescheduling engine to automate schedule recovery when providers go offline.',
    tags: ['Java 17', 'Spring Boot 3', 'Apache Kafka', 'Redis', 'PostgreSQL', 'LLM'],
    source: 'https://github.com/AmanMalviya22/SlotMind',
    sourceLabel: 'View on GitHub',
    problem: 'Managing appointment and slot lifecycles manually when providers go offline causes scheduling conflicts.',
    approach: 'Designed a pluggable Strategy Pattern engine combining nearest-slot heuristics with LLM recommendations. Validated AI outputs against live Redis availability with automated fallback. Used Kafka for async event processing and PostgreSQL pessimistic locking.',
    outcome: 'Eliminated race-condition double-booking and prevented duplicate notifications.'
  },
  {
    title: 'MCP Server — AI-Powered Root-Cause Analysis',
    type: 'INTERNAL TOOLING',
    company: 'NIUM',
    text: 'A Claude-powered MCP server that connected transaction context with database logs and diagnostics to help engineers investigate payment failures.',
    tags: ['Java','Spring Boot','MCP','Claude API','SQL'],
    problem: 'Investigating transaction failures required engineers to gather relevant transaction context, database records, and operational diagnostics.',
    approach: 'Built focused MCP tools to expose investigation context to Claude for structured root-cause analysis.',
    outcome: 'Reduced root-cause investigation time by approximately 30%. Internal company work; implementation details are summarized for confidentiality.',
    workflow: ['Payment failure context', 'Database logs and diagnostics', 'Claude-assisted analysis', 'RCA summary']
  },
  {
    title: 'Banking Reference Data Graph',
    type: 'DATA PLATFORM',
    company: 'NIUM',
    text: 'Migrated SWIFT, IFSC, and bank-code reference data into a centralized graph-based system to simplify configuration.',
    tags: ['Java','Amazon Neptune','Microservices','Redis'],
    problem: 'SWIFT, IFSC, and bank-code reference data needed repeated maintenance across application configuration.',
    approach: 'Moved reference data into a centralized Amazon Neptune graph database backed by Redis caching.',
    outcome: 'Reduced configuration complexity, simplified partner onboarding, and accelerated routing lookups.'
  }
];"""

content = re.sub(r'const projects = \[.*?\];\n---', new_projects + '\n---', content, flags=re.DOTALL)

with open('aman-malviya-portfolio/src/pages/index.astro', 'w') as f:
    f.write(content)

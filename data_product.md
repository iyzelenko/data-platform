# Academic Performance Data Product

## Domain
academic_performance

## Description
Student academic metrics and engagement events.

## Sources
- LMS API
- CSV exports
- Kafka streaming events

## SLA
Daily refresh.

## Quality Metrics
- No duplicate student_id
- grade range 0-100
- attendance range 0-100

## Consumers
- Analytics dashboards
- ML models
- Reporting systems
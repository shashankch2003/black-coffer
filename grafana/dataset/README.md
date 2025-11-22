# Cloud Billing & System Utilization Dashboard

A real-time cloud cost monitoring and resource utilization analytics dashboard built with Grafana, visualizing ₹1.7M+ in cloud infrastructure spending across multiple services and regions.

![Dashboard Preview](./screenshots/dashboard-overview Overview

This project demonstrates advanced data visualization and cloud cost optimization skills by creating an interactive Grafana dashboard that provides actionable insights into cloud billing patterns, resource utilization, and cost drivers.

**Live Demo:** `http://localhost:3000` (when running locally)

## 🎯 Business Value

- **Real-time Cost Monitoring:** Track cloud spending across 9 services and 6 geographic regions
- **Cost Optimization:** Identify the top cost drivers (Cloud Dataproc: 24% of total costs)
- **Resource Efficiency:** Monitor CPU/Memory utilization trends (65-85% average)
- **Budget Planning:** Analyze ₹150K-₹180K monthly spending patterns
- **Data-Driven Decisions:** Visual insights for infrastructure optimization

## 🏗️ Architecture

```
┌─────────────────┐
│   CSV Dataset   │ (10,000+ billing records)
│  (Kaggle Data)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Infinity Plugin│ (Data Source)
│   CSV Parser    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Grafana      │ (Dockerized)
│   Dashboard     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  6 Visualization│
│     Panels      │
└─────────────────┘
```

## 📈 Dashboard Features

### Visualization Panels (6 Total)

1. **Service Cost Distribution (% of Total)** - Pie Chart
   - Shows percentage breakdown of costs by service
   - Identifies Cloud Dataproc as top cost driver (24%)

2. **Total Monthly Cloud Cost (₹)** - Bar Chart
   - Tracks monthly spending trends from Jan-Oct
   - Reveals stable ₹150K-₹180K monthly costs

3. **Cloud Costs by Service (Bar Chart)** - Detailed Breakdown
   - Cloud Dataproc: ₹415,332
   - Pub/Sub: ₹390,930
   - BigQuery, Cloud Endpoints, Cloud Scanner, etc.

4. **Cloud Costs by Region (High→Low)** - Geographic Analysis
   - US-East: ₹285,000 (highest)
   - Europe: ₹195,000
   - Asia-Pacific, US-West, Canada, Australia

5. **CPU & Memory Utilization Trends (%)** - Resource Monitoring
   - Dual-axis visualization (CPU in green, Memory in yellow)
   - Consistent 65-85% utilization across months

6. **Top Resource IDs by Cost** - Resource-Level Analysis
   - Identifies most expensive individual resources
   - Enables targeted optimization efforts

## 🔧 Tech Stack

- **Grafana**: v11+ (Data Visualization Platform)
- **Docker**: Containerization
- **Infinity Plugin**: CSV data source connector
- **Dataset**: Real cloud billing data from Kaggle (GCP cost data)
- **Data Format**: CSV (10,000+ records)
- **Date Range**: August 2024 - November 2025

## 🚀 Quick Start

### Prerequisites

- Docker Desktop installed
- 4GB+ RAM available
- Port 3000 available

### Installation

```bash
# 1. Create data directory
mkdir -p C:/grafana-data
# Place your CSV file: cloud_billing_data.csv

# 2. Run Grafana container
docker run -d \
  --name grafana \
  -p 3000:3000 \
  -v C:/grafana-data:/var/lib/grafana/csvfiles \
  -e "GF_INSTALL_PLUGINS=yesoreyeram-infinity-datasource" \
  grafana/grafana

# 3. Access Grafana
# Open browser: http://localhost:3000
# Login: admin / admin
```

### Dashboard Setup

```bash
# 1. Configure Infinity Data Source
# - Go to Configuration → Data Sources
# - Add "Infinity" data source
# - Type: CSV
# - File Path: /var/lib/grafana/csvfiles/cloud_billing_data.csv

# 2. Import Dashboard
# - Go to Dashboards → Import
# - Upload: dashboard.json (from this repo)
# - Select "Cloud Billing CSV" as data source
```

## 📊 Key Insights Generated

### Cost Analysis
- **Total Cloud Spending:** ₹1,700,000+ (annual projection)
- **Average Monthly Cost:** ₹155,000
- **Top Cost Driver:** Cloud Dataproc (24% = ₹415K)
- **Most Expensive Region:** US-East (₹285K)

### Resource Utilization
- **Average CPU Utilization:** 70-75%
- **Average Memory Utilization:** 75-80%
- **Resource Efficiency:** Stable and well-optimized

### Optimization Opportunities
1. Review Cloud Dataproc usage for potential savings
2. Consolidate resources in US-East region
3. Monitor Pub/Sub costs (2nd highest at ₹390K)
4. Implement cost alerts for budget overruns

## 📁 Project Structure

```
grafana-cloud-dashboard/
│
├── README.md                 # This file
├── dashboard.json            # Grafana dashboard export
├── docker-compose.yml        # Docker setup (optional)
│
├── data/
│   └── sample_data.csv       # Sample dataset (anonymized)
│
├── screenshots/
│   ├── dashboard-overview.png
│   ├── service-distribution.png
│   ├── cost-trends.png
│   └── utilization-metrics.png
│
└── docs/
    ├── SETUP.md              # Detailed setup guide
    └── INSIGHTS.md           # Business insights report
```

## 🎓 Skills Demonstrated

- **Data Visualization:** Advanced Grafana dashboard design
- **Cloud Cost Optimization:** Cost analysis and optimization strategies
- **Docker & Containerization:** Production-grade deployment
- **Data Engineering:** ETL pipeline from CSV to visualizations
- **Business Intelligence:** Actionable insights from raw data
- **DevOps:** Infrastructure as Code principles

## 🔍 Use Cases

- **Cloud Cost Management Teams:** Monitor and optimize cloud spending
- **Finance Departments:** Budget planning and forecasting
- **DevOps Engineers:** Resource utilization tracking
- **C-Level Executives:** High-level spending overviews
- **Data Analysts:** Ad-hoc cost analysis and reporting

## 📈 Future Enhancements

- [ ] Add alerting rules for cost threshold breaches
- [ ] Implement cost forecasting with trend analysis
- [ ] Create drill-down panels for detailed investigation
- [ ] Add real-time data integration (Prometheus/CloudWatch)
- [ ] Build comparative analysis (month-over-month, year-over-year)
- [ ] Integrate with Slack/Email for automated reports

## 🤝 Contributing

This is a portfolio project. Feedback and suggestions are welcome!

## 📝 License

MIT License - Feel free to use this project for learning and portfolio purposes.

## 👤 Author

**Your Name**
- Role: Associate Data Scientist @ Black Coffer
- Education: B.Tech, CBIT Hyderabad
- LinkedIn: [Your Profile]
- GitHub: [Your Profile]
- Portfolio: [Your Website]

## 🙏 Acknowledgments

- Dataset: Kaggle GCP Billing Data
- Tool: Grafana Labs
- Community: Grafana Community Forums
- Company: Black Coffer (Training Project)


**Built with ❤️ for cloud cost optimization and data visualization excellence**

**Tags:** `grafana` `data-visualization` `cloud-cost-optimization` `docker` `dashboard` `business-intelligence` `devops` `portfolio-project`

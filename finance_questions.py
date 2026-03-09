Question_Bank = {
  "domain": "Financial Services",
  "sections": {
    "Infrastructure & Security": [
      {
        "id": "FIN_INF_01",
        "dimension": "Infrastructure & Security",
        "question": "What percentage of core banking/transaction systems are modernized?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "<30%", "score": 0, "risk_level": "Critical" },
          { "label": "30–60%", "score": 1, "risk_level": "High" },
          { "label": "60–90%", "score": 2, "risk_level": "Medium" },
          { "label": ">90%", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "FIN_INF_02",
        "dimension": "Infrastructure & Security",
        "question": "Do you use AI for real-time fraud detection?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "Planning", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_INF_03",
        "dimension": "Infrastructure & Security",
        "question": "How often do you conduct penetration testing on AI systems?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Monthly", "score": 3, "risk_level": "Low" },
          { "label": "Quarterly", "score": 2, "risk_level": "Medium" },
          { "label": "Annually", "score": 1, "risk_level": "High" },
          { "label": "Ad hoc", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_INF_04",
        "dimension": "Infrastructure & Security",
        "question": "Is your infrastructure compliant with PCI DSS and SWIFT CSP?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 1, "risk_level": "High" },
          { "label": "Not sure", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_INF_05",
        "dimension": "Infrastructure & Security",
        "question": "Do you have dedicated AI security monitoring?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In progress", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "Cloud & Data Governance": [
      {
        "id": "FIN_CDG_01",
        "dimension": "Cloud & Data Governance",
        "question": "Are you using AI-driven cloud cost optimization?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_CDG_02",
        "dimension": "Cloud & Data Governance",
        "question": "Do you have a federated data strategy for a customer 360 view?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "Planning", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_CDG_03",
        "dimension": "Cloud & Data Governance",
        "question": "How mature is your real-time data streaming infrastructure?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Advanced", "score": 3, "risk_level": "Low" },
          { "label": "Moderate", "score": 2, "risk_level": "Medium" },
          { "label": "Early", "score": 1, "risk_level": "High" },
          { "label": "None", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_CDG_04",
        "dimension": "Cloud & Data Governance",
        "question": "Do you use synthetic data for AI model training?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Occasionally", "score": 2, "risk_level": "Medium" },
          { "label": "Evaluating", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_CDG_05",
        "dimension": "Cloud & Data Governance",
        "question": "Have you implemented data masking for non-production environments?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 3, "risk_level": "Low" },
          { "label": "Partially", "score": 2, "risk_level": "Medium" },
          { "label": "Minimally", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "AI Adoption & Use Cases": [
      {
        "id": "FIN_AI_01",
        "dimension": "AI Adoption & Use Cases",
        "question": "Which AI use cases are currently in production?",
        "risk_weight": 2,
        "selection_type": "multi",
        "options": [
          { "label": "Credit scoring & underwriting", "score": 1, "risk_level": "Low" },
          { "label": "Algorithmic trading", "score": 1, "risk_level": "Low" },
          { "label": "Anti-money laundering (AML)", "score": 1, "risk_level": "Low" },
          { "label": "Customer service chatbots", "score": 1, "risk_level": "Low" },
          { "label": "Personalized wealth management", "score": 1, "risk_level": "Low" },
          { "label": "Regulatory reporting automation", "score": 1, "risk_level": "Low" },
          { "label": "Document processing (KYC)", "score": 1, "risk_level": "Low" }
        ]
      },
      {
        "id": "FIN_AI_02",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using generative AI for investment research?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" },
          { "label": "Not permitted", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_AI_03",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you have AI-powered risk management systems?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_AI_04",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using computer vision for branch operations?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_AI_05",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you offer AI-driven advisory services?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In development", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      }
    ],

    "Workforce & Culture": [
      {
        "id": "FIN_WRK_01",
        "dimension": "Workforce & Culture",
        "question": "What percentage of your workforce uses AI tools daily?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "<20%", "score": 0, "risk_level": "High" },
          { "label": "20–40%", "score": 1, "risk_level": "Medium" },
          { "label": "40–60%", "score": 2, "risk_level": "Low" },
          { "label": ">60%", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "FIN_WRK_02",
        "dimension": "Workforce & Culture",
        "question": "Do you have a Chief AI Officer or equivalent?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_WRK_03",
        "dimension": "Workforce & Culture",
        "question": "Are compliance officers trained on AI model validation?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 1, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_WRK_04",
        "dimension": "Workforce & Culture",
        "question": "Do you incentivize AI innovation through internal hackathons?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Occasionally", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_WRK_05",
        "dimension": "Workforce & Culture",
        "question": "Is there a defined career path for AI/ML specialists?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Informal", "score": 1, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      }
    ],

    "Compliance & Regulatory": [
      {
        "id": "FIN_COM_01",
        "dimension": "Compliance & Regulatory",
        "question": "Are your AI models explainable to regulators?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 3, "risk_level": "Low" },
          { "label": "Partially", "score": 2, "risk_level": "Medium" },
          { "label": "Minimally", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_COM_02",
        "dimension": "Compliance & Regulatory",
        "question": "Do you conduct fair lending bias testing on AI credit models?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Always", "score": 3, "risk_level": "Low" },
          { "label": "Occasionally", "score": 2, "risk_level": "Medium" },
          { "label": "Rarely", "score": 1, "risk_level": "High" },
          { "label": "Never", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_COM_03",
        "dimension": "Compliance & Regulatory",
        "question": "Are you compliant with the EU AI Act (if applicable)?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In progress", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Not applicable", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "FIN_COM_04",
        "dimension": "Compliance & Regulatory",
        "question": "Do you maintain a model risk management (MRM) framework for AI?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In development", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_COM_05",
        "dimension": "Compliance & Regulatory",
        "question": "How do you handle AI model versioning for audit trails?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Automated", "score": 3, "risk_level": "Low" },
          { "label": "Manual", "score": 1, "risk_level": "Medium" },
          { "label": "Inconsistent", "score": 1, "risk_level": "High" },
          { "label": "No versioning", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "ROI & Scaling": [
      {
        "id": "FIN_ROI_01",
        "dimension": "ROI & Scaling",
        "question": "What is your ROI timeline for AI investments?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "<1 year", "score": 3, "risk_level": "Low" },
          { "label": "1–2 years", "score": 2, "risk_level": "Medium" },
          { "label": "2–3 years", "score": 1, "risk_level": "High" },
          { "label": ">3 years", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_ROI_02",
        "dimension": "ROI & Scaling",
        "question": "What is your biggest barrier to scaling AI?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Regulatory uncertainty", "score": 1, "risk_level": "High" },
          { "label": "Legacy infrastructure", "score": 1, "risk_level": "High" },
          { "label": "Talent shortage", "score": 1, "risk_level": "High" },
          { "label": "Executive sponsorship", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "FIN_ROI_03",
        "dimension": "ROI & Scaling",
        "question": "Do you have standardized AI deployment pipelines?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_ROI_04",
        "dimension": "ROI & Scaling",
        "question": "Are AI initiatives tied to measurable KPIs?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "FIN_ROI_05",
        "dimension": "ROI & Scaling",
        "question": "Do you use AI performance dashboards for management?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Limited", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      }
    ]
  }
}

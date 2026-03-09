Question_Bank = {
  "domain": "Government & Public Sector",
  
  "sections": {

    "Infrastructure & Security": [
      {
        "id": "GOV_INF_01",
        "dimension": "Infrastructure & Security",
        "question": "What percentage of your critical systems are legacy or mainframe-based?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "More than 75%", "score": 0, "risk_level": "Critical" },
          { "label": "50–75%", "score": 1, "risk_level": "High" },
          { "label": "25–50%", "score": 2, "risk_level": "Medium" },
          { "label": "Less than 25%", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_INF_02",
        "dimension": "Infrastructure & Security",
        "question": "Do you have dedicated security operations for citizen data protection?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "Critical" },
          { "label": "Partial", "score": 1, "risk_level": "High" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_INF_03",
        "dimension": "Infrastructure & Security",
        "question": "How often do you conduct cybersecurity audits?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Ad hoc", "score": 0, "risk_level": "High" },
          { "label": "Biannually", "score": 1, "risk_level": "Medium" },
          { "label": "Annually", "score": 2, "risk_level": "Low" },
          { "label": "Quarterly", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_INF_04",
        "dimension": "Infrastructure & Security",
        "question": "Are your systems interoperable across different government departments?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Minimally", "score": 1, "risk_level": "Medium" },
          { "label": "Partially", "score": 2, "risk_level": "Low" },
          { "label": "Fully", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_INF_05",
        "dimension": "Infrastructure & Security",
        "question": "Do you have a government-wide AI infrastructure roadmap?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "In development", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      }
    ],

    "Cloud & Data Governance": [
      {
        "id": "GOV_DATA_01",
        "dimension": "Cloud & Data Governance",
        "question": "Are you using hybrid or multi-cloud for citizen services?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_DATA_02",
        "dimension": "Cloud & Data Governance",
        "question": "What percentage of citizen data is encrypted at rest and in transit?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Less than 50%", "score": 0, "risk_level": "Critical" },
          { "label": "50–75%", "score": 1, "risk_level": "High" },
          { "label": "75–90%", "score": 2, "risk_level": "Medium" },
          { "label": "More than 90%", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_DATA_03",
        "dimension": "Cloud & Data Governance",
        "question": "Do you have a centralized data governance policy across departments?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "Critical" },
          { "label": "In progress", "score": 1, "risk_level": "High" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_DATA_04",
        "dimension": "Cloud & Data Governance",
        "question": "How mature is your open data initiative?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "None", "score": 0, "risk_level": "High" },
          { "label": "Early", "score": 1, "risk_level": "Medium" },
          { "label": "Moderate", "score": 2, "risk_level": "Low" },
          { "label": "Advanced", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_DATA_05",
        "dimension": "Cloud & Data Governance",
        "question": "Have you implemented data localization policies for sensitive citizen data?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "Critical" },
          { "label": "Partial", "score": 1, "risk_level": "High" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      }
    ],

    "AI Adoption & Use Cases": [
      {
        "id": "GOV_AI_01",
        "dimension": "AI Adoption & Use Cases",
        "question": "Which AI use cases are you currently deploying?",
        "risk_weight": 2,
        "selection_type": "multi",
        "options": [
          { "label": "Citizen chatbots", "score": 1, "risk_level": "Low" },
          { "label": "Fraud detection", "score": 1, "risk_level": "Low" },
          { "label": "Emergency response optimization", "score": 1, "risk_level": "Low" },
          { "label": "Predictive analytics", "score": 1, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_AI_02",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using AI for emergency response optimization?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Pilot", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_AI_03",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you have an AI ethics board for public sector applications?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "Critical" },
          { "label": "Planning", "score": 1, "risk_level": "High" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_AI_04",
        "dimension": "AI Adoption & Use Cases",
        "question": "How mature is your citizen-facing AI service delivery?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "None", "score": 0, "risk_level": "High" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "Pilot", "score": 2, "risk_level": "Low" },
          { "label": "Scaled", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_AI_05",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using computer vision for public infrastructure monitoring?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Pilot", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      }
    ],

    "Workforce & Culture": [
      {
        "id": "GOV_WRK_01",
        "dimension": "Workforce & Culture",
        "question": "What percentage of government employees have received AI literacy training?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Less than 20%", "score": 0, "risk_level": "High" },
          { "label": "20–40%", "score": 1, "risk_level": "Medium" },
          { "label": "40–60%", "score": 2, "risk_level": "Low" },
          { "label": "More than 60%", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_WRK_02",
        "dimension": "Workforce & Culture",
        "question": "Do you have a dedicated AI Center of Excellence?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_WRK_03",
        "dimension": "Workforce & Culture",
        "question": "Are procurement teams trained on AI vendor evaluation?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Partial", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_WRK_04",
        "dimension": "Workforce & Culture",
        "question": "Is there resistance to AI adoption from public sector unions?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "High", "score": 0, "risk_level": "High" },
          { "label": "Moderate", "score": 1, "risk_level": "Medium" },
          { "label": "Low", "score": 2, "risk_level": "Low" },
          { "label": "None", "score": 3, "risk_level": "Very Low" }
        ]
      },
      {
        "id": "GOV_WRK_05",
        "dimension": "Workforce & Culture",
        "question": "Do you offer digital upskilling programs for civil servants?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      }
    ],

    "Compliance & Regulatory": [
      {
        "id": "GOV_COM_01",
        "dimension": "Compliance & Regulatory",
        "question": "Do you have an AI-specific procurement framework?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "Critical" },
          { "label": "In development", "score": 1, "risk_level": "High" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_COM_02",
        "dimension": "Compliance & Regulatory",
        "question": "How prepared are you for emerging AI regulations?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Not prepared", "score": 0, "risk_level": "Critical" },
          { "label": "Slightly prepared", "score": 1, "risk_level": "High" },
          { "label": "Moderately prepared", "score": 2, "risk_level": "Medium" },
          { "label": "Very prepared", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_COM_03",
        "dimension": "Compliance & Regulatory",
        "question": "Do you conduct algorithmic bias audits for citizen-facing AI?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Never", "score": 0, "risk_level": "Critical" },
          { "label": "Rarely", "score": 1, "risk_level": "High" },
          { "label": "Occasionally", "score": 2, "risk_level": "Medium" },
          { "label": "Always", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_COM_04",
        "dimension": "Compliance & Regulatory",
        "question": "Is there a designated Chief AI Ethics Officer?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Planned", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_COM_05",
        "dimension": "Compliance & Regulatory",
        "question": "Do you publish AI transparency reports?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Ad hoc", "score": 1, "risk_level": "Medium" },
          { "label": "Annually", "score": 2, "risk_level": "Low" },
          { "label": "Quarterly", "score": 3, "risk_level": "Very Low" }
        ]
      }
    ],

    "ROI & Scaling": [
      {
        "id": "GOV_ROI_01",
        "dimension": "ROI & Scaling",
        "question": "Do you measure citizen satisfaction improvements from AI services?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Planning", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_ROI_02",
        "dimension": "ROI & Scaling",
        "question": "What is your biggest barrier to scaling government AI?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "Budget constraints", "score": 1, "risk_level": "Medium" },
          { "label": "Legacy procurement rules", "score": 1, "risk_level": "Medium" },
          { "label": "Privacy concerns", "score": 1, "risk_level": "Medium" },
          { "label": "Workforce skills", "score": 1, "risk_level": "Medium" },
          { "label": "Political will", "score": 1, "risk_level": "Medium" }
        ]
      },
      {
        "id": "GOV_ROI_03",
        "dimension": "ROI & Scaling",
        "question": "Have you achieved cost savings from AI automation?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Partial", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_ROI_04",
        "dimension": "ROI & Scaling",
        "question": "Do you have metrics to track AI project scalability?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Partial", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      },
      {
        "id": "GOV_ROI_05",
        "dimension": "ROI & Scaling",
        "question": "Are lessons learned from AI pilots reused across departments?",
        "risk_weight": 1,
        "selection_type": "single",
        "options": [
          { "label": "No", "score": 0, "risk_level": "High" },
          { "label": "Partially", "score": 1, "risk_level": "Medium" },
          { "label": "Yes", "score": 3, "risk_level": "Low" }
        ]
      }
    ]

  }
}

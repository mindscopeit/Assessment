Question_Bank = {
  "domain": "Insurance",
  "sections": {

    "Infrastructure & Security": [

      {
        "id": "INS_INF_01",
        "dimension": "Infrastructure & Security",
        "question": "Are your policy administration systems modernized?",
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
        "id": "INS_INF_02",
        "dimension": "Infrastructure & Security",
        "question": "Do you use AI for claims fraud detection?",
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
        "id": "INS_INF_03",
        "dimension": "Infrastructure & Security",
        "question": "Is your claims processing infrastructure API-first?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Partial", "score": 1, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_INF_04",
        "dimension": "Infrastructure & Security",
        "question": "Do you have real-time underwriting capabilities?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Limited", "score": 2, "risk_level": "Medium" },
          { "label": "Planning", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_INF_05",
        "dimension": "Infrastructure & Security",
        "question": "How secure are your third-party Insurtech integrations?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Very secure", "score": 3, "risk_level": "Low" },
          { "label": "Moderately secure", "score": 2, "risk_level": "Medium" },
          { "label": "Slightly secure", "score": 1, "risk_level": "High" },
          { "label": "Unknown", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "Cloud & Data Governance": [

      {
        "id": "INS_CDG_01",
        "dimension": "Cloud & Data Governance",
        "question": "Do you use cloud-native insurance platforms?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Migration in progress", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_CDG_02",
        "dimension": "Cloud & Data Governance",
        "question": "Are you leveraging IoT/telematics data for pricing?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_CDG_03",
        "dimension": "Cloud & Data Governance",
        "question": "Do you have a unified customer data platform?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In progress", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_CDG_04",
        "dimension": "Cloud & Data Governance",
        "question": "How mature is your usage-based insurance (UBI) data infrastructure?",
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
        "id": "INS_CDG_05",
        "dimension": "Cloud & Data Governance",
        "question": "Do you use external data sources for underwriting?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes, integrated", "score": 3, "risk_level": "Low" },
          { "label": "Yes, manual", "score": 2, "risk_level": "Medium" },
          { "label": "Occasionally", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "AI Adoption & Use Cases": [

      {
        "id": "INS_AI_01",
        "dimension": "AI Adoption & Use Cases",
        "question": "Which AI use cases are you deploying?",
        "risk_weight": 2,
        "selection_type": "multi",
        "options": [
          { "label": "Automated claims adjudication", "score": 1, "risk_level": "Low" },
          { "label": "Telematics-based pricing", "score": 1, "risk_level": "Low" },
          { "label": "Health/life risk assessment", "score": 1, "risk_level": "Low" },
          { "label": "Policy recommendation engines", "score": 1, "risk_level": "Low" },
          { "label": "Churn prediction", "score": 1, "risk_level": "Low" },
          { "label": "Subrogation automation", "score": 1, "risk_level": "Low" },
          { "label": "Underwriting workbench", "score": 1, "risk_level": "Low" }
        ]
      },
      {
        "id": "INS_AI_02",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using computer vision for damage assessment?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "Evaluating", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_AI_03",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you use NLP for claims intake processing?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_AI_04",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you leveraging predictive analytics for customer lifetime value?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In development", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_AI_05",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you offer AI-powered virtual claims assistants?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Beta", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      }
    ],

    "Workforce & Culture": [

      {
        "id": "INS_WRK_01",
        "dimension": "Workforce & Culture",
        "question": "What percentage of underwriters use AI decision support tools?",
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
        "id": "INS_WRK_02",
        "dimension": "Workforce & Culture",
        "question": "Do you have actuarial staff trained in machine learning?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Many", "score": 3, "risk_level": "Low" },
          { "label": "Some", "score": 2, "risk_level": "Medium" },
          { "label": "Few", "score": 1, "risk_level": "High" },
          { "label": "None", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_WRK_03",
        "dimension": "Workforce & Culture",
        "question": "Are claims adjusters using AI for workflow prioritization?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Pilot", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_WRK_04",
        "dimension": "Workforce & Culture",
        "question": "Do you have a culture of experimentation with Insurtech?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Strong", "score": 3, "risk_level": "Low" },
          { "label": "Moderate", "score": 2, "risk_level": "Medium" },
          { "label": "Weak", "score": 1, "risk_level": "High" },
          { "label": "None", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_WRK_05",
        "dimension": "Workforce & Culture",
        "question": "Is there AI upskilling for legacy workforce?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes, formal", "score": 3, "risk_level": "Low" },
          { "label": "Yes, informal", "score": 2, "risk_level": "Medium" },
          { "label": "Minimal", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "Compliance & Regulatory": [

      {
        "id": "INS_COM_01",
        "dimension": "Compliance & Regulatory",
        "question": "Are your pricing models compliant with unisex/gender regulations?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 3, "risk_level": "Low" },
          { "label": "Partially", "score": 2, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Low" },
          { "label": "Not sure", "score": 0, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_COM_02",
        "dimension": "Compliance & Regulatory",
        "question": "Do you conduct bias audits for underwriting models?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Regularly", "score": 3, "risk_level": "Low" },
          { "label": "Occasionally", "score": 2, "risk_level": "Medium" },
          { "label": "Rarely", "score": 1, "risk_level": "High" },
          { "label": "Never", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_COM_03",
        "dimension": "Compliance & Regulatory",
        "question": "Are you compliant with Solvency II AI requirements (EU)?",
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
        "id": "INS_COM_04",
        "dimension": "Compliance & Regulatory",
        "question": "Do you maintain model governance for actuarial AI?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "In development", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_COM_05",
        "dimension": "Compliance & Regulatory",
        "question": "How transparent are your AI-driven pricing decisions?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Fully transparent", "score": 3, "risk_level": "Low" },
          { "label": "Partially transparent", "score": 2, "risk_level": "Medium" },
          { "label": "Minimally transparent", "score": 1, "risk_level": "High" },
          { "label": "Not transparent", "score": 0, "risk_level": "Critical" }
        ]
      }
    ],

    "ROI & Scaling": [

      {
        "id": "INS_ROI_01",
        "dimension": "ROI & Scaling",
        "question": "What is your combined ratio trend since AI adoption?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Improved", "score": 3, "risk_level": "Low" },
          { "label": "Stable", "score": 2, "risk_level": "Medium" },
          { "label": "Worsened", "score": 0, "risk_level": "High" },
          { "label": "Not tracked", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_ROI_02",
        "dimension": "ROI & Scaling",
        "question": "What is your biggest barrier to scaling insurance AI?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Data silos", "score": 1, "risk_level": "High" },
          { "label": "Regulatory constraints", "score": 1, "risk_level": "High" },
          { "label": "Legacy systems", "score": 1, "risk_level": "High" },
          { "label": "Talent gap", "score": 1, "risk_level": "High" },
          { "label": "Customer trust", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "INS_ROI_03",
        "dimension": "ROI & Scaling",
        "question": "Do you track loss ratio improvement from AI fraud detection?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes, quantified", "score": 3, "risk_level": "Low" },
          { "label": "Yes, estimated", "score": 2, "risk_level": "Medium" },
          { "label": "Too early", "score": 1, "risk_level": "High" },
          { "label": "No", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_ROI_04",
        "dimension": "ROI & Scaling",
        "question": "How many AI use cases have moved from pilot to production?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": ">10", "score": 3, "risk_level": "Low" },
          { "label": "5–10", "score": 2, "risk_level": "Medium" },
          { "label": "1–5", "score": 1, "risk_level": "High" },
          { "label": "0", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "INS_ROI_05",
        "dimension": "ROI & Scaling",
        "question": "Do you have a dedicated AI innovation budget?",
        "risk_weight": 2,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 3, "risk_level": "Low" },
          { "label": "Intermittent", "score": 1, "risk_level": "Medium" },
          { "label": "No", "score": 0, "risk_level": "High" }
        ]
      }
    ]
  }
}

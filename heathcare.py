Question_Bank= {
  "domain": "Heathcare",
  "sections": {
    "Infrastructure & Security": [
      {
        "id": "PH_A_01",
        "dimension": "Infrastructure & Security",
        "question": "Is your R&D data infrastructure cloud enabled?",
        "risk_weight": 5,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 4, "risk_level": "Low" },
          { "label": "Partially", "score": 3, "risk_level": "Medium" },
          { "label": "Minimally", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_A_02",
        "dimension": "Infrastructure & Security",
        "question": "Do you use AI for drug discovery pipelines?",
        "risk_weight": 5,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "Evaluating", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_A_03",
        "dimension": "Infrastructure & Security",
        "question": "Are your clinical trial systems GxP validated for AI?",
        "risk_weight": 5,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In process", "score": 3, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_A_04",
        "dimension": "Infrastructure & Security",
        "question": "Do you have secure research collaboration platforms?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Limited", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_A_05",
        "dimension": "Infrastructure & Security",
        "question": "Is your genomic data infrastructure ready?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Partial", "score": 3, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      }
    ],

    "Cloud & Data Governance": [
      {
        "id": "PH_B_06",
        "dimension": "Cloud & Data Governance",
        "question": "Do you use secure research environments (SREs) for data sharing?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In development", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_B_07",
        "dimension": "Cloud & Data Governance",
        "question": "How mature is your real world evidence (RWE) data platform?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Advanced", "score": 4, "risk_level": "Low" },
          { "label": "Moderate", "score": 3, "risk_level": "Medium" },
          { "label": "Early", "score": 2, "risk_level": "High" },
          { "label": "None", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_B_08",
        "dimension": "Cloud & Data Governance",
        "question": "Do you have a FAIR data strategy?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In progress", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" },
          { "label": "What's FAIR?", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_B_09",
        "dimension": "Cloud & Data Governance",
        "question": "Are you using federated learning for multisite research?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "Evaluating", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_B_10",
        "dimension": "Cloud & Data Governance",
        "question": "Do you have standardized ontologies across research data?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 4, "risk_level": "Low" },
          { "label": "Partially", "score": 3, "risk_level": "Medium" },
          { "label": "Minimally", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      }
    ],

    "AI Adoption & Use Cases": [
      {
        "id": "PH_C_11",
        "dimension": "AI Adoption & Use Cases",
        "question": "Which AI use cases are you deploying?",
        "risk_weight": 5,
        "selection_type": "multi",
        "options": [
          { "label": "Target identification", "score": 1, "risk_level": "Low" },
          { "label": "Molecule generation", "score": 1, "risk_level": "Low" },
          { "label": "Clinical trial optimization", "score": 1, "risk_level": "Low" },
          { "label": "Patient recruitment", "score": 1, "risk_level": "Low" },
          { "label": "Medical imaging analysis", "score": 1, "risk_level": "Low" },
          { "label": "Real world evidence analysis", "score": 1, "risk_level": "Low" },
          { "label": "Manufacturing process optimization", "score": 1, "risk_level": "Low" },
          { "label": "Regulatory writing automation", "score": 1, "risk_level": "Low" }
        ]
      },
      {
        "id": "PH_C_12",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you using generative AI for novel protein design?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Research", "score": 3, "risk_level": "Medium" },
          { "label": "Evaluating", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_C_13",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you use AI for adverse event detection?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_C_14",
        "dimension": "AI Adoption & Use Cases",
        "question": "Are you applying AI to biomarker discovery?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_C_15",
        "dimension": "AI Adoption & Use Cases",
        "question": "Do you use computer vision for pathology slides?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      }
    ],

    "Workforce & Culture": [
      {
        "id": "PH_D_16",
        "dimension": "Workforce & Culture",
        "question": "What percentage of research scientists use AI tools?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "<20%", "score": 1, "risk_level": "Critical" },
          { "label": "20-40%", "score": 2, "risk_level": "High" },
          { "label": "40-60%", "score": 3, "risk_level": "Medium" },
          { "label": ">60%", "score": 4, "risk_level": "Low" }
        ]
      },
      {
        "id": "PH_D_17",
        "dimension": "Workforce & Culture",
        "question": "Do you have computational biologists or AI researchers on staff?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Many", "score": 4, "risk_level": "Low" },
          { "label": "Some", "score": 3, "risk_level": "Medium" },
          { "label": "Few", "score": 2, "risk_level": "High" },
          { "label": "None", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_D_18",
        "dimension": "Workforce & Culture",
        "question": "Are clinical operations teams trained on AI trial tools?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_D_19",
        "dimension": "Workforce & Culture",
        "question": "Do you collaborate with academic AI research centers?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes, formal", "score": 4, "risk_level": "Low" },
          { "label": "Yes, informal", "score": 3, "risk_level": "Medium" },
          { "label": "Planning", "score": 2, "risk_level": "High" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_D_20",
        "dimension": "Workforce & Culture",
        "question": "Is there cultural resistance to AI driven discovery?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "High", "score": 1, "risk_level": "Critical" },
          { "label": "Moderate", "score": 2, "risk_level": "High" },
          { "label": "Low", "score": 3, "risk_level": "Medium" },
          { "label": "None", "score": 4, "risk_level": "Low" }
        ]
      }
    ],

    "Compliance & Regulatory": [
      {
        "id": "PH_E_21",
        "dimension": "Compliance & Regulatory",
        "question": "Are your AI models FDA/EMA validation-ready?",
        "risk_weight": 5,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In preparation", "score": 3, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_E_22",
        "dimension": "Compliance & Regulatory",
        "question": "Do you maintain algorithm change control for regulated AI?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In development", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_E_23",
        "dimension": "Compliance & Regulatory",
        "question": "Are you compliant with GDPR for clinical trial data?",
        "risk_weight": 5,
        "selection_type": "single",
        "options": [
          { "label": "Fully", "score": 4, "risk_level": "Low" },
          { "label": "Partially", "score": 3, "risk_level": "Medium" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_E_24",
        "dimension": "Compliance & Regulatory",
        "question": "Do you have specific SOPs for GxP environments?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "In development", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_E_25",
        "dimension": "Compliance & Regulatory",
        "question": "How do you handle AI explainability for regulatory submissions?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Robust", "score": 4, "risk_level": "Low" },
          { "label": "Minimal", "score": 2, "risk_level": "Medium" },
          { "label": "None", "score": 1, "risk_level": "High" },
          { "label": "Not applicable", "score": 3, "risk_level": "Medium" }
        ]
      }
    ],

    "ROI & Scaling": [
      {
        "id": "PH_F_26",
        "dimension": "ROI & Scaling",
        "question": "What is your average drug discovery cycle time reduction from AI?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": ">50%", "score": 4, "risk_level": "Low" },
          { "label": "30-50%", "score": 3, "risk_level": "Medium" },
          { "label": "10-30%", "score": 2, "risk_level": "High" },
          { "label": "<10%", "score": 1, "risk_level": "High" },
          { "label": "Not tracked", "score": 0, "risk_level": "Critical" }
        ]
      },
      {
        "id": "PH_F_27",
        "dimension": "ROI & Scaling",
        "question": "Do you track AI impact on clinical trial costs?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes, consistently", "score": 4, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_F_28",
        "dimension": "ROI & Scaling",
        "question": "Do you have AI-enabled manufacturing process optimization?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Pilot", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_F_29",
        "dimension": "ROI & Scaling",
        "question": "Do you measure ROI of AI across R&D and production?",
        "risk_weight": 4,
        "selection_type": "single",
        "options": [
          { "label": "Yes, comprehensive", "score": 4, "risk_level": "Low" },
          { "label": "Partial", "score": 2, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      },
      {
        "id": "PH_F_30",
        "dimension": "ROI & Scaling",
        "question": "Is AI adoption scalable across multiple sites?",
        "risk_weight": 3,
        "selection_type": "single",
        "options": [
          { "label": "Yes", "score": 4, "risk_level": "Low" },
          { "label": "Partially", "score": 3, "risk_level": "Medium" },
          { "label": "No", "score": 1, "risk_level": "High" }
        ]
      }
    ]
  }
}
  

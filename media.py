Question_Bank = {
          "domain": "Media & Entertainment",
  
  "sections": {
  "Infrastructure & Security": [
    {
      "id": "ME_INF_01",
      "dimension": "Infrastructure",
      "question": "Is your content delivery infrastructure modernized?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Fully modernized", "score": 3, "risk_level": "Low" },
        { "label": "Partially modernized", "score": 2, "risk_level": "Medium" },
        { "label": "Minimally modernized", "score": 1, "risk_level": "High" },
        { "label": "Not modernized", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_INF_02",
      "dimension": "Security",
      "question": "Do you use AI for content personalization?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Pilot", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Planning", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_INF_03",
      "dimension": "Data",
      "question": "Are your media assets digitized and AI-tagged?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Fully digitized and AI-tagged", "score": 3, "risk_level": "Low" },
        { "label": "Partially digitized", "score": 2, "risk_level": "Medium" },
        { "label": "Minimally digitized", "score": 1, "risk_level": "High" },
        { "label": "Not digitized", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_INF_04",
      "dimension": "Analytics",
      "question": "Do you have real-time streaming analytics?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Partial", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Planning", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_INF_05",
      "dimension": "Infrastructure",
      "question": "Is your Digital Asset Management (DAM) system AI-enabled?",
      "rank_weight": 4,
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
      "id": "ME_DATA_06",
      "dimension": "Cloud",
      "question": "Do you use cloud-native media processing?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Migration in progress", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_DATA_07",
      "dimension": "Data",
      "question": "Do you have a unified audience data platform?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Partial", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Planning", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_DATA_08",
      "dimension": "Edge Computing",
      "question": "Are you leveraging edge computing for content delivery?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Pilot", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Evaluating", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_DATA_09",
      "dimension": "Metadata",
      "question": "How mature is your metadata and content tagging infrastructure?",
      "rank_weight": 4,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Advanced", "score": 3, "risk_level": "Low" },
        { "label": "Moderate", "score": 2, "risk_level": "Medium" },
        { "label": "Early", "score": 1, "risk_level": "High" },
        { "label": "None", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_DATA_10",
      "dimension": "Rights Management",
      "question": "Do you use AI for rights management?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Partial", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Not applicable", "score": 3, "risk_level": "Low" }
      ]
    }
  ],

  "AI Adoption & Use Cases": [
    {
      "id": "ME_AI_11",
      "dimension": "AI Use Cases",
      "question": "Which AI use cases are you deploying?",
      "rank_weight": 5,
      "risk_weight": 5,
      "selection_type": "multi",
      "options": [
        { "label": "Content recommendation", "score": 1 },
        { "label": "Content moderation", "score": 1 },
        { "label": "Automated video editing", "score": 1 },
        { "label": "Personalized advertising", "score": 1 },
        { "label": "Audience segmentation", "score": 1 },
        { "label": "Predictive content performance", "score": 1 },
        { "label": "Script/screenplay analysis", "score": 1 },
        { "label": "Synthetic media generation", "score": 1 },
        { "label": "Voice cloning/localization", "score": 1 }
      ]
    },
    {
      "id": "ME_AI_12",
      "dimension": "Generative AI",
      "question": "Are you using generative AI for content creation?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3, "risk_level": "Low" },
        { "label": "Pilot", "score": 2, "risk_level": "Medium" },
        { "label": "No", "score": 1, "risk_level": "High" },
        { "label": "Evaluating", "score": 0, "risk_level": "Critical" }
      ]
    },
    {
      "id": "ME_AI_13",
      "dimension": "Computer Vision",
      "question": "Do you use computer vision for video indexing?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Pilot", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_AI_14",
      "dimension": "Audio AI",
      "question": "Are you applying AI to music or soundtrack generation?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Pilot", "score": 2 },
        { "label": "No", "score": 1 },
        { "label": "Not applicable", "score": 3 }
      ]
    },
    {
      "id": "ME_AI_15",
      "dimension": "Experience",
      "question": "Do you offer AI-powered interactive experiences?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Pilot", "score": 2 },
        { "label": "No", "score": 1 },
        { "label": "In development", "score": 2 }
      ]
    }
  ],

  "Workforce & Culture": [
    {
      "id": "ME_WRK_16",
      "dimension": "Adoption",
      "question": "What percentage of creative staff use AI tools?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": ">60%", "score": 3 },
        { "label": "40–60%", "score": 2 },
        { "label": "20–40%", "score": 1 },
        { "label": "<20%", "score": 0 }
      ]
    },
    {
      "id": "ME_WRK_17",
      "dimension": "Leadership",
      "question": "Do you have a Chief AI or Innovation Officer?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Planning", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_WRK_18",
      "dimension": "Training",
      "question": "Are content creators trained on generative AI?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes, formal", "score": 3 },
        { "label": "Yes, informal", "score": 2 },
        { "label": "No", "score": 1 },
        { "label": "Not allowed", "score": 0 }
      ]
    },
    {
      "id": "ME_WRK_19",
      "dimension": "Culture",
      "question": "Is there creative resistance to AI adoption?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "None", "score": 3 },
        { "label": "Low", "score": 2 },
        { "label": "Moderate", "score": 1 },
        { "label": "High", "score": 0 }
      ]
    },
    {
      "id": "ME_WRK_20",
      "dimension": "Ethics",
      "question": "Do you have AI ethics guidelines for content creation?",
      "rank_weight": 4,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "In development", "score": 2 },
        { "label": "No", "score": 0 },
        { "label": "Not applicable", "score": 3 }
      ]
    }
  ],

  "Compliance & Regulatory": [
    {
      "id": "ME_REG_21",
      "dimension": "Compliance",
      "question": "Do you have AI content disclosure policies?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "In development", "score": 2 },
        { "label": "No", "score": 0 },
        { "label": "Not applicable", "score": 3 }
      ]
    },
    {
      "id": "ME_REG_22",
      "dimension": "Bias & Fairness",
      "question": "Do you conduct bias audits for recommendation algorithms?",
      "rank_weight": 4,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Regularly", "score": 3 },
        { "label": "Occasionally", "score": 2 },
        { "label": "Rarely", "score": 1 },
        { "label": "Never", "score": 0 }
      ]
    },
    {
      "id": "ME_REG_23",
      "dimension": "Copyright Compliance",
      "question": "Are you compliant with copyright laws for AI training?",
      "rank_weight": 4,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Fully", "score": 3 },
        { "label": "Partially", "score": 2 },
        { "label": "No", "score": 0 },
        { "label": "Not sure", "score": 1 }
      ]
    },
    {
      "id": "ME_REG_24",
      "dimension": "Deepfake Detection",
      "question": "Do you have deepfake detection capabilities?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Partial", "score": 2 },
        { "label": "No", "score": 0 },
        { "label": "Evaluating", "score": 1 }
      ]
    },
    {
      "id": "ME_REG_25",
      "dimension": "IP Ownership",
      "question": "How do you handle AI-generated IP ownership?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Clear policy", "score": 3 },
        { "label": "Ad hoc", "score": 1 },
        { "label": "Not addressed", "score": 0 },
        { "label": "Not applicable", "score": 3 }
      ]
    }
  ],

  "ROI & Scaling": [
    {
      "id": "ME_ROI_26",
      "dimension": "ROI",
      "question": "What is your AI-driven engagement improvement?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": ">30%", "score": 4 },
        { "label": "20–30%", "score": 3 },
        { "label": "10–20%", "score": 2 },
        { "label": "<10%", "score": 1 },
        { "label": "Not tracked", "score": 0 }
      ]
    },
    {
      "id": "ME_ROI_27",
      "dimension": "Scaling Barriers",
      "question": "What is your biggest barrier to scaling media AI?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Creative resistance", "score": 0 },
        { "label": "IP uncertainty", "score": 0 },
        { "label": "Technology cost", "score": 0 },
        { "label": "Talent shortage", "score": 0 },
        { "label": "Audience trust", "score": 0 }
      ]
    },
    {
      "id": "ME_ROI_28",
      "dimension": "Cost Tracking",
      "question": "Do you track AI impact on content production costs?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes, quantified", "score": 3 },
        { "label": "Yes, estimated", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_ROI_29",
      "dimension": "AI Content Share",
      "question": "What percentage of content is AI-assisted?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": ">50%", "score": 4 },
        { "label": "30–50%", "score": 3 },
        { "label": "10–30%", "score": 2 },
        { "label": "<10%", "score": 1 },
        { "label": "0%", "score": 0 }
      ]
    },
    {
      "id": "ME_ROI_30",
      "dimension": "Scaling Readiness",
      "question": "Are AI systems ready for large-scale deployment?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes, fully", "score": 3 },
        { "label": "Partially", "score": 2 },
        { "label": "No", "score": 0 },
        { "label": "Planning", "score": 1 }
      ]
    }
  ],

  "Advanced AI Capabilities": [
    {
      "id": "ME_ADV_31",
      "dimension": "NLP",
      "question": "Do you use NLP for script or dialogue analysis?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Pilot", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_ADV_32",
      "dimension": "AR/VR",
      "question": "Are you leveraging AR/VR for AI-driven experiences?",
      "rank_weight": 3,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes", "score": 3 },
        { "label": "Pilot", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_ADV_33",
      "dimension": "Synthetic Media",
      "question": "Do you generate synthetic actors or media using AI?",
      "rank_weight": 4,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes, extensively", "score": 3 },
        { "label": "Yes, partially", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_ADV_34",
      "dimension": "Predictive Analytics",
      "question": "Do you predict content trends using AI?",
      "rank_weight": 5,
      "risk_weight": 4,
      "selection_type": "single",
      "options": [
        { "label": "Yes, accurately", "score": 3 },
        { "label": "Partially", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    },
    {
      "id": "ME_ADV_35",
      "dimension": "AI Operations",
      "question": "Do you have MLOps pipelines for media AI?",
      "rank_weight": 4,
      "risk_weight": 3,
      "selection_type": "single",
      "options": [
        { "label": "Yes, fully automated", "score": 3 },
        { "label": "Partial automation", "score": 2 },
        { "label": "No", "score": 0 }
      ]
    }
  ]
}
    }
    

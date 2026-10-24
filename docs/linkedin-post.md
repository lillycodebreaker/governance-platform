AI governance becomes tangible when you can run the controls and inspect the evidence.

I've been working on a hands-on AI Governance Lab that brings together:

• ML fairness audits using Fairlearn and AIF360
• Model explanations with SHAP and LIME
• A governed support retrieval pipeline using LangChain and Semantic Kernel
• Regression cases for grounding, abstention, prompt injection and disclosure attempts
• Audit events that record operational metadata without storing prompt or response text

One result stood out: reducing a demographic parity gap did not improve every fairness measure. In the synthetic experiment, reweighing reduced that gap from 0.088 to 0.004, while the equalized odds gap increased from 0.054 to 0.214.

That's the engineering challenge I wanted to explore: making tradeoffs visible so people can review them.

The core demos run locally without API keys. Live generation and external judge integrations are optional. This is an educational portfolio project with synthetic data, not a claim of production readiness or regulatory compliance.

Code and setup:
https://github.com/lillycodebreaker/governance-platform

Which evidence would you want to see before approving an AI system for deployment?

#AIGovernance #ResponsibleAI #AIEngineering #ExplainableAI #LLM

# Interactive governance portal

A buildless browser demo based on the supplied AI Governance Lab user manual. Register synthetic assets, walk through release gates, simulate runtime controls, record measurement inputs and export/reimport an audit package.

From the repository root, start with Python 3.11+:

```sh
python app.py
```

Open http://127.0.0.1:8765/. Stop the local server with Ctrl+C.

The portal has no accounts or server-side persistence. Assets and events are saved in localStorage for this browser and origin. Use synthetic metadata. The hosted Site starts owner-private, with hosting access separate from asset registration. Browser data is not synchronized between the local and hosted versions.

Evaluation PASS/FAIL rows are explicitly illustrative fixtures. LangFair, UQLM and LLMs are not executed in the browser. Human approvals are demo labels, not authenticated signatures. Runtime responses, action execution and deployment are simulated. Run the separate Python lab for actual fairness and retrieval evaluation.

The state machine enforces current evidence, human approval, release status, material-change reassessment, per-asset isolation and a three-violation circuit breaker. Audit exports contain SHA-256-linked events; imports verify the chain and recalculate metrics without modifying live state. A chain is not a digital signature or tamper-resistant record.

Run the behavior checks with Node.js 20+:

```sh
cd portal
node --test model.test.mjs
```

`dist/usermanual.html` preserves the original illustrated manual, with a banner explaining differences in the new walkthrough. `dist/` is the static deployment output. No build or package installation is required.

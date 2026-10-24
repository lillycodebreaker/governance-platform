# AI Governance Lab

A runnable engineering portfolio exploring how to turn responsible AI principles into measurable controls: fairness audits, model explanations, constrained retrieval, risk evaluation, and privacy-conscious audit events.

The examples use synthetic data and run locally without API credentials. This repository is an educational lab, not a production governance platform or a compliance certification.

## Interactive portal

Run `python app.py` and open http://127.0.0.1:8765/ to register synthetic AI assets and explore evaluation gates, human review, simulated releases, runtime controls and audit exports. The portal includes a guided user manual and the original illustrated manual. See [portal setup and scope](portal/README.md).

An [owner-private hosted portal](https://governance-lab-asset-portal.indigoanole8.chatgpt.site) is also available to the Site owner. Other visitors can clone and run the local version.

Portal evaluations are illustrative fixtures, and browser data stays local. The Python commands below run actual ML and retrieval evaluations.

## What you can explore

| Area | Implementation | Evidence |
| --- | --- | --- |
| ML fairness | Logistic regression, AIF360 Reweighing, Fairlearn ThresholdOptimizer | Held-out accuracy, selection rates, demographic parity and equalized odds gaps |
| Explainability | SHAP and LIME on the baseline classifier | Feature contributions, SHAP additivity, local surrogate fit |
| Governed support assistant | LangChain pipeline and a Semantic Kernel knowledge-search plugin | Read-only tool allowlist, screened inputs/retrieval, unsupported-question abstention |
| GenAI risk testing | Six offline cases; optional DeepEval, RAGAS and TruLens judges | Grounding, abstention, direct/indirect injection, disclosure and Unicode-obfuscation checks |
| Observability | Local JSONL audit events | Trace ID, latency, status, policy version and corpus hash; prompt/response text excluded |

## Run locally

Prerequisites: Python 3.11 or 3.12 and [uv](https://docs.astral.sh/uv/). Run from the repository root.

```sh
git clone https://github.com/lillycodebreaker/governance-platform.git
cd governance-platform
uv sync --frozen --extra dev --extra eval --prerelease=allow
uv run --no-sync python -m lab.ml
uv run --no-sync python -m lab.ai "How long does standard shipping take?"
uv run --no-sync python -m lab.evaluate
uv run --no-sync python -m pytest -q
```

These commands work in PowerShell and POSIX shells. The lockfile pins dependencies, including the Azure prerelease dependency required by Semantic Kernel. The `eval` extra includes the optional judge integrations used by the full test suite.

For a smaller install, omit `--extra eval` and run tests with `-k "not eval_integrations_import"`. The default assistant extracts text from a tiny local corpus; it does not call an LLM. The shipping question returns `Standard shipping takes 5 business days.`

These commands run the Python lab independently of the optional interactive portal.

## Inspect the outputs

Running the demos creates ignored files under `artifacts/`:

- `ml_report.json`: held-out model metrics and numerical explanations.
- `lime_explanation.html`: browser-viewable local explanation.
- `ai_report.json`: case-level results, with external judges explicitly marked `not_run` by default.
- `audit.jsonl`: append-only local audit events. This is not tamper-resistant storage.

The seed-42 experiment uses 2,400 synthetic applicants, split into training, calibration and held-out test sets. The labels deliberately include group bias.

| Model | Accuracy | Demographic parity gap | Equalized odds gap |
| --- | ---: | ---: | ---: |
| Baseline | 0.719 | 0.088 | 0.054 |
| AIF360 reweighed | 0.719 | 0.004 | 0.214 |
| Fairlearn threshold | 0.708 | 0.025 | 0.133 |

Both mitigations reduce selection-rate disparity in this experiment while increasing equalized-odds disparity. Fairness needs an explicit objective and review of competing outcomes. Agreement with biased historical labels is not an ethical quality measure.

## Optional live generation and judges

Install the `eval` extra, then configure credentials and model IDs in your own shell. PowerShell example:

```powershell
$env:OPENAI_API_KEY = "your-key"
$env:GENERATOR_MODEL = "your-generation-model-id"
$env:JUDGE_MODEL = "your-judge-model-id"
uv run --no-sync python -m lab.ai --live "How long does standard shipping take?"
uv run --no-sync python -m lab.evaluate --live --judges
```

Live calls transmit synthetic inputs to the configured provider and incur usage charges. Never commit credentials. Offline exact-match checks are regression tests, not measurements of LLM hallucination rates. Live paraphrases can fail exact-match checks even when valid. External judges are fallible and are not run by the default commands.

## Design boundaries

Input screening is heuristic and can miss novel attacks. Retrieved source IDs establish provenance, not claim-level factual support. The stronger capability restriction is the invocation allowlist permitting only `knowledge.search`; the assistant has no action tools. SHAP/LIME explain model behavior, not causation. ThresholdOptimizer uses group membership at inference and can randomize decisions.

Production work would require authentication, authorization, tenant isolation, rate limits, durable audit storage, representative adversarial evaluation, and broader fairness analysis with uncertainty estimates.

## Repository map

```text
lab/ml.py              Synthetic ML audit and explanations
lab/ai.py              Governed support retrieval pipeline
lab/evaluate.py        Offline cases and opt-in external judges
tests/test_lab.py      Regression and integration-import tests
docs/technical-guide.md Detailed methods, references and caveats
docs/linkedin-post.md  Portfolio announcement draft
pyproject.toml         Dependencies and pytest configuration
uv.lock                Reproducible dependency resolution
```

See the [technical guide](docs/technical-guide.md) for methods and framework references, and the [local validation record](docs/validation.md) for tested commands and limitations. LangFair and UQLM are separate upstream projects present in the original workspace; their source is not bundled or used by this lab.

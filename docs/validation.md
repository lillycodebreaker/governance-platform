# Local validation

Validated on October 24, 2026, on Windows with Python 3.11, running the packaged source from the repository root using the original lab's existing virtual environment.

| Check | Result |
| --- | --- |
| `python -m pytest -q` | 11 passed; three upstream SHAP plotting deprecation warnings |
| `python -m lab.ml` | Completed; generated model metrics, SHAP contributions and LIME HTML |
| `python -m lab.ai "How long does standard shipping take?"` | Returned the expected shipping answer with the `shipping` citation |
| `python -m lab.evaluate` | All six offline cases passed; external judges marked `not_run` |
| `uv lock --check --offline --cache-dir .uv-cache --prerelease=allow` | Passed; resolved 294 packages |

The local interpreter printed a platform-library path warning but commands completed successfully. AIF360 also reported unavailable optional algorithms; those algorithms are not used by the demos. Semantic Kernel logged the intentional blocked-retrieval case during evaluation.

A fresh dependency installation, Python 3.12, live generation and external judge API calls were not tested. The results validate this small synthetic experiment; they do not establish production safety, regulatory compliance or general resistance to prompt injection.

## Interactive portal

The new browser-local portal was checked on October 24, 2026:

- `node --test portal/model.test.mjs`: six tests passed, covering release gates, circuit breaker behavior, model reassessment, asset isolation, audit-chain verification and measurement denominators.
- JavaScript syntax checks passed for `portal/dist/app.js` and `portal/dist/model.mjs`.
- Browser walkthrough completed: registration, passing illustrative suite, reviewer approval, demo release and derived audit metrics.
- Responsive narrow-screen layout inspected in the in-app browser.

Portal checks use fixtures and simulated actions. They do not execute the Python lab or LangFair/UQLM. The portal tests are independent of the eleven Python tests above.

# ML Systems Blueprints

[![Quality](https://github.com/vipul957/ml-systems-blueprints/actions/workflows/quality.yml/badge.svg)](https://github.com/vipul957/ml-systems-blueprints/actions/workflows/quality.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **ML Systems Blueprints** is a production-minded reliability utilities for research-to-inference workflows.

## Start here

**In one sentence:** Turn research models into observable, testable, deployment-ready systems.

| If you want to... | Open this first |
|---|---|
| Understand the method | [`src/ml_systems_blueprints/monitoring.py`](src/ml_systems_blueprints/monitoring.py) |
| See the second reusable utility | [`src/ml_systems_blueprints/contracts.py`](src/ml_systems_blueprints/contracts.py) |
| Run a tiny example | [`examples/quick_demo.py`](examples/quick_demo.py) |
| Understand the next milestone | [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Check correctness | [`tests/`](tests/) and the CI badge above |

### System flow

```mermaid
flowchart LR
    A[Domain input] --> B[Validated contract]
    B --> C[model]
    C --> D[Measured output]
    D --> E[Limitations and next experiment]
```

### What is implemented now

The repository currently contains a dependency-light, deterministic baseline with tests. It is intentionally small enough to inspect line by line. The next research layer should preserve the same input contract and evaluation protocol rather than replacing the baseline with an opaque demo.


## Visual architecture

The project follows a transparent pipeline. Each stage has a testable responsibility, and the evaluation stage feeds failure information back into the next experiment.

```mermaid
flowchart LR
    A["Inference payload + schema"] --> B["Validate contract"]
    B --> C["Model + monitoring checks"]
    C --> D["Risk decision / alert"]
    D --> E["Drift / latency / rollback"]
    E --> F["ML Systems Blueprints
Evaluation"]
    F -. feedback .-> C
```


For implementation details, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Problem statement

Make drift, ownership, and operational assumptions visible before deployment.

The central mathematical object is **PSI=sum((actual_i-expected_i)*log(actual_i/expected_i))**. The current implementation keeps this object small and testable so that later deep-learning improvements can be compared with an auditable baseline.

## Data contract

Expected input: **reference/serving numeric batches, timestamps, schema, and model metadata**. Every adapter must document units, provenance, timezone, missing values, licensing, and information available at prediction time. Synthetic examples test the software contract; they are not domain evidence.

## Baseline and assumptions

The first method is **dependency-light monitoring followed by validation, tracking, model cards, and health checks**. It assumes correctly timestamped observations and a stable evaluation definition. A future model must preserve the split logic and report improvement over this baseline rather than only reporting an absolute score.

## Evaluation protocol

Report **drift sensitivity, alert precision, false positives, latency, rollback time**. Include performance by regime, calibration or uncertainty quality where applicable, compute cost, and known failure cases. Never tune repeatedly on the final test set.

## Next research milestone

**Add typed data contracts, FastAPI reference service, metrics, and deployment records.**

## Research status

This repository is a documented baseline and extensible source scaffold. Results are experimental until validated on a licensed, representative dataset. No proprietary data, employment claim, endorsement, or company affiliation is implied.

## Architecture

The project separates domain formulation, data contracts, deterministic baselines, model implementations, evaluation, and deployment concerns. `src/` contains importable utilities, `tests/` contains fast contract tests, `examples/` contains runnable synthetic demonstrations, and `docs/ROADMAP.md` describes the next research stages.

## Reproducibility contract

Any future experiment must record dataset provenance and license, units and timezone, sampling interval, missing-value policy, split logic, random seeds, software versions, compute environment, and known limitations. Preprocessing must be fitted only on training data. Temporal problems require chronological or group-aware splits.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest -q
python examples/quick_demo.py
```

## Engineering standards

The repository includes GitHub Actions CI, MIT licensing, contribution and security guidance, issue and pull-request templates, and monthly Dependabot updates. A model card should be added before presenting domain results as decision-ready.

## Limitations

The baseline is not production-ready. Real deployment requires external validation, monitoring, access controls, incident response, and review by subject-matter experts.

## References

[1]: https://scikit-learn.org/stable/modules/model_evaluation.html "Scikit-learn model evaluation"
[2]: https://pytorch.org/docs/stable/index.html "PyTorch documentation"

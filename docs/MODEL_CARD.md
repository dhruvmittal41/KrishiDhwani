# Model card — planned, no trained model

Purpose: classify a verified subset of audible insect sounds and produce inspection cues.
Target classes: not selected yet. Architecture: compact CNN / DS-CNN candidate. Baseline: MFCC + conventional classifier.
Weights: not available. Accuracy, calibration, runtime and field range: not measured.

Training sources must have traceable licences and species labels. Split by source recording/session; reserve held-out farms, dates and devices for validation. Evaluate background and unsupported insects. Use a calibrated rejection policy; softmax alone is not an unknown detector.

Not suitable for pest counts, guaranteed infestation diagnosis, universal species identification or automatic pesticide recommendations.

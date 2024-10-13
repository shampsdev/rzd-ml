from __future__ import annotations

import os
import argparse
import json

from src.predictor import Predictor


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get submission.")
    parser.add_argument(
        "--src",
        type=str,
        help="Path to the source audio files.",
    )
    parser.add_argument(
        "--dst",
        type=str,
        help="Path to the output submission.",
    )
    args = parser.parse_args()
    predictor = Predictor()

    results = []
    for audio_path in os.listdir(args.src):
        result = predictor(os.path.join(args.src, audio_path))
        results.append(result)

    with open(
        os.path.join(args.dst, "submission.json"), "w", encoding="utf-8"
    ) as outfile:
        json.dump(results, outfile)

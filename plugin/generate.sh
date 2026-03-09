#!/bin/bash
set -e
cd "$(dirname "$0")"

pip install -e synth/ -q
synth generate --config synth.toml

echo "Done. WAV files written to sounds/"

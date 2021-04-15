#!/bin/bash

cargo install cargo-generate
cargo install --git https://github.com/PRL-PRG/cargo-djanco
cargo generate --git https://github.com/PRL-PRG/djanco-query-template --name my-query-crate
cd my-query-crate
cargo djanco
cargo run --release --bin djanco -- --dataset-path ../toy-dataset --cache-path cache --output-path output
cd ..
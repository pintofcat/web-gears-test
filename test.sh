#!/bin/bash

set -e

#docker-compose -f docker-compose.test.yml build --progress plain
docker-compose -f docker-compose.test.yml run --rm test-web pytest --showlocals --durations=10 $@

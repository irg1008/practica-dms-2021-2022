#!/usr/bin/env bash
(find . -type f  -name "*.sh" -print0 | xargs -0 dos2unix) && docker-compose -f docker/config/dev.yml up -d
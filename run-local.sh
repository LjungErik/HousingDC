#!/bin/bash
docker_image=$(docker build -q .)
CONF_FILE="private-config.ini"

if [ -z ${docker_image} ]; then
    echo "${docker_image}"
    echo "DOCKER IMAGE COULD NOT BE BUILT"
else
    echo "RUNNING DOCKER IMAGE: ${docker_image}" 
    if [ -f $CONF_FILE ]; then
        docker run -it --rm \
        -e COLLECTOR_CONFIG_PATH="/etc/collector/config.ini" \
        -e COLLECTOR_VERBOSE="TRUE" \
        -v $(pwd)/$CONF_FILE:/etc/collector/config.ini:ro \
        -v $(pwd)/test-symbols.json:/etc/collector/symbols.json:ro \
        ${docker_image} $@
    else
        docker run -it --rm \
        -e COLLECTOR_CONFIG_PATH="/etc/collector/config.ini" \
        -e COLLECTOR_VERBOSE="TRUE" \
        -v $(pwd)/test-config.ini:/etc/collector/config.ini:ro \
        -v $(pwd)/test-symbols.json:/etc/collector/symbols.json:ro \
        ${docker_image} $@
    fi
fi
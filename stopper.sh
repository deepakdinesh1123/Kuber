#!/bin/bash

# Set the image name to identify the containers to stop and remove
image_name="why:latest"

# Stop and remove containers based on the image name
container_ids=$(docker ps -a --filter "ancestor=$image_name" -q)
if [ -z "$container_ids" ]; then
  echo "No containers found for image: $image_name"
else
  echo "Stopping and removing containers for image: $image_name"
  docker stop $container_ids
  docker rm $container_ids
fi

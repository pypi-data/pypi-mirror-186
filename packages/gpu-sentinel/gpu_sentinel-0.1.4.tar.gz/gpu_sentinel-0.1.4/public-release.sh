#!/bin/bash

# Deploy the code to github
#cd /home/nharada/Code/copybara
#bazel run //java/com/google/copybara -- migrate ~/Code/moonshine/src/public/gpu_sentinel/copy.bara.sky
#cd -

# Build and deploy the release
python -m build
twine check dist/*
twine upload dist/*
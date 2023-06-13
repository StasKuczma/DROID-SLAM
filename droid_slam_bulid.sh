xhost +local:root

# BUILD THE IMAGE
docker build -f Dockerfile -t "DROID_SLAM_IMAGE" ./..

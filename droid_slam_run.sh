xhost +local:root

# BUILD THE IMAGE
DROID_IMAGE="DROID_SLAM_IMAGE"
DROID_CONTAINER="DROID_SLAM"
 
docker stop $DROID_CONTAINER || true && docker rm $DROID_CONTAINER || true

docker run -itd \
    --gpus all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env="XAUTHORITY=$XAUTH" \
    --volume="$XAUTH:$XAUTH" \
    --env="NVIDIA_VISIBLE_DEVICES=all" \
    --env="NVIDIA_DRIVER_CAPABILITIES=all" \
    --privileged \
    --network=host \
    --name="$ROS_CONTAINER" \
    $DROID_IMAGE \
   # /bin/bash

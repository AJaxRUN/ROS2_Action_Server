docker build -t fleetglue_ros2 .
docker run --rm -it -p 8080:8080 fleetglue_ros2
curl http://127.0.0.1:8080/mission
curl -X 'POST' \
  'http://127.0.0.1:8080/mission' \
  -H 'Content-Type: application/json' \
  -d '{"mission_id": 8}'
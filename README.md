# ROS2 Action Hooks
## Details:
1. Create a python REST API
    - one POST mission endpoint which accepts json
    - one GET mission endpoint which retrieves json from the POST endpoint
2. Create ROS2 python node 1 (RN1)
    - Uses the GET API endpoint to check for new data at least every second
    - Processes json from the REST API into a ROS action
    - Hosts an Action Client, which sends the ROS action to the Action Server
3. Create ROS2 python node 2 (RN2)
    - Hosts an Action Server
    - Execute callback simply prints the ROS action

## Implementation:
Using ROS2 Humble as base image the expected functionality resides in a docker container. I have implemented an in memory queue instead of MQTT, given its a simple functionality. All that needs to be done to run the container are build and deploy: 
```
docker build -t fleetglue_assignment .
```
Exposed port 8080, to use a different port modify *EXPOSE* line in Dockerfile
```
docker run --rm -it -p 8080:8080 fleetglue_assignment
```
To test the GET endpoint you can use:
```
curl http://127.0.0.1:8080/mission
```
To test the POST endpoint you can use:
```
curl -X 'POST' \
  'http://127.0.0.1:8080/mission' \
  -H 'Content-Type: application/json' \
  -d '{"mission_id": 8}'
```

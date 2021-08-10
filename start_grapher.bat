set tag=basic_v2.4
echo %tag%
docker run --name grapher -w /root/Graphs -td grapher:%tag% bash
docker exec -ti grapher bash
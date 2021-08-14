set temp_dir=%cd%\..\runtemp
docker run -td --name graph-drawer -v %temp_dir%:/root/runtemp -w /root/runtemp %1 bash
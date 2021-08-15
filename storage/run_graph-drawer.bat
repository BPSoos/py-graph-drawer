SET temp_dir=%~dp0../runtemp/

if [%1] NEQ [] (
    SET image=%1
) else (
    python %temp_dir%../libraries/yaml_parser.py "get_graph_drawer_data('%temp_dir%../storage/versions_info.yaml','image')" > Output
    SET /p image=<Output
    DEL Output
)

docker run -td --name graph-drawer -v %temp_dir%:/root/py-graph-drawer/runtemp^
                                   -v %temp_dir%../libraries/:/root/py-graph-drawer/libraries^
								   -w /root/py-graph-drawer/runtemp^
								    %image% bash

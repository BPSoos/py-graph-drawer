SET temp_dir=%~dp0../runtemp/
if [%1] NEQ [] (
SET image=%1
) else (
python %temp_dir%../libraries/yaml_parser.py "get_graph_drawer_data('%temp_dir%../storage/versions_info.yaml','image')" > Output
SET /p image=<Output
DEL Output
)
ECHO docker run -td --name graph-drawer -v %temp_dir%:/root/runtemp -w /root/runtemp %image% bash

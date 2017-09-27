import re
#back up source file
pass
#open the config file

srsconfig=open('srs.conf',mode='r')
change='rtmp://stream.vkuserlive.com:443/live?s;\n'
program_list=(
    'ingest cctve_fb {',
    'ingest cctvf_fb {',
    'ingest cctva_fb {',
    'ingest cctvr_fb {',
    'ingest cctve_live_fb {',
    'ingest cctvf_live_fb {',
    'ingest cctva_live_fb {',
    'ingest cctvr_live_fb {',
    'ingest cctve_yt {',
    'ingest cctvf_yt {',
    'ingest cctva_yt {',
    'ingest cctvr_yt {',
    'ingest cctvr_vk {',)
for line in srsconfig:
    if not line:
        break
    if program_list[0] in line:

        print(line)
    if 'output' in line:
        testchange = re.split(' ',line)
        testchange[-1]=change
        #print(line)
        print(' '.join(testchange))
#close the file
srsconfig.close()
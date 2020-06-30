resources = ['形态表','CX600_M2', 'CX6600', 'NE40E', 'NE5000E', 'NE8000', 'NE9000']

resources_dic = {
    'CX600_M2':['NPU240A(4G 4Bank)','NPU480(4G 4Bank)'], #先写一个 再说
    'CX6600' : ['1TCB(5885)','2TF&4TA(5886)','LPUI2T(5886)']
}

head_name = {
    'id':'ID',
    'algo' : '算法',
    'name' : '业务名',
    'bit' : '位宽(bit)',
    'numK' : '条数(K)',
    'tidW' : 'TID位宽',
    'tidN' : 'TID值',
    'subTidW' : 'SubTID位宽',
    'subTidN' : 'SubTID值',
    'sTypeW_bit' : 'server type位宽/起始bit',
    'sType' : 'server type值',
    'storeLocation' : '存储位置',
    'algoId': '算法表ID',
    'ISSU':'ISSU升级表ID偏移值',
    'algoSpe': '算法表规格(K)',
    'testSpe': '测试规格(K)',
    'castType':'单/多播',
    'iOrd': 'index/data模式',
    'TBLM_ID': 'TBLM_ID',
    'dpt':'落地部门',
    'dpt_person':'落地负责人',
    'confirmation':'落地情况确认'
}

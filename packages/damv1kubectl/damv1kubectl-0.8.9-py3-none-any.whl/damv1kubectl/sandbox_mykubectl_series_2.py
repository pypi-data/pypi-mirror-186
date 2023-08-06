import damv1time7 as time7
import damv1time7.mylogger as Q
import damv1manipulation as mpl

import re
import time
import stringcase

from .sandbox_mykubectl_series_1 import sanbox
cortex = sanbox()

class sandbox_series_2():

    # 2023-01-18 | new function for detected case of deployment name by podname
    def getJson_infoLabel_IoName_singlePods_by_podname_ns(self, _podname, _ns, _bShowCommandGtPoC = False):
        lst_ipoC = []
        get_bStatus_complete_sshcmd = False
        get_exception_message_handler = ''
        try:
            str_jsonpath =  '{.metadata.name}{", "}{.metadata.namespace}{", "}{.metadata.labels.app\.kubernetes\.io\/name}{", "}{.metadata.labels.pod-template-hash}'

            cmd_gtPoC = "kubectl get pods {podname} -n {ns} -o jsonpath='{c_jsonpath}' --sort-by=.metadata.name".format(podname =  _podname, ns = _ns, c_jsonpath = str_jsonpath)
            if _bShowCommandGtPoC==True: print(cmd_gtPoC)
            get_bStatus_complete_sshcmd, get_exception_message_handler, raw_datas = cortex.execsshcmd_detail_v2(cmd_gtPoC)
            if raw_datas==None:
                raise Exception('Please check your connection and try again [Fail of function "execsshcmd"]')
            else: 
                data_line = {}
                lst_infpod = str(raw_datas).strip("']['").split(', ')
                if "'list'" in str(type(lst_infpod)):
                    data_line['pod'] = str(lst_infpod[0])
                    data_line['namespace'] = str(lst_infpod[1])
                    data_line['labels component name'] = str(lst_infpod[2])
                    data_line['labels template hash'] = str(lst_infpod[3])
                if len(data_line)>0: lst_ipoC.append(data_line)
        except Exception as e:
            Q.logger(time7.currentTime7(),'Fail of function "getJson_infoLabel_IoName_singlePods_by_podname_ns"')  
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return get_bStatus_complete_sshcmd, get_exception_message_handler, lst_ipoC

    # 2023-01-18 | new function for detected case of deployment name by podname
    def getJson_infoLabel_Component_singlePods_by_podname_ns(self, _podname, _ns, _bShowCommandGtPoC = False):
        lst_ipoC = []
        get_bStatus_complete_sshcmd = False
        get_exception_message_handler = ''
        try:
            str_jsonpath =  '{.metadata.name}{", "}{.metadata.namespace}{", "}{.metadata.labels.component}{", "}{.metadata.labels.pod-template-hash}'

            cmd_gtPoC = "kubectl get pods {podname} -n {ns} -o jsonpath='{c_jsonpath}' --sort-by=.metadata.name".format(podname =  _podname, ns = _ns, c_jsonpath = str_jsonpath)
            if _bShowCommandGtPoC==True: print(cmd_gtPoC)
            get_bStatus_complete_sshcmd, get_exception_message_handler, raw_datas = cortex.execsshcmd_detail_v2(cmd_gtPoC)
            if raw_datas==None:
                raise Exception('Please check your connection and try again [Fail of function "execsshcmd"]')
            else: 
                data_line = {}
                lst_infpod = str(raw_datas).strip("']['").split(', ')
                if "'list'" in str(type(lst_infpod)):
                    data_line['pod'] = str(lst_infpod[0])
                    data_line['namespace'] = str(lst_infpod[1])
                    data_line['labels component name'] = str(lst_infpod[2])
                    data_line['labels template hash'] = str(lst_infpod[3])
                if len(data_line)>0: lst_ipoC.append(data_line)
        except Exception as e:
            Q.logger(time7.currentTime7(),'Fail of function "getJson_infoLabel_Component_singlePods_by_podname_ns"')  
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return get_bStatus_complete_sshcmd, get_exception_message_handler, lst_ipoC

    def getLstEvents_fieldSelector_byDeployment(self, _deployment, _namespace, _bShowCommandGtPoC = False):
        lst_oput = []
        get_bStatus_complete_sshcmd = False
        get_exception_message_handler = ''
        try:
            cmd_gtEvent = "kubectl get events --field-selector involvedObject.name={deployment} -n {ns} --no-headers --sort-by='.lastTimestamp'".format(deployment = _deployment, ns = _namespace)
            cmd_awk = cmd_gtEvent + " | awk '{printf $1\" | \"$2\" | \"$3\" | \"$4\" | \"}{for(i=5;i<=NF;i++) printf $i\" \"; print \"\"}'"
            if _bShowCommandGtPoC==True: print(cmd_awk)
            get_bStatus_complete_sshcmd, get_exception_message_handler, raw_datas = cortex.execsshcmd_detail_v2(cmd_awk)
            if len(raw_datas) != 0 :
                lst_oput = raw_datas
        except Exception as e:
            Q.logger(time7.currentTime7(),'Fail of function "getLstEvents_fieldSelector_byDeployment"')  
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return get_bStatus_complete_sshcmd, get_exception_message_handler, lst_oput

    def execRollout_restartDeployment(self, _deployment, _namespace, _bShowCommandGtPoC = False):
        lst_oput = []
        get_bStatus_complete_sshcmd = False
        get_exception_message_handler = ''
        try:
            cmd = "kubectl rollout restart deployment/{deployment} -n {ns}".format(deployment = _deployment, ns = _namespace)
            if _bShowCommandGtPoC==True: print(cmd)
            get_bStatus_complete_sshcmd, get_exception_message_handler, raw_datas = cortex.execsshcmd_detail_v2(cmd)
            if len(raw_datas) != 0 :
                lst_oput = raw_datas
        except Exception as e:
            Q.logger(time7.currentTime7(),'Fail of function "execRollout_restartDeployment"')  
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return get_bStatus_complete_sshcmd, get_exception_message_handler, lst_oput

    # from ast import literal_eval # Just for simulation
    def getEventsResponse_afterRestartDeployment_v2(self, _deployment, _namespace, _inCase, _bShowCommandGtPoC = False, _bShowResult = False):
        lst_oput = []
        response = False; 
        get_bStatus_complete_sshcmd = False; get_exception_message_handler = ''
        try:
            # # simulation sampling - - - - -
            # data = open('sample2.txt')
            # mainlist = [list(literal_eval(line)) for line in data]
            # lst_oput = mainlist[0]
            # # - - - - - - - - - - - - -
            get_bStatus_complete_sshcmd, get_exception_message_handler, lst_oput = self.getLstEvents_fieldSelector_byDeployment(_deployment, _namespace, _bShowCommandGtPoC)
            material_data = ''
            strfind_up = 'Scaled up replica set'
            strfind_down = 'Scaled down replica set'
            if len(lst_oput)!=0:
                lst_event_last_head2 = list(reversed(lst_oput))[0:2]
                # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                if len(lst_event_last_head2) == 1: # for only one list of event Scaled up
                    if _inCase == "event scaled up":
                        material_data = lst_event_last_head2[0].removesuffix('\n')
                        pattern = re.compile(r'{0}'.format(strfind_up))
                else:
                    # for only list of last event Scaled up
                    if re.search(re.compile(r'{0}'.format(strfind_up)), lst_event_last_head2[0].removesuffix('\n')) and _inCase == "event scaled up":  
                        material_data = lst_event_last_head2[0].removesuffix('\n')
                        pattern = re.compile(r'{0}'.format(strfind_up))
                    else:
                        if _inCase == "event scaled up":
                            material_data = lst_event_last_head2[-1:][0].removesuffix('\n')
                            pattern = re.compile(r'{0}'.format(strfind_up))
                        elif _inCase  == "event scaled down":
                            material_data = lst_event_last_head2[0].removesuffix('\n')
                            pattern = re.compile(r'{0}'.format(strfind_down))
                # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                if material_data != '':
                    row_split = material_data.split(" | ")
                    if len(row_split)!=0:
                        eTime = ''
                        eStatus = ''
                        eTask = ''
                        for idy, col in enumerate(row_split):
                            if idy == 0: eTime = col
                            if idy == 1: eStatus = col
                            if idy == 2: eTask = col
                            if idy == 4:
                                if re.search(pattern, col):
                                    lst_pods_events = mpl.string().getWord_searchString(col,_deployment)
                                    key = mpl.listofdictionary().getKeys_dictionary(lst_pods_events,0)
                                    if len(lst_pods_events)!=0:
                                        if _bShowResult == True:
                                            Q.logger(time7.currentTime7(),' '*6, '{0}:'.format(str(stringcase.capitalcase(_inCase))))
                                            Q.logger(time7.currentTime7(),' '*7,' - {0}/{1}/{2}'.format(str(eTime),str(eStatus),str(eTask)))
                                            Q.logger(time7.currentTime7(),' '*7,' - ' + str(col))
                                            Q.logger(time7.currentTime7(),' '*7,' - event podname:', str(lst_pods_events[0][int(key)]))
                                        response = True
                                    break
                    
                
                message = "EVENTS IS AVAILABLE"
            else:
                message = 'EVENTS IS NOT AVAILABLE'
            lst_oput.clear()
        except Exception as e:
            Q.logger(time7.currentTime7(),'Fail of function "response_afterRestartDeployment"')  
            Q.logger(time7.currentTime7(),'Error Handling ( エラー ):',str(e))
        return get_bStatus_complete_sshcmd, get_exception_message_handler, message, response

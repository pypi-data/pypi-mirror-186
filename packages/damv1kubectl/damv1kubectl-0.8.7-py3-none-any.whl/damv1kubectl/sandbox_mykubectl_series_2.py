import damv1time7 as time7
import damv1time7.mylogger as Q
import damv1manipulation as mpl

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
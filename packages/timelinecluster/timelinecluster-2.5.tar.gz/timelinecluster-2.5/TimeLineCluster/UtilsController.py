import os.path
import json
import js2py
import TimeLineCluster.ConfigReader as ConfigReader
def readFileJson(path):
    if(os.path.exists(path)):
        try:
            with open(path, "r" , encoding="utf8") as openfile:
                data = json.load(openfile)
            return data
        except:
            print("Variable " + path + " is not defined")
            return False
    else:
        print("Path not found :", path)
        return False

def fileExists(path):
    if(os.path.exists(path)):
        return True
    else:
        return False

def getEpWeek(date):
    eval_res, tempfile = js2py.run_file(ConfigReader.ConfigPath.path_js + "getWOY.js")
    ep = tempfile.getWeekOfYear(str(date))
    return ep

def writeLastUpdateSurveyJson(filename , last_update):
    dictionary = {
        "last_update" : last_update,
    }
    json_object = json.dumps(dictionary, indent = 4 , ensure_ascii=False)
    with open(filename, "w" , encoding='utf-8') as outfile:
        outfile.write(json_object)
        
def genStringValuesBindParam(count):
    str = ""
    for i in range(count):
        if(i > 0):
            str += ", %s"
        else:
            str += "%s"
    return str

def getSql():
    return {
                # insert_for_new_cluster
                "sql_for_insert_execute" : { 
                    "report_sql" : "",
                    "report_values" : [],
                    "summary_sql" : "",
                    "summary_values" : [],
                    "member_sql" : "",
                    "member_values" : [],
                    "summary_details_sql" : "",
                    "summary_details_values" : [],
                    "member_details_sql" : "",
                    "member_details_values" : [],
                },
                # insert_for_existing_cluster
                "sql_for_insert_cluster_execute" : {
                    "summary_sql" : "",
                    "summary_values" : [],
                    "member_sql" : "",
                    "member_values" : [],
                    "summary_details_sql" : "",
                    "summary_details_values" : [],
                    "member_details_sql" : "",
                    "member_details_values" : [],
                    "flag_insert_for_summary_details" : False,
                },
                # update_for_existing_cluster
                "sql_for_update_execute" : {
                    "report_sql" : "",
                    "report_sql_values" : [],
                    "summary_sql" : "",
                    "summary_sql_values" : [],
                    "member_sql" : "",
                    "member_sql_values" : [],
                    "summary_details_sql" : "",
                    "summary_details_sql_values" : [],
                    "member_details_sql" : "",
                    "member_details_sql_values" : [],
                    # for active = false
                    "summary_false_sql" : "",
                    "summary_false_sql_values" : [],
                    "summary_false_details_sql" : "",
                    "summary_false_details_sql_values" : [],
                },
                # "sql_for_delete_execute": {
                #     "report_sql" : "",
                #     "report_sql_values" : [],
                #     "summary_sql" : "",
                #     "summary_sql_values" : [],
                #     "member_sql" : "",
                #     "member_sql_values" : [],
                #     "summary_details_sql" : "",
                #     "summary_details_sql_values" : [],
                #     "member_details_sql" : "",
                #     "member_details_sql_values" : [],
                # }
    }

def getFlagData():
    return {
                "flag_representative" : 0,
                "flag_index_source_data_detail" : 0,
                "flag_index_representative" : 0,
                "flag_index_source_data_no_detail" : 0,
                "flag_continuity" : False,
                "flag_representative_id_list" : [],
                "flag_representative_list_df" : [],
                "flag_representative_update" : "",
                "flag_representative_update_start_date" : "",
                "flag_representative_update_end_date" : "",
                "flag_index_source_data_sum" : 0,
                "flag_update_report": False,
                "flag_rollback_process": []
            }
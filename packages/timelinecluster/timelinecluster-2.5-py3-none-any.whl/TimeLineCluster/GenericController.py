import TimeLineCluster.LogController as LogController
import TimeLineCluster.UtilsController as UtilsController
from datetime import datetime
import sys, os

class GenericControllerClass:
    def __init__(self, data_for_time_line_cluster):
        self.app_name = data_for_time_line_cluster["app_name"]
        self.log = LogController.LogController("", data_for_time_line_cluster["app_name"], data_for_time_line_cluster["log_path"])
        self.data_app_config = data_for_time_line_cluster["data_app_config"]
        self.msg_error = ""
        self.process_status = True

        self.controller_app = {
                "member" : data_for_time_line_cluster["controller"]["member"],
                "summary": data_for_time_line_cluster["controller"]["summary"],
                "report" : data_for_time_line_cluster["controller"]["report"]
        }

        if("member_details" in data_for_time_line_cluster["controller"]):
            self.controller_app["member_details"] = data_for_time_line_cluster["controller"]["member_details"]

        if("summary_details" in data_for_time_line_cluster["controller"]):
            self.controller_app["summary_details"] = data_for_time_line_cluster["controller"]["summary_details"]
        
    def exploreCluster(self, connect_db_output, source, unique_source_data, i,source_by_create_date, data_cluster_representative, flag_data, generic):
        try:
            # print("exploreCluster . . .")
            if(len(data_cluster_representative) > 0): # เจอกลุ่ม
                # print("Find cluster ...")
                if(str(data_cluster_representative.iloc[0]["representative_id"]) not in flag_data["flag_representative_id_list"]):
                    flag_data["flag_representative_id_list"].append(str(data_cluster_representative.iloc[0]["representative_id"]))
                    flag_data["flag_representative_list_df"].append(data_cluster_representative)
                flag_data["flag_continuity"] = False
                if("member_details" in self.data_app_config):
                    sql = """
                        select bm.""" + self.data_app_config["member"]["field_pk"] + """, """ + self.data_app_config["member_details"]["field_pk"] + """ from """ + self.data_app_config["output_db"]["member"] + """ bm
                        left join """ + self.data_app_config["output_db"]["member_details"] + """ cm on cm.""" + self.data_app_config["member"]["field_pk"] + """ = bm.""" + self.data_app_config["member"]["field_pk"] + """ and 
                            cm.representative_id = """ + str(data_cluster_representative.iloc[0]["representative_id"]) + """ and 
                            cm.""" + self.data_app_config["member"]["field_partition"] + """ >= '""" + str(data_cluster_representative.iloc[0]["start_date"]) + """' and 
                            cm.""" + self.data_app_config["member"]["field_partition"] + """ <= '""" + str(data_cluster_representative.iloc[0]["end_date"]) + """'
                        where bm.representative_id = """ + str(data_cluster_representative.iloc[0]["representative_id"]) + """ and 
                            bm.""" + self.data_app_config["member"]["field_partition"] + """ >= '""" + str(data_cluster_representative.iloc[0]["start_date"]) + """' and 
                            bm.""" + self.data_app_config["member"]["field_partition"] + """ <= '""" + str(data_cluster_representative.iloc[0]["end_date"]) + """'
                    """
                    sql_where_survey = ""
                    for source_detail in source_by_create_date.iloc:
                        if(sql_where_survey == ""):
                            sql_where_survey += "and bm." + self.data_app_config["member"]["field_pk"] + " in ('" + source_detail[self.data_app_config["member"]["field_pk"]] +"'"
                        else:
                            sql_where_survey += ",'" + source_detail[self.data_app_config["member"]["field_pk"]] + "'"
                    sql_where_survey += ") order by bm." + self.data_app_config["member"]["field_pk"] + " asc"
                    sql += sql_where_survey
                else:
                    sql = """
                        select bm.""" + self.data_app_config["member"]["field_pk"] + """ from """ + self.data_app_config["output_db"]["member"] + """ bm
                        where bm.representative_id = """ + str(data_cluster_representative.iloc[0]["representative_id"]) + """ and 
                            bm.""" + self.data_app_config["member"]["field_partition"] + """ >= '""" + str(data_cluster_representative.iloc[0]["start_date"]) + """' and 
                            bm.""" + self.data_app_config["member"]["field_partition"] + """ <= '""" + str(data_cluster_representative.iloc[0]["end_date"]) + """' 
                        order by bm.""" + self.data_app_config["member"]["field_pk"] + """ asc
                    """
                data_member = connect_db_output.queryRead(sql)
                source_duplicate = []
                if(len(data_member) > 0):
                    source_duplicate = data_member.drop_duplicates([self.data_app_config["member"]["field_pk"]]) # duplicates source data detail

                if(len(source_duplicate) == 0):
                    source_for_insert = source_by_create_date # for insert
                    return [True, source_for_insert, [], flag_data, data_member] 

                if(len(source_duplicate) == len(source_by_create_date) and len(source_duplicate) != 0):
                    return [True, [], source_duplicate, flag_data, data_member] # for update
                else:
                    source_for_insert = source_by_create_date[~source_by_create_date[self.data_app_config["member"]["field_pk"]].isin(source_duplicate[self.data_app_config["member"]["field_pk"]])] # for insert
                    source_for_update = source_by_create_date[source_by_create_date[self.data_app_config["member"]["field_pk"]].isin(source_duplicate[self.data_app_config["member"]["field_pk"]])]  # for update
                    return [True, source_for_insert, source_for_update, flag_data, data_member] # for insert, update
            
            # print("New cluster ...")

            flag_data["flag_representative_update"] = ""
            if(self.data_app_config["continuity"]["required"]):
                data_continuity = self.checkContinuity(connect_db_output, source, self.data_app_config["continuity"]["n_days"], generic.data_app_config)
                if(len(data_continuity) > 0):
                    if(str(data_continuity.iloc[0]["representative_id"]) not in flag_data["flag_representative_id_list"]):
                        flag_data["flag_representative_id_list"].append(str(data_continuity.iloc[0]["representative_id"]))
                        flag_data["flag_representative_list_df"].append(data_cluster_representative)

                    if(int(data_continuity.iloc[0]["continuity_start_number"]) < 0):
                        flag_data["flag_representative_update_start_date"] = source[self.data_app_config["report"]["field_start_date"]]
                    elif(int(data_continuity.iloc[0]["continuity_end_number"]) < 0):
                        flag_data["flag_representative_update_end_date"] = source[self.data_app_config["report"]["field_start_date"]]
                        
                    flag_data["flag_representative_update"] = str(data_continuity.iloc[0]["representative_id"])
                    return [False, [], [], flag_data, []] # for update continuity
                else:
                    if(len(unique_source_data) == i+1):
                        if(flag_data["flag_continuity"]):
                            flag_data["flag_continuity"] = False
                        return [False, [], [], flag_data, []] # for insert no continuity

                    # source_active_true = source_by_create_date.loc[source_by_create_date['active'] == True]
                    # if(len(source_active_true) == 0):
                    #     flag_data["flag_continuity"] = False
                    #     return [False, [], [], flag_data, []] # for insert
                        
                    continuity_status = True

                    for pk in self.data_app_config["report"]["field_pk"]:
                        if(source[pk] != unique_source_data.iloc[i+1][pk]):
                            continuity_status = False
                            break

                    if(continuity_status):
                        date_format = "%Y-%m-%d"
                        delta = datetime.strptime(unique_source_data.iloc[i+1][self.data_app_config["report"]["field_start_date"]], date_format) - datetime.strptime(source[self.data_app_config["report"]["field_start_date"]], date_format)
                        if(delta.days <= self.data_app_config["continuity"]["n_days"]):
                            flag_data["flag_continuity"] = True
                            return [False, [], [], flag_data, []] # for insert continuity
                            
                    if(flag_data["flag_continuity"]):
                        flag_data["flag_continuity"] = False

            return [False, [], [], flag_data, []] # for insert
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error exploreCluster , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            flag_data = UtilsController.getFlagData()
            return False

    def checkContinuity(self, connect_db_output, source, continuity_day, data_app_config):
        try:

            sql_where_pk = ""
            for pk in data_app_config["report"]["field_pk"]:
                if(sql_where_pk == ""):
                    sql_where_pk += pk + " = '" + source[pk] + "' "
                else:
                    sql_where_pk += "and " + pk + " = '" + source[pk] + "' "

            sql = """
                select representative_id, start_date, end_date, ('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - start_date as continuity_start_number,
                ('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - end_date as continuity_end_number
                from """ + data_app_config["output_db"]["report"] + """
                where 
                    """ + sql_where_pk + """
					and (('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - start_date >= -""" + str(continuity_day) + """ and ('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - start_date < 0 or 
						 ('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - end_date <= """ + str(continuity_day) + """ and ('""" + source[data_app_config["report"]["field_start_date"]] + """'::DATE) - end_date > 0)
                """
            return connect_db_output.queryRead(sql)
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            return False

    def getClusterRepresentative(self, connect_db_output, generic, data_source):
        try: 
            pk_report_start_date = generic.data_app_config["report"]["field_start_date"]

            sql_where_pk = ""
            for pk in generic.data_app_config["report"]["field_pk"]:
                if(sql_where_pk == ""):
                    sql_where_pk += pk + " = '" + data_source[pk] + "' "
                else:
                    sql_where_pk += "and " + pk + " = '" + data_source[pk] + "' "

            # if(data_app_config["continuity"]["required"]):
            #     sql = """select representative_id , start_date , end_date 
            #     from """ + data_app_config["output_db"]["report"] + """
            #     where """ + sql_where_pk +""" and 
            #     ((start_date - """ + str(data_app_config["continuity"]["n_days"]) + """ <= '""" + data_source[pk_report_start_date] + """' and start_date >= '""" + data_source[pk_report_start_date] + """') or
            #     (end_date + """ + str(data_app_config["continuity"]["n_days"])  + """ >= '""" + data_source[pk_report_start_date] + """' and end_date <= '""" + data_source[pk_report_start_date] + """'))"""
            # else:
            #     sql = """select representative_id , start_date , end_date 
            #     from """ + data_app_config["output_db"]["report"] + """
            #     where """ + sql_where_pk +""" and start_date <= '""" + data_source[pk_report_start_date] + """'
            #     and end_date >= '"""+ data_source[pk_report_start_date] +"""' """

            sql = """select representative_id , start_date , end_date 
            from """ + generic.data_app_config["output_db"]["report"] + """
            where """ + sql_where_pk +""" and start_date <= '""" + data_source[pk_report_start_date] + """'
            and end_date >= '""" + data_source[pk_report_start_date] + """' """

            # print("getClusterRepresentative . . .")
            return connect_db_output.queryRead(sql)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error getClusterRepresentative , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False

    def handleProcessMember(self, connect_db_output, source, source_by_create_date, source_detail_by_create_date, source_data_no_detail, model_app, flag_data, sql_data, data_cluster_representative, data_explore_cluster, generic):
        try:
            self.controller_app["member"].processMember(connect_db_output, source, source_by_create_date, source_detail_by_create_date, source_data_no_detail, model_app, flag_data, sql_data, data_cluster_representative, data_explore_cluster, generic)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error handleProcessMember , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False

    def handleProcessSummary(self, connect_db_output, source, source_by_create_date, source_detail_by_create_date, model_app, flag_data, sql_data, data_cluster_representative, generic):
        try:    
            self.controller_app["summary"].processSummary(connect_db_output, source, source_by_create_date, source_detail_by_create_date, model_app, flag_data, sql_data, data_cluster_representative, generic)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error handleProcessSummary , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False
            
    def handleProcessReport(self, source, model_app, flag_data, sql_data, data_cluster_representative, generic):
        try:
            return self.controller_app["report"].processReport(source, model_app, flag_data, sql_data, data_cluster_representative, generic)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error handleProcessReport , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False

    def executeInsertCluster(self, connect_db_output, flag_data, sql_data, generic):
        try:
            flag_data["flag_update_report"] = False
            if(len(sql_data["sql_for_insert_cluster_execute"]["member_sql"]) > 0):
                flag_data["flag_update_report"] = True

                print("Insert cluster member ...")
                sql_member_insert_cluster = sql_data["sql_for_insert_cluster_execute"]["member_sql"]
                if(len(sql_data["sql_for_insert_cluster_execute"]["member_values"]) > 0):
                    sql_data["sql_for_insert_cluster_execute"]["member_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_cluster_execute"]["member_values"]]
                    connect_db_output.queryExecute(sql_member_insert_cluster, sql_data["sql_for_insert_cluster_execute"]["member_values"], "")
                else:
                    connect_db_output.queryExecute(sql_member_insert_cluster, None, "")
                print("Insert cluster member successfully")

                # UtilsController.genLog(sql_member_insert_cluster, "info")
                sql_data["sql_for_insert_cluster_execute"]["member_sql"] = ""
                sql_data["sql_for_insert_cluster_execute"]["member_values"] = []

            if(len(sql_data["sql_for_insert_cluster_execute"]["member_details_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Insert cluster member detail ...")
                sql_member_detail_insert_cluster = sql_data["sql_for_insert_cluster_execute"]["member_details_sql"]
                if(len(sql_data["sql_for_insert_cluster_execute"]["member_details_values"]) > 0):
                    sql_data["sql_for_insert_cluster_execute"]["member_details_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_cluster_execute"]["member_details_values"]]
                    connect_db_output.queryExecute(sql_member_detail_insert_cluster, sql_data["sql_for_insert_cluster_execute"]["member_details_values"], "")
                else:
                    connect_db_output.queryExecute(sql_member_detail_insert_cluster, None, "")
                print("Insert cluster member detail successfully")

                # UtilsController.genLog(sql_member_detail_insert_cluster, "info")
                sql_data["sql_for_insert_cluster_execute"]["member_details_sql"] = ""
                sql_data["sql_for_insert_cluster_execute"]["member_details_values"] = []

            if(len(sql_data["sql_for_insert_cluster_execute"]["summary_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Insert cluster summary ...")
                sql_summary_insert_cluster = sql_data["sql_for_insert_cluster_execute"]["summary_sql"]

                if(len(sql_data["sql_for_insert_cluster_execute"]["summary_values"]) > 0):
                    sql_data["sql_for_insert_cluster_execute"]["summary_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_cluster_execute"]["summary_values"]]
                    connect_db_output.queryExecute(sql_summary_insert_cluster , sql_data["sql_for_insert_cluster_execute"]["summary_values"], "")
                else:
                    connect_db_output.queryExecute(sql_summary_insert_cluster , None, "")
                print("Insert cluster summary successfully")

                # UtilsController.genLog(sql_summary_insert_cluster, "info")
                sql_data["sql_for_insert_cluster_execute"]["summary_sql"] = ""
                sql_data["sql_for_insert_cluster_execute"]["summary_values"] = []
                
            if(len(sql_data["sql_for_insert_cluster_execute"]["summary_details_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Insert cluster summary detail ...")
                sql_summary_detail_insert_cluster = sql_data["sql_for_insert_cluster_execute"]["summary_details_sql"]

                if(len(sql_data["sql_for_insert_cluster_execute"]["summary_details_values"]) > 0):
                    sql_data["sql_for_insert_cluster_execute"]["summary_details_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_cluster_execute"]["summary_details_values"]]
                    connect_db_output.queryExecute(sql_summary_detail_insert_cluster, sql_data["sql_for_insert_cluster_execute"]["summary_details_values"], "")
                else:
                    connect_db_output.queryExecute(sql_summary_detail_insert_cluster, sql_data["sql_for_insert_cluster_execute"]["summary_details_values"], "")
                print("Insert cluster summary detail successfully")
                # UtilsController.genLog(sql_summary_detail_insert_cluster, "info")
                sql_data["sql_for_insert_cluster_execute"]["summary_details_sql"] = ""
                sql_data["sql_for_insert_cluster_execute"]["summary_details_values"] = []
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error executeInsertCluster , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            flag_data = UtilsController.getFlagData()
            sql_data = UtilsController.getSql()
            return False

    def executeInsertNewCluster(self, connect_db_output, flag_data, sql_data, generic):
        try:
            if(len(sql_data["sql_for_insert_execute"]["report_sql"]) > 0):
                print("Insert new cluster report ...")
                sql_report_insert = sql_data["sql_for_insert_execute"]["report_sql"]
                if(len(sql_data["sql_for_insert_execute"]["report_values"]) > 0):
                    my_cursor = connect_db_output.queryExecute(sql_report_insert, sql_data["sql_for_insert_execute"]["report_values"], "fetchone")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_report_insert, None, "fetchone")
                print("Insert new cluster report successfully")
                sql_data = self.replaceSqlReport(sql_data, my_cursor, connect_db_output.flag_return_data[0])
                print("Insert new cluster member ...")

                sql_member_insert = sql_data["sql_for_insert_execute"]["member_sql"]

                # UtilsController.genLog(sql_member_insert, "info")
                if(len(sql_data["sql_for_insert_execute"]["member_values"]) > 0):
                    connect_db_output.queryExecute(sql_member_insert, sql_data["sql_for_insert_execute"]["member_values"], "")
                else:
                    connect_db_output.queryExecute(sql_member_insert, None, "")
                print("Insert new cluster member successfully")
                if(len(sql_data["sql_for_insert_execute"]["member_details_sql"]) > 0):
                    print("Insert new cluster member detail ...")
                    sql_member_detail_insert = sql_data["sql_for_insert_execute"]["member_details_sql"]

                    if(len(sql_data["sql_for_insert_execute"]["member_details_values"]) > 0):
                        connect_db_output.queryExecute(sql_member_detail_insert, sql_data["sql_for_insert_execute"]["member_details_values"], "")
                    else:
                        connect_db_output.queryExecute(sql_member_detail_insert, None, "")
                    print("Insert new cluster member detail successfully")
                    # UtilsController.genLog(sql_member_detail_insert, "info")       

                if(len(sql_data["sql_for_insert_execute"]["summary_sql"]) > 0):
                    print("Insert new cluster summary ...")
                    sql_summary_insert = sql_data["sql_for_insert_execute"]["summary_sql"]
                    if(len(sql_data["sql_for_insert_execute"]["summary_values"]) > 0):
                        connect_db_output.queryExecute(sql_summary_insert , sql_data["sql_for_insert_execute"]["summary_values"], "")
                    else:
                        connect_db_output.queryExecute(sql_summary_insert , None, "")
                    print("Insert new cluster summary successfully")
                # UtilsController.genLog(sql_summary_insert, "info")

                if(len(sql_data["sql_for_insert_execute"]["summary_details_sql"]) > 0):
                    print("Insert new cluster summary detail ...")
                    sql_summary_detail_insert = sql_data["sql_for_insert_execute"]["summary_details_sql"]
                    if(len(sql_data["sql_for_insert_execute"]["summary_details_values"]) > 0):
                        connect_db_output.queryExecute(sql_summary_detail_insert, sql_data["sql_for_insert_execute"]["summary_details_values"], "")
                    else:
                        connect_db_output.queryExecute(sql_summary_detail_insert, None, "")
                    print("Insert new cluster summary detail successfully")
                    # UtilsController.genLog(sql_summary_detail_insert, "info")

                sql_data["sql_for_insert_execute"]["report_sql"] = ""
                sql_data["sql_for_insert_execute"]["member_sql"] = ""
                sql_data["sql_for_insert_execute"]["member_details_sql"] = ""
                sql_data["sql_for_insert_execute"]["summary_sql"] = ""
                sql_data["sql_for_insert_execute"]["summary_details_sql"] = ""

                sql_data["sql_for_insert_execute"]["report_values"] = []
                sql_data["sql_for_insert_execute"]["member_values"] = []
                sql_data["sql_for_insert_execute"]["member_details_values"] = []
                sql_data["sql_for_insert_execute"]["summary_values"] = []
                sql_data["sql_for_insert_execute"]["summary_details_values"] = []

                flag_data["flag_index_representative"] = 0
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error executeInsertNewCluster , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            flag_data = UtilsController.getFlagData()
            sql_data = UtilsController.getSql()
            return False

    def executeSQLUpdateCluster(self, connect_db_output, flag_data, sql_data, generic):
        try:     
            if(len(sql_data["sql_for_update_execute"]["member_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Update member ...")
                sql_member_update = sql_data["sql_for_update_execute"]["member_sql"]
                if(len(sql_data["sql_for_update_execute"]["member_sql_values"]) > 0):
                    sql_data["sql_for_update_execute"]["member_sql_values"] = [None if i is 'null' else i for i in sql_data["sql_for_update_execute"]["member_sql_values"]]
                    my_cursor = connect_db_output.queryExecute(sql_member_update, sql_data["sql_for_update_execute"]["member_sql_values"], "")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_member_update, None, "")
                print("Update member successfully ...")
                # UtilsController.genLog(sql_member_update, "info")
                sql_data["sql_for_update_execute"]["member_sql"] = ""
                sql_data["sql_for_update_execute"]["member_sql_values"] = []

            if(len(sql_data["sql_for_update_execute"]["member_details_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Update member detail ...")
                sql_member_detail_update = sql_data["sql_for_update_execute"]["member_details_sql"]
                if(len(sql_data["sql_for_update_execute"]["member_details_sql_values"]) > 0):
                    sql_data["sql_for_update_execute"]["member_details_sql_values"] = [None if i is 'null' else i for i in sql_data["sql_for_update_execute"]["member_details_sql_values"]]
                    my_cursor = connect_db_output.queryExecute(sql_member_detail_update, sql_data["sql_for_update_execute"]["member_details_sql_values"], "")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_member_detail_update, None, "")
                print("Update member detail successfully ...")
                # UtilsController.genLog(sql_member_detail_update, "info")
                sql_data["sql_for_update_execute"]["member_details_sql"] = ""
                sql_data["sql_for_update_execute"]["member_details_sql_values"] = []

            if(len(sql_data["sql_for_update_execute"]["summary_sql"]) > 0):
                flag_data["flag_update_report"] = True
                print("Update summary...")
                sql_summary_update = sql_data["sql_for_update_execute"]["summary_sql"]
                if(len(sql_data["sql_for_update_execute"]["summary_sql_values"]) > 0):
                    sql_data["sql_for_update_execute"]["summary_sql_values"] = [None if i is 'null' else i for i in sql_data["sql_for_update_execute"]["summary_sql_values"]]
                    my_cursor = connect_db_output.queryExecute(sql_summary_update, sql_data["sql_for_update_execute"]["summary_sql_values"], "")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_summary_update, None, "")
                print("Update summary successfully...")
                if(my_cursor.rowcount == 0 and len(sql_data["sql_for_update_execute"]["summary_false_sql"]) and len(sql_data["sql_for_update_execute"]["summary_false_sql_values"])):
                    # all active false
                    my_cursor = connect_db_output.queryExecute(sql_data["sql_for_update_execute"]["summary_false_sql"], sql_data["sql_for_update_execute"]["summary_false_sql_values"], "")
                # UtilsController.genLog(sql_summary_update, "info")
                sql_data["sql_for_update_execute"]["summary_sql"] = ""
                sql_data["sql_for_update_execute"]["summary_sql_values"] = []
                sql_data["sql_for_update_execute"]["summary_false_sql"] = ""
                sql_data["sql_for_update_execute"]["summary_false_sql_values"] = []
            
            if(len(sql_data["sql_for_update_execute"]["summary_details_sql"]) > 0):
                print("Update summary detail ...")
                flag_data["flag_update_report"] = True
                sql_summary_detail_update = sql_data["sql_for_update_execute"]["summary_details_sql"]
                if(len(sql_data["sql_for_update_execute"]["summary_details_sql_values"]) > 0):
                    sql_data["sql_for_update_execute"]["summary_details_sql_values"] = [None if i is 'null' else i for i in sql_data["sql_for_update_execute"]["summary_details_sql_values"]]
                    my_cursor = connect_db_output.queryExecute(sql_summary_detail_update, sql_data["sql_for_update_execute"]["summary_details_sql_values"], "fetchall")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_summary_detail_update, None, "fetchall")
                print("Update summary detail successfully...")
                if(my_cursor.rowcount == 0 and len(sql_data["sql_for_update_execute"]["summary_false_details_sql"]) and len(sql_data["sql_for_update_execute"]["summary_false_details_sql_values"])):
                    # all active false
                    my_cursor = connect_db_output.queryExecute(sql_data["sql_for_update_execute"]["summary_false_details_sql"], sql_data["sql_for_update_execute"]["summary_false_details_sql_values"], "")
                else:
                    if(connect_db_output.flag_return_data != None):
                        data_update = connect_db_output.flag_return_data
                        if(len(data_update) > 0):
                            my_cursor = connect_db_output.queryExecute(self.controller_app["summary"].genSummaryDetailFalseUpdate(data_update, generic), None, "")
                # UtilsController.genLog(sql_summary_detail_update, "info")
                sql_data["sql_for_update_execute"]["summary_details_sql"] = ""
                sql_data["sql_for_update_execute"]["summary_details_sql_values"] = []
                sql_data["sql_for_update_execute"]["summary_false_details_sql"] = ""
                sql_data["sql_for_update_execute"]["summary_false_details_sql_values"] = []

            if(flag_data["flag_update_report"]):
                print("Update report ...")
                sql_data["sql_for_update_execute"] = self.controller_app["report"].genSqlReportUpdateByRepresentativeProcess(connect_db_output, sql_data["sql_for_update_execute"], flag_data["flag_representative_list_df"], generic)
                sql_report_update = sql_data["sql_for_update_execute"]["report_sql"]
                # UtilsController.genLog(sql_report_update, "info")
                if(len(sql_data["sql_for_update_execute"]["report_sql_values"]) > 0):
                    my_cursor = connect_db_output.queryExecute(sql_report_update, sql_data["sql_for_update_execute"]["report_sql_values"], "")
                else:
                    my_cursor = connect_db_output.queryExecute(sql_report_update, None, "")
                sql_data["sql_for_update_execute"]["report_sql"] = ""
                sql_data["sql_for_update_execute"]["report_sql_values"] = []
                print("Update report successfully ...")

                print("Check Representative Date ...")
                sql_update_date = self.genSqlUpdateRepresentativeDate(connect_db_output, flag_data["flag_representative_id_list"], generic)
                if(sql_update_date != "" and sql_update_date != False):
                    my_cursor = connect_db_output.queryExecute(sql_update_date, None, "")
                flag_data["flag_representative_id_list"] = []
                flag_data["flag_representative_list_df"] = []
                print("Check Representative Date successfully ...")

        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error executeSQLUpdateCluster , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            flag_data = UtilsController.getFlagData()
            sql_data = UtilsController.getSql()
            return False 
    
    def executeSQLForProcess(self, connect_db_output, flag_data, sql_data, generic):
        try:
            # self.controller_app["report"].set_sql_insert(self.controller_app["report"], generic.data_app_config)

            # if(sql_data["sql_for_delete_execute"]["member_details"] != ""): # delete no detail
            #     sql_member_detail_delete = sql_data["sql_for_delete_execute"]["member_details"]
            #     my_cursor = connect_db_output.queryExecute(sql_member_detail_delete, None, "")
            #     # UtilsController.genLog(sql_member_detail_delete, "info")
            #     sql_data["sql_for_delete_execute"]["member_details"] = ""

            # insert member, member detail for existing cluster 
            flag_data["flag_update_report"] = False
            if(self.executeInsertCluster(connect_db_output, flag_data, sql_data, generic) == False):
                return False
            # insert report, member, member detail, summary, summary detail for new cluster
            if(self.executeInsertNewCluster(connect_db_output, flag_data, sql_data, generic) == False):
                return False
            # update report, member, member detail, summary, summary detail for existing cluster
            if(self.executeSQLUpdateCluster(connect_db_output, flag_data, sql_data, generic) == False):
                return False

            print("Process successfully !!!")
            return True
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error executeSQLForProcess , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False

    def replaceSqlReport(self , sql_data, my_cursor, representative_id):
        representative_id_new = int(representative_id)

        for i in range(my_cursor.rowcount):
            sql_data["sql_for_insert_execute"]["member_values"] = list(map(lambda x: x.replace('representative_id'  + str(i), str(representative_id_new + i)), sql_data["sql_for_insert_execute"]["member_values"]))
            sql_data["sql_for_insert_execute"]["summary_values"] = list(map(lambda x: x.replace('representative_id'  + str(i), str(representative_id_new + i)), sql_data["sql_for_insert_execute"]["summary_values"]))
            if(len(sql_data["sql_for_insert_execute"]["member_details_values"]) > 0):
                sql_data["sql_for_insert_execute"]["member_details_values"] = list(map(lambda x: x.replace('representative_id'  + str(i), str(representative_id_new + i)), sql_data["sql_for_insert_execute"]["member_details_values"]))
            if(len(sql_data["sql_for_insert_execute"]["summary_details_values"]) > 0):
                sql_data["sql_for_insert_execute"]["summary_details_values"] = list(map(lambda x: x.replace('representative_id'  + str(i), str(representative_id_new + i)), sql_data["sql_for_insert_execute"]["summary_details_values"]))

        sql_data["sql_for_insert_execute"]["member_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_execute"]["member_values"]]
        sql_data["sql_for_insert_execute"]["summary_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_execute"]["summary_values"]]
        
        if(len(sql_data["sql_for_insert_execute"]["member_details_values"]) > 0):
            sql_data["sql_for_insert_execute"]["member_details_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_execute"]["member_details_values"]]
        if(len(sql_data["sql_for_insert_execute"]["summary_details_values"]) > 0):
            sql_data["sql_for_insert_execute"]["summary_details_values"] = [None if i is 'null' else i for i in sql_data["sql_for_insert_execute"]["summary_details_values"]]
        return sql_data

    def genSqlUpdateRepresentativeDate(self, connect_db_output, flag_representative_id_list, generic):
        try:
            # check active ture for start_date end_date
            sql_for_update = ""
            for representative_id in flag_representative_id_list:
                sql = """select lsr.representative_id, summary_date
                        from """ + generic.data_app_config["output_db"]["report"] + """ lsr 
                        inner join """ + generic.data_app_config["output_db"]["summary"] + """ ps on ps.representative_id = lsr.representative_id
                        where lsr.representative_id = """ + str(representative_id) + """ and ps.active = true
                        order by summary_date
                        """
                data_summary_date = connect_db_output.queryRead(sql)

                if(len(data_summary_date) == 1): # one record 
                    start_date = str(data_summary_date.iloc[0]["summary_date"])
                    end_date = str(data_summary_date.iloc[0]["summary_date"])
                elif(len(data_summary_date) > 0): # one more record
                    start_date = str(data_summary_date.iloc[0]["summary_date"])
                    end_date = str(data_summary_date.iloc[len(data_summary_date)-1]["summary_date"])
                else:
                    return False
                
                sql_for_update += """update """ + generic.data_app_config["output_db"]["report"] + """ 
                set start_date = '""" + start_date + """', end_date = '""" + end_date + """' 
                where representative_id = """ + str(representative_id) + """;
                """
            return sql_for_update
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            generic.process_status = False
            generic.log.text_long += "Error genSqlUpdateRepresentativeDate , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            return False
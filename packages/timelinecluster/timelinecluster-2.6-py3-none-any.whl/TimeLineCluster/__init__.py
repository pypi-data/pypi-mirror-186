import TimeLineCluster.GenericController as GenericController
import TimeLineCluster.UtilsController as UtilsController
import TimeLineCluster.DBConnector as DBConnector 
from datetime import datetime
import sys, os
class TimeLineClusterClass:
    def __init__(self, data_for_time_line_cluster) :
        # if(~UtilsController.fileExists(data_for_time_line_cluster["data_app_config"])):
        #     self.status = False
        #     print("Data app config not found !!")
        #     return
        if(UtilsController.fileExists(data_for_time_line_cluster["log_path"]) == False):
            self.status = False
            print("Log path config not found !!")
            return

        if(len(data_for_time_line_cluster["controller"]) >= 3):
            if("member" in data_for_time_line_cluster["controller"] and "summary" in data_for_time_line_cluster["controller"] and "report" in data_for_time_line_cluster["controller"]):
                self.generic = GenericController.GenericControllerClass(data_for_time_line_cluster)
        else:
            self.status = False
            print("Controller not found !!")
            return 

        self.app_name = data_for_time_line_cluster["app_name"]
        self.generic = GenericController.GenericControllerClass(data_for_time_line_cluster)
        self.connect_db_output = DBConnector.ConnectDB(self.generic.data_app_config["output_db"]["host"], self.generic.data_app_config["output_db"]["port"], self.generic.data_app_config["output_db"]["database"] , self.generic.data_app_config["output_db"]["user"] ,self.generic.data_app_config["output_db"]["password"])
        self.connect_db_output.connect_to_db(1,1)  # connect db output 
        self.flag_data = UtilsController.getFlagData()
        self.sql_data = UtilsController.getSql()
        self.source_data = ""
        self.source_detail_data = ""

        self.store_for_time_line_cluster = data_for_time_line_cluster
        self.model_app = self.store_for_time_line_cluster["model"]

        # self.data_for_time_line_cluster = data_for_time_line_cluster

        self.pk_report_name = self.generic.data_app_config["report"]["field_pk"]
        self.pk_report_start_date = self.generic.data_app_config["report"]["field_start_date"]

        self.pk_member_name = ""
        if("field_pk" in self.generic.data_app_config["member"]):
            self.pk_member_name = self.generic.data_app_config["member"]["field_pk"]

        self.pk_member_detail_start_date = ""
        if("member_details" in self.generic.data_app_config): 
            if("field_partition" in self.generic.data_app_config["member_details"]):          
                self.pk_member_detail_start_date = self.generic.data_app_config["member_details"]["field_partition"]

        self.status = True
        
        self.last_process_fail = {}
        self.for_drop_report = []
        self.first_update_source = []
        self.last_update_source = []
        self.unique_source_data = []

    def setSource(self, source_data, source_detail_data):
        self.source_data = source_data
        self.source_detail_data = source_detail_data

    def run(self):
        try:
            self.last_process_fail = {} # Reset
            if(self.generic.data_app_config == "" or self.generic.data_app_config == False or self.generic.data_app_config == None):
                self.status = False
                return
            if(self.status):

                source_data = self.source_data
                source_data_no_detail = []
                
                if(len(source_data) > 0): # check source data for process
                        
                    self.flag_data = UtilsController.getFlagData()
                    self.sql_data = UtilsController.getSql()
                        
                    if(self.connect_db_output.conn == False or self.connect_db_output.conn == None): # connect db output 
                        print("Connect database output")
                        self.connect_db_output.connect_to_db(1,1)

                    # last_update_source = UtilsController.readFileJson(self.store_for_time_line_cluster["last_update_path"]) # get last update timestamp

                    # if(last_update_source == False): # Check last update not found or Error readFileJson function ??
                    #     self.connect_db_output.closeAllConnection("output")
                    #     self.status = False
                    #     self.generic.log.text_long += "last update not found or Error readFileJson function."
                    #     # self.generic.log.genLog(self.generic.log.text_long, "error")
                    #     return False    

                    self.first_update_source = source_data.iloc[0] # store first update timestamp
                    self.last_update_source = source_data.iloc[len(source_data)-1] # store max update timestamp

                    # sort data by pk, start_date
                    for_drop = []
                    ascending_list = []
                    for pk in self.generic.data_app_config["report"]["field_pk"]:
                        for_drop.append(pk)
                        ascending_list.append(True)
                    for_drop.append(self.generic.data_app_config["report"]["field_start_date"])
                    ascending_list.append(True)
                    source_data = source_data.sort_values(for_drop, ascending=ascending_list)
                     # end sort data by pk, start_date

                    self.for_drop_report = self.getPkReport(self.pk_report_name)
                    
                    for_drop_source = self.for_drop_report + [self.pk_report_start_date]
                    self.unique_source_data = source_data.drop_duplicates(for_drop_source) # duplicates source data for process
                    if(len(self.source_detail_data) > 0):
                        source_detail_data = self.source_detail_data
                        unique_source_detail_data = source_detail_data.drop_duplicates([self.pk_member_name]) # duplicates source data detail for process
                        if(len(source_data) != len(unique_source_detail_data)): # check source data no detail
                            source_data_no_detail = source_data[~source_data[self.pk_member_name].isin(unique_source_detail_data[self.pk_member_name])]
                            
                    self.model_app["report"] = self.store_for_time_line_cluster["model"]["report"]
                    data_explore_cluster = []

                    for i , source in enumerate(self.unique_source_data.iloc): # self.pk_report_name, self.pk_report_start_date
                        self.generic.data_app_config = self.store_for_time_line_cluster["data_app_config"]
                        self.generic.log.text_long = "Process start time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]) + " "
                        
                        self.model_app["summary"] = self.store_for_time_line_cluster["model"]["summary"]
                        self.model_app["summary"].summary_date = source[self.pk_report_start_date]
                        
                        self.sql_data["sql_for_insert_cluster_execute"]["flag_insert_for_summary_details"] = False
                        source_by_create_date = source_data.loc[(source_data[self.pk_report_start_date] == source[self.pk_report_start_date])] # member source 
                        for pk in self.pk_report_name:
                            source_by_create_date = source_by_create_date.loc[(source_by_create_date[pk]  == source[pk])] # member source 

                        if(self.pk_member_detail_start_date != ""):
                            source_detail_by_create_date = source_detail_data.loc[(source_detail_data[self.pk_member_detail_start_date] == source[self.pk_report_start_date])] # member detail source
                            for pk in self.pk_report_name:
                                source_detail_by_create_date = source_detail_by_create_date.loc[(source_detail_by_create_date[pk]  == source[pk])] # member detail source
                        else:
                            source_detail_by_create_date = []

                        self.generic.log.text_long += "Clustering start time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]) + " "
                        data_cluster_representative = self.generic.getClusterRepresentative(self.connect_db_output, self.generic, source) # get cluster
                        if(self.generic.process_status == False):
                            self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
                            return
                        data_explore_cluster = self.generic.exploreCluster(self.connect_db_output, source, self.unique_source_data, i, source_by_create_date, data_cluster_representative, self.flag_data, self.generic) # check cluster
                        if(self.generic.process_status == False):
                            self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
                            return
                        self.generic.log.text_long += "Clustering end time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]) + " "
                        
                        for pk in self.pk_report_name:
                            self.generic.log.text_long += pk + " : " + str(source[pk]) + " "

                        if(self.pk_member_name != ""):
                            self.generic.log.text_long += self.generic.log.convertDf2StringForLog(source_by_create_date, self.pk_member_name) + " "
                        
                        self.generic.handleProcessMember(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, source_data_no_detail, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, data_explore_cluster, self.generic)
                        if(self.generic.process_status == False):
                            self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
                            return
                        self.generic.handleProcessSummary(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, self.generic)
                        if(self.generic.process_status == False):
                            self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
                            return
                        self.generic.handleProcessReport(source, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, self.generic)
                        if(self.generic.process_status == False):
                            self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
                            return
                        # self.model_app["report"] = data_process_report[0] # data model report
                        # self.flag_data = data_process_report[1] # self.flag_data
                        
                        if(self.generic.data_app_config["execute_status"] == 1):
                            self.generic.executeSQLForProcess(self.connect_db_output, self.flag_data, self.sql_data, self.generic)
                        else:
                            self.generic.controller_app["report"].executeSQLForProcess(self.connect_db_output, self.flag_data, self.generic)
                            
                        self.generic.log.text_long += "Process end time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]) + " "
                        
                        if("log_info" in self.generic.data_app_config):
                            if(self.generic.data_app_config["log_info"] == 1):
                                self.generic.log.genLog(self.generic.log.text_long, "info")
                    
                    self.writeFileUpdate()
                
            self.connect_db_output.closeAllConnection("output")
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(error, exc_type, fname, exc_tb.tb_lineno)
            self.status = False
            self.generic.log.text_long += "Error run , " + str(error) + " " + str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " "
            self.flag_data = UtilsController.getFlagData()

            if(len(self.source_data) > 0):
                self.generic.process_status = False
                self.for_drop_report = self.getPkReport(self.pk_report_name)
                for_drop_source = self.for_drop_report + [self.pk_report_start_date]
                self.unique_source_data = self.source_data.drop_duplicates(for_drop_source) # duplicates source data for process
                self.first_update_source = self.source_data.iloc[0] # store first update timestamp
                self.last_update_source = self.source_data.iloc[len(self.source_data)-1] # store max update timestamp
                self.genLogErrorPk(self.for_drop_report, self.unique_source_data, self.first_update_source, self.last_update_source)
            else:
                self.generic.log.genLog(self.generic.log.text_long, "error")
                self.status = False
                self.connect_db_output.closeAllConnection("output")

    def writeFileUpdate(self):
        if("field_last_update_timestamp" in self.generic.data_app_config):
            UtilsController.writeLastUpdateSurveyJson(self.store_for_time_line_cluster["last_update_path"] , self.last_update_source[self.generic.data_app_config["field_last_update_timestamp"]])

    def getPkReport(self, report_name):
        data = []
        for pk in report_name:
            data.append(pk)
        return data

    def genLogErrorPk(self, for_drop_report, unique_source_data, first_update_source, last_update_source):
        self.generic.process_status = True
        if("field_last_update_timestamp" in self.generic.data_app_config):
            self.writeFileUpdate()
            self.generic.log.text_long += " | [update_timestamp : " + last_update_source[self.generic.data_app_config["field_last_update_timestamp"]] + " "
            self.last_process_fail["start_date"] = first_update_source[self.generic.data_app_config["field_last_update_timestamp"]]
            self.last_process_fail["end_date"] = last_update_source[self.generic.data_app_config["field_last_update_timestamp"]]
            
        i = 0
        pk_list = []
        for pk in for_drop_report:
            for source_pk in unique_source_data[pk]:
                pk_list.append(source_pk)

            if(i == 0):
                self.generic.log.text_long += pk + " : " + source_pk
            else:
                self.generic.log.text_long += ", " + pk + " : " + source_pk + " "

            self.last_process_fail[pk] = pk_list
            i += 1

        self.generic.log.text_long += "]"
        self.generic.log.genLog(self.generic.log.text_long, "error")
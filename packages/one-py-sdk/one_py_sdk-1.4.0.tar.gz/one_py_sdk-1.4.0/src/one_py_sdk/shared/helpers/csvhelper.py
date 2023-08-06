import csv
import json
import logging
from one_py_sdk.operations.spreadsheet import SpreadsheetApi
from one_py_sdk.common.library import LibraryApi
from one_py_sdk.enterprise.twin import DigitalTwinApi
from one_py_sdk.common.configuration import ConfigurationApi
from one_py_sdk.historian.data import HistorianApi
from one_py_sdk.shared.helpers.datetimehelper import *
from datetime import datetime, timezone


class Exporter:
    def __init__(self, env, auth):
        self.Environment = env
        self.Authentication = auth
        self.Spreadsheet = SpreadsheetApi(env, auth)
        self.Library = LibraryApi(env, auth)
        self.DigitalTwin = DigitalTwinApi(env, auth)
        self.Configuration = ConfigurationApi(env, auth)
        self.Historian = HistorianApi(env, auth)
    dataFieldNames = ['Worksheet Type', 'Time', 'ColumnName', 'ColumnId',
                      'RowNumber', 'Value', 'StringValue', 'DateEntered', 'ChangedUsing']
    columnFieldNames = ['Worksheet Type', 'ColumnNumber', 'Name', 'ParameterId', 'LocationId', 'LocationName', 'LocationType', 'LocationSubtype', 'Path', 'Latitude', 'Longitude',
                        'ParameterTranslation', 'ColumnId', 'UnitId', 'UnitTranslation', 'LastPopulatedDate', 'DataBinding',
                        'LimitName', "LowValue", "LowOperation", "HighValue", "HighOperation", "LimitStartTime", "LimitEndTime"]
    historianDataFieldNames = ["DateUTC", "Value", "String Value",
                               'Property Bag', "CreatedById", "CreatedOn", "ModifiedById", "ModifiedOn", ]
    limitFieldNames = ["ColumnId", "ColumnName", 'LimitName', "LimitType", "LowValue", "LowOperation",
                       "HighValue", "HighOperation", "LimitStartTime", "LimitEndTime", "NotificationsEnabled"]

    def ExportHistorianTwin(self, filename, twinId, startDate, endDate):
        fieldnames = self.historianDataFieldNames
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            historianData = self.Historian.GetHistorianDataRange(
                twinId, startDate, endDate)
            for datum in historianData:
                worksheetWriter.writerow({"DateUTC": datum.dateTimeUTC.jsonDateTime.value,
                                          "Value": datum.value.value,
                                          "String Value": datum.stringValue.value,
                                          'Property Bag': datum.propertyBag.value,
                                          "CreatedById": datum.recordAuditInfo.createdById,
                                          "CreatedOn": datum.recordAuditInfo.createdOn.jsonDateTime.value,
                                          "ModifiedById": datum.recordAuditInfo.modifiedById,
                                          "ModifiedOn": datum.recordAuditInfo.modifiedOn.jsonDateTime.value})

    def ExportWorksheet(self, filename, plantId, startDate, endDate, updatedAfter=None, wsType=None):
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.dataFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            if not wsType:
                wsTypes = range(1, 5)
                for wsType in wsTypes:
                    try:
                        self.__mapAndWriteRowsAndColumns(
                            worksheetWriter, plantId, wsType, startDate, endDate, updatedAfter)
                    except:
                        logging.error(f"Export for ws type {self.ConvertWSTypeToStringValue(wsType)} ")
                        continue
            else:
                self.__mapAndWriteRowsAndColumns(
                    worksheetWriter, plantId, wsType, startDate, endDate, updatedAfter)

    def __mapAndWriteRowsAndColumns(self, worksheetWriter, plantId, wsType, startDate, endDate, updatedAfter):
        wsVal = self.ConvertWSTypeToStringValue(wsType)
        if not startDate.tzinfo:
            startDate = startDate.replace(tzinfo=timezone.utc)
        if not endDate.tzinfo:
            endDate = endDate.replace(tzinfo=timezone.utc)
        try:
            ws = self.Spreadsheet.GetWorksheetDefinition(plantId, wsType)[0]
        except:           
            return
        if not ws.columns:            
            return
        rows = self.Spreadsheet.GetRowsForTimeRange(
            plantId, wsType, startDate, endDate)
        try:
            rowNumbers = rows.keys()
            rowValues = rows.values()
        except(AttributeError):
            return
        rowDict = {}
        for num in rowNumbers:
            rowDict[num] = str(GetDateFromRowNumber(num, ws.enumWorksheet))

        numberMapping = {}
        for column in ws.columns:
            numberMapping[column.columnNumber] = [column.name, column.columnId]
        for vals in rows.values():
            for cell in vals.cells:
                if updatedAfter != None:
                    try:
                        dateEntered = cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value
                        if dateEntered:
                            dateEntered = self.ParseAuditTime(dateEntered)
                            if not updatedAfter.tzinfo:
                                updatedAfter = updatedAfter.replace(
                                    tzinfo=timezone.utc)
                            if dateEntered > updatedAfter:
                                worksheetWriter.writerow({'Worksheet Type': wsVal,
                                                        'Time': rowDict[vals.rowNumber], 'ColumnName': numberMapping[cell.columnNumber][0],
                                                        'ColumnId': numberMapping[cell.columnNumber][1],
                                                        'Value': cell.cellDatas[0].value.value,
                                                        'RowNumber': vals.rowNumber,
                                                        'StringValue': cell.cellDatas[0].stringValue.value,
                                                        'DateEntered': cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value,
                                                        'ChangedUsing': self.EnumDataSourceToStringValue(cell.cellDatas[0].auditEvents[-1].enumDataSource)})
                        else: 
                            logging.error(f"Audit info not found for Plant: {plantId},'Worksheet Type': {wsVal}, 'ColumnName':{numberMapping[cell.columnNumber][0]},'Time': {rowDict[vals.rowNumber]}, 'Value': {cell.cellDatas[0].value.value} ")
                    except IndexError:
                        pass
                    except TypeError:
                        logging.exception("message")
                        logging.error(
                            f"Input date could not be parsed for'Worksheet Type': {wsVal}, 'ColumnName':{numberMapping[cell.columnNumber][0]},'Time': {rowDict[vals.rowNumber]}, 'Value': {cell.cellDatas[0].value.value}, 'DateEntered':{cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value} ")
                        logging.debug(len(dateEntered))
                    except ValueError:
                        logging.exception("message")
                        logging.error(
                            f"Input date could not be parsed for'Worksheet Type': {wsVal}, 'ColumnName':{numberMapping[cell.columnNumber][0]},'Time': {rowDict[vals.rowNumber]}, 'Value': {cell.cellDatas[0].value.value}, 'DateEntered':{cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value} ")
                        logging.debug(len(dateEntered))
                    except:
                        logging.exception("message")
                        logging.error(
                            f"Input date could not be parsed for'Worksheet Type': {wsVal}, 'ColumnName':{numberMapping[cell.columnNumber][0]},'Time': {rowDict[vals.rowNumber]}, 'Value': {cell.cellDatas[0].value.value}, 'DateEntered':{cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value} ")
                else:
                    try:
                        worksheetWriter.writerow({'Worksheet Type': wsVal,
                                                  'Time': rowDict[vals.rowNumber],
                                                  'ColumnName': numberMapping[cell.columnNumber][0],
                                                  'ColumnId': numberMapping[cell.columnNumber][1],
                                                  'Value': (cell.cellDatas[0].value.value),
                                                  'RowNumber': vals.rowNumber,
                                                  'StringValue': cell.cellDatas[0].stringValue.value,
                                                  'DateEntered': cell.cellDatas[0].auditEvents[-1].timeStamp.jsonDateTime.value,
                                                  'ChangedUsing': self.EnumDataSourceToStringValue(cell.cellDatas[0].auditEvents[-1].enumDataSource)})
                    except(IndexError):
                        pass

    def ExportWorksheetByType(self, filename, plantId, startDate, endDate, wsType=4, updatedAfter=None):
        wsVal = self.ConvertWSTypeToStringValue(wsType)
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.dataFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            self.__mapAndWriteRowsAndColumns(
                worksheetWriter, plantId, wsType, startDate, endDate, updatedAfter)

    def ExportColumnDetails(self, filename, plantId, wsType=None, viewName=""):
        unitDict, paramDict, typeDict, subtypeDict = self.__mapUnitsAndParams()

        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.columnFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            if not wsType:
                wsTypes = range(1, 5)
                for wsType in wsTypes:
                    try:
                        self.__mapAndWriteColumns(
                            plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, viewName)
                    except:
                        raise
                        continue
            else:
                self.__mapAndWriteColumns(
                    plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, viewName)

    def ExportLimitColumns(self, filename, plantId, wsType=None, viewName="", allLimits=False):
        unitDict, paramDict, typeDict, subtypeDict = self.__mapUnitsAndParams()
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.columnFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            if not wsType:
                wsTypes = range(1, 5)
                for wsType in wsTypes:
                    try:
                        self.__mapAndWriteLimitColumns(
                            plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, allLimits, viewName="")
                    except:
                        continue
            else:
                self.__mapAndWriteLimitColumns(
                    plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, allLimits, viewName="")

    def ExportLimits(self, filename, plantId, wsType=None):
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.limitFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            if not wsType:
                wsTypes = range(1, 5)
                for wsType in wsTypes:
                    wsVal = self.ConvertWSTypeToStringValue(wsType)
            try:
                ws = self.Spreadsheet.GetWorksheetDefinition(plantId, wsType)[
                    0]
            except:
                return
            if not ws.columns:
                return
            columnDict = {}
            for column in ws.columns:
                if column.limits:
                    columnDict[column.columnId] = [column.name, column.limits]

            for key in columnDict.keys():
                for lim in columnDict[key][1]:
                    worksheetWriter.writerow({
                        'ColumnId': key,
                        'ColumnName': columnDict[key][0],
                        'LimitName': lim.name,
                        'LimitType': self.ConvertLimitEnumToStringValue(lim.enumLimit),
                        'LowValue': lim.lowValue.value,
                        "LowOperation": self.LimitOperationToStringValue(lim.lowOperation),
                        "HighValue": lim.highValue.value,
                        "HighOperation": self.LimitOperationToStringValue(lim.highOperation),
                        "LimitStartTime": lim.timeWindow.startTime.jsonDateTime.value,
                        "LimitEndTime": lim.timeWindow.endTime.jsonDateTime.value,
                        "NotificationsEnabled": lim.notificationFlag
                    })

    def __mapAndWriteLimitColumns(self, plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, allLimits, viewName):
        wsVal = self.ConvertWSTypeToStringValue(wsType)
        try:
            ws = self.Spreadsheet.GetWorksheetDefinition(plantId, wsType)[0]
        except:
            return
        if not ws.columns:
            return

        columnDict = {}
        for column in ws.columns:
            columnDict[column.columnNumber] = [column.name,  column.columnId, column.parameterId,  column.displayUnitId,
                                               column.lastRowNumberWithData, column.locationId, column.limits, column.dataSourceBinding]
        limitDict = {}
        for column in columnDict.values():
            try:
                limit = column[6][0]
                if allLimits:
                    limitDict[column[1]] = [limit.name, limit.lowValue.value, limit.lowOperation, limit.highValue.value,
                                            limit.highOperation,  limit.timeWindow.startTime.jsonDateTime.value, limit.timeWindow.endTime.jsonDateTime.value]
                else:
                    if limit.enumLimit == 5 or limit.enumLimit == 4 or limit.enumLimit == 1:
                        limitDict[column[1]] = [limit.name, limit.lowValue.value, limit.lowOperation, limit.highValue.value,
                                                limit.highOperation,  limit.timeWindow.startTime.jsonDateTime.value, limit.timeWindow.endTime.jsonDateTime.value]

            except:
                pass

        twinDict = self.PathFinder(plantId, columnDict)
        for key in columnDict.keys():
            try:
                try:
                    dataSourceBinding = columnDict[key][7]
                except:
                    dataSourceBinding = ""
                locationSubtype = subtypeDict[twinDict[columnDict[key][5]][5]][1]
                locationType = typeDict[twinDict[columnDict[key][5]][4]][1]
                lat = twinDict[columnDict[key][1]][6]
                long = twinDict[columnDict[key][1]][7]
                worksheetWriter.writerow({'ColumnNumber': key,
                                          'Name': columnDict[key][0],
                                          'ColumnId': columnDict[key][1],
                                          'Worksheet Type': wsVal,
                                          'ParameterId': columnDict[key][2],
                                          'UnitId': columnDict[key][3],
                                          'LocationName': twinDict[columnDict[key][1]][3],
                                          'LastPopulatedDate': GetDateFromRowNumber(columnDict[key][4], wsType),
                                          'UnitTranslation': unitDict[columnDict[key][3]][2],
                                          'LocationId': columnDict[key][5],
                                          'LocationType': locationType,
                                          'ParameterTranslation': paramDict[columnDict[key][2]][1],
                                          "Path": twinDict[columnDict[key][1]][2],
                                          "Latitude": lat,
                                          "Longitude": long,
                                          'LimitName':  limitDict[columnDict[key][1]][0],
                                          "LowValue": limitDict[columnDict[key][1]][1],
                                          "LowOperation": self.LimitOperationToStringValue(limitDict[columnDict[key][1]][2]),
                                          "HighValue": limitDict[columnDict[key][1]][3],
                                          "HighOperation": self.LimitOperationToStringValue(limitDict[columnDict[key][1]][4]),
                                          "LimitStartTime": limitDict[columnDict[key][1]][5],
                                          "LimitEndTime": limitDict[columnDict[key][1]][6],
                                          "LocationSubtype": locationSubtype,
                                          "DataBinding": dataSourceBinding

                                          })
            except (KeyError):
                pass

    def __mapAndWriteColumns(self, plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, viewName=""):
        wsVal = self.ConvertWSTypeToStringValue(wsType)
        try:
            ws = self.Spreadsheet.GetWorksheetDefinition(plantId, wsType)[0]
        except:
            return
        if not ws.columns:
            return

        if (viewName != ""):
            configsInPlant = self.Configuration.GetSpreadsheetViews(plantId)
            configsWithName = [config.configurationData for config in configsInPlant if json.loads(
                config.configurationData).get('name') == viewName]
            columnNumbersInConfig = [json.loads(jsData).get(
                'columnNumbers') for jsData in configsWithName]
            columnsInView = []
            for lst in columnNumbersInConfig:
                for item in lst:
                    columnsInView.append(item)

        columnDict = {}
        for column in ws.columns:
            if (viewName != ""):
                if(column.columnNumber in columnsInView):
                    columnDict[column.columnNumber] = [column.name,  column.columnId, column.parameterId,  column.displayUnitId,
                                                       column.lastRowNumberWithData, column.locationId, column.limits, column.dataSourceBinding.bindingId]
            else:
                columnDict[column.columnNumber] = [column.name,  column.columnId, column.parameterId,  column.displayUnitId,
                                                   column.lastRowNumberWithData, column.locationId, column.limits, column.dataSourceBinding.bindingId]
        limitDict = {}
        for column in columnDict.values():
            try:
                limit = column[6][0]
                if limit.enumLimit == 5 or limit.enumLimit == 4 or limit.enumLimit == 1:
                    limitDict[column[1]] = [limit.name, limit.lowValue.value, limit.lowOperation, limit.highValue.value,
                                            limit.highOperation,  limit.timeWindow.startTime.jsonDateTime.value, limit.timeWindow.endTime.jsonDateTime.value]

            except:
                pass

        twinDict = self.PathFinder(plantId, columnDict)
        for key in columnDict.keys():
            locationType = typeDict[twinDict[columnDict[key][5]][4]][1]
            try:
                dataSourceBinding = columnDict[key][7]
            except:
                dataSourceBinding = ""
            try:
                locationSubtype = subtypeDict[twinDict[columnDict[key][5]][5]][1]
                lat = twinDict[columnDict[key][1]][6]
                long = twinDict[columnDict[key][1]][7]
                worksheetWriter.writerow({'ColumnNumber': key,
                                          'Name': columnDict[key][0],
                                          'ColumnId': columnDict[key][1],
                                          'Worksheet Type': wsVal,
                                          'ParameterId': columnDict[key][2],
                                          'UnitId': columnDict[key][3],
                                          'LocationName': twinDict[columnDict[key][1]][3],
                                          'LastPopulatedDate': GetDateFromRowNumber(columnDict[key][4], wsType),
                                          'UnitTranslation': unitDict[columnDict[key][3]][2],
                                          'LocationId': columnDict[key][5],
                                          'LocationType': locationType,
                                          'ParameterTranslation': paramDict[columnDict[key][2]][1],
                                          "Path": twinDict[columnDict[key][1]][2],
                                          "Latitude": lat,
                                          "Longitude": long,
                                          'LimitName':  limitDict[columnDict[key][1]][0],
                                          "LowValue": limitDict[columnDict[key][1]][1],
                                          "LowOperation": self.LimitOperationToStringValue(limitDict[columnDict[key][1]][2]),
                                          "HighValue": limitDict[columnDict[key][1]][3],
                                          "HighOperation": self.LimitOperationToStringValue(limitDict[columnDict[key][1]][4]),
                                          "LimitStartTime": limitDict[columnDict[key][1]][5],
                                          "LimitEndTime": limitDict[columnDict[key][1]][6],
                                          "LocationSubtype": locationSubtype,
                                          "DataBinding": dataSourceBinding
                                          })
            except (KeyError):
                locationSubtype = subtypeDict[twinDict[columnDict[key][5]][5]][1]
                lat = twinDict[columnDict[key][1]][6]
                long = twinDict[columnDict[key][1]][7]
                worksheetWriter.writerow({'ColumnNumber': key,
                                          'Name': columnDict[key][0],
                                          'ColumnId': columnDict[key][1],
                                          'Worksheet Type': wsVal,
                                          'ParameterId': columnDict[key][2],
                                          'UnitId': columnDict[key][3],
                                          'LocationName': twinDict[columnDict[key][1]][3],
                                          'LastPopulatedDate': GetDateFromRowNumber(columnDict[key][4], wsType),
                                          'UnitTranslation': unitDict[columnDict[key][3]][2],
                                          'LocationId': columnDict[key][5],
                                          'LocationType': locationType,
                                          'ParameterTranslation': paramDict[columnDict[key][2]][1],
                                          "Path": twinDict[columnDict[key][1]][2],
                                          "Latitude": lat,
                                          "Longitude": long,
                                          "LocationSubtype": locationSubtype,
                                          "DataBinding": dataSourceBinding
                                          })

    def __mapUnitsAndParams(self):
        units = self.Library.GetUnits()
        parameters = self.Library.GetParameters()
        i18N = self.Library.Geti18nKeys("AQI_FOUNDATION_LIBRARY")[
            0].get("AQI_FOUNDATION_LIBRARY")
        i18NUnits = i18N.get("UnitType").get("LONG")
        i18NParams = i18N.get("Parameter").get("LONG")
        i18NSubtypes = i18N.get("DigitalTwinSubType")
        paramDict = {}
        for param in parameters:
            try:
                paramDict[param.IntId] = [
                    param.i18nKey, i18NParams[param.i18nKey]]
            except:
                paramDict[param.IntId] = [param.i18nKey, None]
        unitDict = {}
        for unit in units:
            try:
                unitDict[unit.IntId] = [unit.i18nKey,
                                        unit.unitName, i18NUnits[unit.i18nKey]]
            except:
                unitDict[unit.IntId] = [unit.i18nKey, unit.unitName, None]
        twinTypes = self.DigitalTwin.GetDigitalTwinTypes()
        typeDict = {}
        for twinType in twinTypes:
            typeDict[twinType.id] = [
                twinType.i18NKeyName, twinType.description.value]
        twinSubtypes = self.DigitalTwin.GetDigitalTwinSubtypes()
        subTypeDict = {}
        for subtype in twinSubtypes:
            try:
                subTypeDict[subtype.id] = [subtype.i18NKeyName,
                                           i18NSubtypes[subtype.i18NKeyName]]
            except(KeyError):
                subTypeDict[subtype.id] = [
                    subtype.i18NKeyName, subtype.i18NKeyName]

        return unitDict, paramDict, typeDict, subTypeDict

    def ExportColumnDetailsByType(self, filename, plantId, wsType=4,  viewName=""):
        unitDict, paramDict, typeDict, subtypeDict = self.__mapUnitsAndParams()
        with open(filename, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = self.columnFieldNames
            worksheetWriter = csv.DictWriter(file, fieldnames=fieldnames)
            worksheetWriter.writeheader()
            self.__mapAndWriteColumns(
                plantId, wsType, unitDict, paramDict, worksheetWriter, typeDict, subtypeDict, viewName="")

    def PathFinder(self, plantId, columnDict):
        twins = self.DigitalTwin.GetDescendantsByType(
            plantId, "ae018857-5f27-4fe4-8117-d0cbaecb9c1e", False)
        twins.MergeFrom(
            self.DigitalTwin.GetDescendantsByRefByCategory(plantId, 2, False))
        twins = twins.items
        twinDict = {}
        lat = ""
        long = ""
        for twin in twins:
            lat = twin.geography.point2d.y
            long = twin.geography.point2d.x
            twinDict[twin.twinReferenceId.value] = [twin.parentTwinReferenceId.value,
                                                    twin.name.value, None, None, twin.twinTypeId, twin.twinSubTypeId.value, lat, long]

        for key in columnDict.keys():
            twinId = columnDict[key][1]
            path = []
            twinChain = []
            pathString = ""
            while (twinId != plantId):
                path.append(twinDict[twinId][1])
                twinChain.append(twinId)
                twinId = twinDict[twinId][0]
            path.append(twinDict[twinId][1])
            twinChain.append(plantId)
            for twinRef in twinChain:
                if not twinDict[twinRef][6] or not twinDict[twinRef][7]:
                    lat = ""
                    long = ""
                else:
                    lat = twinDict[twinRef][6]
                    long = twinDict[twinRef][7]
                if lat and long:
                    break

            twinDict[twinChain[0]][6] = lat
            twinDict[twinChain[0]][7] = long
            twinDict[columnDict[key][1]][3] = path[1]
            while (path):
                pathString = f'{pathString}/{path.pop()}'
            twinDict[columnDict[key][1]][2] = pathString
        return twinDict

    def ConvertWSTypeToStringValue(self, wsType):
        if wsType == 1:
            return "Fifteen Minute"
        elif wsType == 2:
            return "Hourly"
        elif wsType == 3:
            return "Four Hour"
        elif wsType == 4:
            return "Daily"
        else:
            return print("Enter valid worksheet type value (1= Fifteen minute, 2=Hourly, 3=FourHour, 4=Daily)")

    def ConvertLimitEnumToStringValue(self, limitEnum):
        if limitEnum == 1:
            return "Regulatory"
        elif limitEnum == 2:
            return "Warning"
        elif limitEnum == 3:
            return "Warning"
        elif limitEnum == 4:
            return "Regulatory"
        elif limitEnum == 5:
            return "Regulatory"
        elif limitEnum == 6:
            return "Warning"
        elif limitEnum == 7:
            return "Goal"
        else:
            return print("Enter valid worksheet type value (1-7)")

    def LimitOperationToStringValue(self, limitOperation):
        if limitOperation == 1:
            return ">"
        elif limitOperation == 2:
            return ">="
        elif limitOperation == 3:
            return "<"
        elif limitOperation == 4:
            return "=<"
        elif limitOperation == 0:
            return "Undefined"
        else:
            return print(f"{limitOperation}Enter valid limit Operation value (1 is >, 2  is ≥  , 3 is < , 4 is ≤)")

    def EnumDataSourceToStringValue(self, enumDataSource):
        if enumDataSource == 1:
            return "MOBILE"
        elif enumDataSource == 2:
            return "COMPUTATION"
        elif enumDataSource == 3:
            return "WEBAPP"
        elif enumDataSource == 4:
            return "INSTRUMENT"
        elif enumDataSource == 0:
            return "UNKNOWN"
        elif enumDataSource == 5:
            return "IMPORT"
        elif enumDataSource == 6:
            return "SPREADSHEETDEF"
        elif enumDataSource == 7:
            return "CONNECT"
        else:
            return print(f"{enumDataSource}Enter valid enumDataSource (valid values are 0-7))")

    def ParseAuditTime(self, dateEntered):       
        dateEntered =datetime.strptime(dateEntered[:15], '%Y-%m-%dT%H:%M')
        dateEntered = dateEntered.replace(tzinfo=timezone.utc)        
        return dateEntered        
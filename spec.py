circuitParameters = {
    "LOAD_KW" : 0,
    "LOAD_AMPS": 0,
    "CABLE_LENGTH" : 50,
    "LOAD_TYPE": "DOL",
    "INSTALL_METHOD": "UNENCLOSED_TOUCHING",
}
systemParameters = {
    "PF_DEFAULT" = 0.9,
    "VOLTAGE_SYSTEM" = 400,
    "VOLTAGE_PHASE" = 230,
    "VOLT_DROP_MAX" = 0.05,
    "CU_CONSTANT" = 0.0225,
    "AL_CONSTANT" = 0.036
}
tableIndex = {
    "14" = table14
    # add tables here
}
table14 = {
    "id" = "TABLE 14",
    "source" = "AS/NZS 3008.1.1-2017",
    "headers" = ["mm^2","AMPS_SPACED","AMPS_TOUCHING"],
    "0" = [500,779,718] ,	
    "1" = [400,685,632]	,
    "2" = [300,594,549]	,
    "3" = [240,517,479]	,
    "4" = [185,240,404]	,
    "5" = [150,377,350]	,
    "6" = [120,330,306]	,
    "7" = [95,283,263]	,
    "8" = [70,229,213]	,
    "9" = [50,180,168]	,
    "10" = [35,147,137]	,
    "11" = [25,119,111]	,
    "12" = [16,88,83]	,
    "13" = [10,66,62]	,
    "14" = [6,48,45]	,
    "15" = [4,38,35]	,
    "16" = [2.5,28,26]	,
    "17" = [1.5,20,19]	,
    "18" = [1,16,14]	
}
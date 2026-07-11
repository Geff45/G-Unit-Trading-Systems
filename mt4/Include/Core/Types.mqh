/*
+------------------------------------------------------------------+
|                                                  Types.mqh       |
|                 G-Unit Trading Systems (GUTS)                    |
|                                                                  |
| Purpose : Common system types, enums and constants               |
| Version : 0.1.0-alpha                                            |
| Platform: MT4 Build 2419                                         |
| Author  : Geoffrey Ndungu & ChatGPT                              |
+------------------------------------------------------------------+
*/

#ifndef __GUTS_TYPES_MQH__
#define __GUTS_TYPES_MQH__

//====================================================
// SYSTEM INFORMATION
//====================================================

#define GUTS_NAME                "G-Unit Trading Systems"
#define GUTS_ENGINE              "ATLAS"
#define GUTS_VERSION_MAJOR       0
#define GUTS_VERSION_MINOR       1
#define GUTS_VERSION_PATCH       0

//====================================================
// LOG LEVELS
//====================================================

enum ENUM_LOG_LEVEL
{
   LOG_TRACE = 0,
   LOG_DEBUG,
   LOG_INFO,
   LOG_WARNING,
   LOG_ERROR,
   LOG_FATAL
};

//====================================================
// MODULE STATES
//====================================================

enum ENUM_MODULE_STATE
{
   MODULE_CREATED = 0,
   MODULE_INITIALIZED,
   MODULE_STARTED,
   MODULE_RUNNING,
   MODULE_STOPPED,
   MODULE_SHUTDOWN,
   MODULE_ERROR
};

//====================================================
// HEALTH STATUS
//====================================================

enum ENUM_HEALTH_STATE
{
   HEALTH_UNKNOWN = 0,
   HEALTH_OK,
   HEALTH_WARNING,
   HEALTH_CRITICAL
};

//====================================================
// MODULE PRIORITIES
//====================================================

enum ENUM_MODULE_PRIORITY
{
   PRIORITY_CORE            = 100,
   PRIORITY_CONFIGURATION   = 200,
   PRIORITY_ANALYSIS        = 300,
   PRIORITY_DECISION        = 400,
   PRIORITY_EXECUTION       = 500,
   PRIORITY_INFRASTRUCTURE  = 600
};

//====================================================
// SYSTEM STATUS
//====================================================

enum ENUM_SYSTEM_STATUS
{
   SYSTEM_STOPPED = 0,
   SYSTEM_STARTING,
   SYSTEM_RUNNING,
   SYSTEM_STOPPING,
   SYSTEM_FAILED
};

#endif
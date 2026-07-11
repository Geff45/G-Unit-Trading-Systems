//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| CORE-002 : Constants                                             |
//| Version : 0.1.0-alpha                                            |
//+------------------------------------------------------------------+
#ifndef __ATLAS_CONSTANTS_MQH__
#define __ATLAS_CONSTANTS_MQH__

//==================================================
// Runtime Information
//==================================================
#define ATLAS_NAME        "ATLAS Runtime"
#define ATLAS_VERSION     "0.1.0-alpha"
#define ATLAS_ENGINE      "GUTS"

//==================================================
// Trading Constants
//==================================================
#define INVALID_PRICE     (-1.0)
#define INVALID_VOLUME    (-1.0)
#define INVALID_TICKET    (-1)

//==================================================
// Timeframes
//==================================================
#define TF_M1   PERIOD_M1
#define TF_M5   PERIOD_M5
#define TF_M15  PERIOD_M15
#define TF_M30  PERIOD_M30
#define TF_H1   PERIOD_H1
#define TF_H4   PERIOD_H4
#define TF_D1   PERIOD_D1
#define TF_W1   PERIOD_W1
#define TF_MN1  PERIOD_MN1

#endif
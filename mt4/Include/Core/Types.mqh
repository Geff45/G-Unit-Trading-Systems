//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| CORE-001 : Types                                                 |
//| Version : 0.1.0-alpha                                            |
//+------------------------------------------------------------------+
#ifndef __ATLAS_TYPES_MQH__
#define __ATLAS_TYPES_MQH__

//==================================================
// Runtime Status
//==================================================
enum ENUM_RUNTIME_STATUS
{
   RUNTIME_STOPPED = 0,
   RUNTIME_INITIALIZING,
   RUNTIME_RUNNING,
   RUNTIME_PAUSED,
   RUNTIME_SHUTTING_DOWN
};

//==================================================
// Market Bias
//==================================================
enum ENUM_MARKET_BIAS
{
   BIAS_UNKNOWN = 0,
   BIAS_BULLISH,
   BIAS_BEARISH,
   BIAS_RANGING
};

//==================================================
// Trade Direction
//==================================================
enum ENUM_TRADE_DIRECTION
{
   TRADE_NONE = 0,
   TRADE_BUY,
   TRADE_SELL
};

//==================================================
// Module State
//==================================================
enum ENUM_MODULE_STATE
{
   MODULE_OFFLINE = 0,
   MODULE_INITIALIZING,
   MODULE_READY,
   MODULE_RUNNING,
   MODULE_ERROR
};

#endif
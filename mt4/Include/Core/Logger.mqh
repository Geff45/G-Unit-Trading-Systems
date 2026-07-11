//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| Module : CORE-003 Logger                                         |
//| Version: 0.1.0-alpha                                             |
//+------------------------------------------------------------------+
#ifndef __ATLAS_LOGGER_MQH__
#define __ATLAS_LOGGER_MQH__

//-------------------------------------------------------------
// Log Levels
//-------------------------------------------------------------
enum ENUM_LOG_LEVEL
{
   LOG_TRACE = 0,
   LOG_DEBUG,
   LOG_INFO,
   LOG_WARNING,
   LOG_ERROR,
   LOG_CRITICAL
};

//-------------------------------------------------------------
// Logger Service
//-------------------------------------------------------------
class CLogger
{
private:

   bool m_enabled;
   ENUM_LOG_LEVEL m_minLevel;

   string LevelToString(ENUM_LOG_LEVEL level);

public:

   CLogger();

   bool Initialize();

   void Shutdown();

   void SetEnabled(bool enabled);

   void SetMinimumLevel(ENUM_LOG_LEVEL level);

   void Trace(string module,string message);

   void Debug(string module,string message);

   void Info(string module,string message);

   void Warning(string module,string message);

   void Error(string module,string message);

   void Critical(string module,string message);

private:

   void Write(
      ENUM_LOG_LEVEL level,
      string module,
      string message
   );

};

#endif
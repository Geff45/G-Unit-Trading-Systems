//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| CORE-006 : Runtime Manager                                       |
//| Version : 0.1.0-alpha                                            |
//+------------------------------------------------------------------+
#ifndef __ATLAS_RUNTIME_MANAGER_MQH__
#define __ATLAS_RUNTIME_MANAGER_MQH__

#include "Configuration.mqh"
#include "Logger.mqh"
#include "EventBus.mqh"

class CRuntimeManager
{
private:

   CConfiguration m_configuration;
   CLogger        m_logger;
   CEventBus      m_eventBus;

public:

   bool Initialize()
   {
      m_configuration.Initialize();
      m_logger.Initialize();
      m_eventBus.Initialize();

      m_logger.Info(
         "Runtime",
         "ATLAS Runtime initialized."
      );

      return(true);
   }

   void Update()
   {
      m_configuration.Update();
      m_logger.Update();
      m_eventBus.Update();
   }

   void Shutdown()
   {
      m_logger.Info(
         "Runtime",
         "ATLAS Runtime shutting down."
      );

      m_eventBus.Shutdown();
      m_logger.Shutdown();
      m_configuration.Shutdown();
   }

   CConfiguration& Configuration()
   {
      return(m_configuration);
   }

   CLogger& Logger()
   {
      return(m_logger);
   }

   CEventBus& EventBus()
   {
      return(m_eventBus);
   }
};

#endif
//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| CORE-005 : Event Bus                                             |
//| Version : 0.1.0-alpha                                            |
//+------------------------------------------------------------------+
#ifndef __ATLAS_EVENTBUS_MQH__
#define __ATLAS_EVENTBUS_MQH__

//==================================================
// Event Types
//==================================================
enum ENUM_EVENT_TYPE
{
   EVENT_NONE = 0,

   EVENT_RUNTIME_STARTED,
   EVENT_RUNTIME_STOPPED,

   EVENT_TICK_RECEIVED,
   EVENT_NEW_BAR,

   EVENT_SIGNAL_CREATED,
   EVENT_ORDER_OPENED,
   EVENT_ORDER_CLOSED,

   EVENT_ERROR
};

//==================================================
// Event Structure
//==================================================
struct SEvent
{
   ENUM_EVENT_TYPE type;

   string source;

   string message;

   datetime timestamp;
};

//==================================================
// Event Bus
//==================================================
class CEventBus
{
private:

   SEvent m_lastEvent;

public:

   CEventBus()
   {
      Reset();
   }

   bool Initialize()
   {
      Reset();
      return(true);
   }

   void Update()
   {
      // Reserved for future queued events
   }

   void Shutdown()
   {
      Reset();
   }

   void Publish(
      ENUM_EVENT_TYPE type,
      string source,
      string message)
   {
      m_lastEvent.type      = type;
      m_lastEvent.source    = source;
      m_lastEvent.message   = message;
      m_lastEvent.timestamp = TimeCurrent();
   }

   SEvent LastEvent()
   {
      return(m_lastEvent);
   }

   void Reset()
   {
      m_lastEvent.type      = EVENT_NONE;
      m_lastEvent.source    = "";
      m_lastEvent.message   = "";
      m_lastEvent.timestamp = 0;
   }
};

#endif
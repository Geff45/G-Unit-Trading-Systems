//+------------------------------------------------------------------+
//| ATLAS Runtime                                                    |
//| CORE-004 : Configuration Manager                                 |
//| Version : 0.1.0-alpha                                             |
//+------------------------------------------------------------------+
#ifndef __ATLAS_CONFIGURATION_MQH__
#define __ATLAS_CONFIGURATION_MQH__

class CConfiguration
{
private:

   bool   m_debugMode;
   bool   m_loggingEnabled;

   double m_defaultRiskPercent;
   int    m_maxSpreadPoints;
   int    m_slippagePoints;

public:

   CConfiguration()
   {
      LoadDefaults();
   }

   bool Initialize()
   {
      return(true);
   }

   void Update()
   {
      // Reserved for future dynamic configuration reload.
   }

   void Shutdown()
   {
   }

   void LoadDefaults()
   {
      m_debugMode          = true;
      m_loggingEnabled     = true;

      m_defaultRiskPercent = 1.0;

      m_maxSpreadPoints    = 20;

      m_slippagePoints     = 5;
   }

   //==========================
   // Getters
   //==========================

   bool DebugMode()
   {
      return(m_debugMode);
   }

   bool LoggingEnabled()
   {
      return(m_loggingEnabled);
   }

   double DefaultRisk()
   {
      return(m_defaultRiskPercent);
   }

   int MaxSpread()
   {
      return(m_maxSpreadPoints);
   }

   int Slippage()
   {
      return(m_slippagePoints);
   }

   //==========================
   // Setters
   //==========================

   void SetDebugMode(bool value)
   {
      m_debugMode = value;
   }

   void SetLoggingEnabled(bool value)
   {
      m_loggingEnabled = value;
   }

   void SetDefaultRisk(double value)
   {
      m_defaultRiskPercent = value;
   }

   void SetMaxSpread(int value)
   {
      m_maxSpreadPoints = value;
   }

   void SetSlippage(int value)
   {
      m_slippagePoints = value;
   }
};

#endif
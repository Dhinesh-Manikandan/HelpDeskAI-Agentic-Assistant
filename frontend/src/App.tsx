import { useState } from 'react';
import './index.css';
import AIAssistant from './views/AIAssistant';
import ArchitectureView from './views/ArchitectureView';
import WorkflowView from './views/WorkflowView';
import DeploymentView from './views/DeploymentView';
import SecurityView from './views/SecurityView';
import MonitoringView from './views/MonitoringView';
import HistoryView from './views/HistoryView';
import ApprovalsView from './views/ApprovalsView';
import ToolRegistryView from './views/ToolRegistryView';
import { Bot, CheckSquare, Clock, Cpu, FileJson, LayoutDashboard, Settings, Shield, Terminal, Zap } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('assistant');

  const renderContent = () => {
    return (
      <>
        <div className={activeTab === 'assistant' ? 'h-full' : 'hidden'}><AIAssistant /></div>
        {activeTab === 'history' && <div className="h-full"><HistoryView /></div>}
        {activeTab === 'approvals' && <div className="h-full"><ApprovalsView /></div>}
        {activeTab === 'tools' && <div className="h-full"><ToolRegistryView /></div>}
        {activeTab === 'monitoring' && <div className="h-full"><MonitoringView /></div>}
        {activeTab === 'architecture' && <div className="h-full"><ArchitectureView /></div>}
        {activeTab === 'workflow' && <div className="h-full"><WorkflowView /></div>}
        {activeTab === 'deployment' && <div className="h-full"><DeploymentView /></div>}
        {activeTab === 'security' && <div className="h-full"><SecurityView /></div>}
      </>
    );
  };

  const navItems = [
    { id: 'assistant', label: 'AI Assistant', icon: <Bot size={18} /> },
    { id: 'history', label: 'History', icon: <Clock size={18} /> },
    { id: 'approvals', label: 'Approvals', icon: <CheckSquare size={18} /> },
    { id: 'tools', label: 'Tools', icon: <Settings size={18} /> },
  ];

  const deliverableItems = [
    { id: 'architecture', label: 'Architecture', icon: <Cpu size={18} /> },
    { id: 'workflow', label: 'Agent Workflow', icon: <Terminal size={18} /> },
    { id: 'deployment', label: 'Deployment', icon: <Zap size={18} /> },
    { id: 'security', label: 'Security Model', icon: <Shield size={18} /> },
    { id: 'monitoring', label: 'Monitoring', icon: <LayoutDashboard size={18} /> },
  ];

  return (
    <div className="flex h-screen bg-background text-slate-200 font-sans overflow-hidden">
      {/* Dynamic Background Elements */}
      <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-brand-500/20 blur-[120px] rounded-full pointer-events-none" />
      <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-blue-500/20 blur-[120px] rounded-full pointer-events-none" />

      <aside className="w-72 glass-panel border-r border-slate-700/50 flex flex-col z-10 relative shadow-2xl">
        <div className="p-8 pb-4">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-brand-400 to-blue-500 flex items-center justify-center shadow-lg shadow-brand-500/30">
              <Bot size={24} className="text-white" />
            </div>
            <h1 className="text-2xl font-bold tracking-tight">HelpDesk<span className="gradient-text">AI</span></h1>
          </div>
          <p className="text-xs text-slate-400 font-medium pl-13">Agentic Enterprise Support</p>
        </div>
        
        <nav className="flex-1 px-4 space-y-2 overflow-y-auto pb-4 mt-6 custom-scrollbar">
          <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 mt-4 px-4">Application core</div>
          {navItems.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${activeTab === tab.id ? 'bg-brand-500/10 text-brand-400 border border-brand-500/20 shadow-inner' : 'hover:bg-slate-800/50 text-slate-400 hover:text-slate-200 border border-transparent'}`}
            >
              {tab.icon}
              <span className="font-medium">{tab.label}</span>
              {activeTab === tab.id && <div className="ml-auto w-1.5 h-1.5 rounded-full bg-brand-400 shadow-[0_0_8px_rgba(45,212,191,0.8)]" />}
            </button>
          ))}
          
          <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 mt-8 px-4">Deliverables</div>
          {deliverableItems.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${activeTab === tab.id ? 'bg-blue-500/10 text-blue-400 border border-blue-500/20 shadow-inner' : 'hover:bg-slate-800/50 text-slate-400 hover:text-slate-200 border border-transparent'}`}
            >
              {tab.icon}
              <span className="font-medium">{tab.label}</span>
              {activeTab === tab.id && <div className="ml-auto w-1.5 h-1.5 rounded-full bg-blue-400 shadow-[0_0_8px_rgba(59,130,246,0.8)]" />}
            </button>
          ))}
        </nav>
      </aside>
      
      <main className="flex-1 overflow-auto z-10 relative">
        <div className="h-full w-full max-w-7xl mx-auto p-4 md:p-8 animate-in fade-in zoom-in-95 duration-500">
            {renderContent()}
        </div>
      </main>
    </div>
  );
}
export default App;

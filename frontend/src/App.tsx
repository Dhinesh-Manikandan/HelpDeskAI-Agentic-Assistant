import { useState, useEffect } from 'react';
import axios from 'axios';
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
  const [hasPendingApprovals, setHasPendingApprovals] = useState(false);

  useEffect(() => {
    const checkApprovals = async () => {
      try {
        const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:8080'}/api/data/approvals`);
        const pending = res.data.some((a: any) => a.status === 'PENDING');
        setHasPendingApprovals(pending);
      } catch (e) {
        console.error(e);
      }
    };

    checkApprovals();
    const interval = setInterval(checkApprovals, 5000);
    return () => clearInterval(interval);
  }, []);



  const navItems = [
    { id: 'assistant', label: 'AI Assistant', icon: <Bot size={18} /> },
    { id: 'history', label: 'History', icon: <Clock size={18} /> },
    { id: 'approvals', label: 'Approvals', icon: <CheckSquare size={18} /> },
    { id: 'tools', label: 'About', icon: <Settings size={18} /> },
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
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 relative ${activeTab === tab.id ? 'bg-brand-500/10 text-brand-400 border border-brand-500/20 shadow-inner' : 'hover:bg-slate-800/50 text-slate-400 hover:text-slate-200 border border-transparent'}`}
            >
              {tab.icon}
              <span className="font-medium">{tab.label}</span>
              {tab.id === 'approvals' && hasPendingApprovals && (
                <span className="absolute right-4 top-1/2 -translate-y-1/2 flex h-2.5 w-2.5">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-red-500"></span>
                </span>
              )}
              {activeTab === tab.id && !(tab.id === 'approvals' && hasPendingApprovals) && <div className="ml-auto w-1.5 h-1.5 rounded-full bg-brand-400 shadow-[0_0_8px_rgba(45,212,191,0.8)]" />}
            </button>
          ))}


        </nav>
      </aside>

      <main className="flex-1 flex flex-col min-h-0 min-w-0 overflow-hidden z-10 relative">
        <div className="flex-1 w-full max-w-7xl mx-auto p-4 md:p-8 animate-in fade-in zoom-in-95 duration-500 flex flex-col min-h-0 min-w-0">
          <div className={activeTab === 'assistant' ? 'flex-1 flex flex-col min-h-0' : 'hidden'}>
            <AIAssistant />
          </div>
          {activeTab === 'history' && <div className="flex-1 overflow-y-auto custom-scrollbar"><HistoryView /></div>}
          {activeTab === 'approvals' && <div className="flex-1 overflow-y-auto custom-scrollbar"><ApprovalsView onResolve={() => setActiveTab('assistant')} /></div>}
          {activeTab === 'tools' && <div className="flex-1 overflow-y-auto custom-scrollbar"><ToolRegistryView /></div>}

        </div>

        {hasPendingApprovals && activeTab !== 'approvals' && (
          <div className="absolute bottom-8 right-8 bg-slate-900 border border-red-500/50 rounded-xl p-5 shadow-2xl z-50 flex items-start gap-4 animate-in slide-in-from-bottom-5">
            <div className="bg-red-500/20 text-red-500 p-2 rounded-lg mt-0.5 border border-red-500/30">
              <CheckSquare size={20} />
            </div>
            <div>
              <h4 className="font-semibold text-slate-200">Approval Required</h4>
              <p className="text-sm text-slate-400 mt-1 mb-3">You have pending agent requests that require human authorization to proceed.</p>
              <button
                onClick={() => setActiveTab('approvals')}
                className="text-xs font-semibold bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition-colors shadow-sm shadow-red-500/20"
              >
                Review Approvals
              </button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
export default App;

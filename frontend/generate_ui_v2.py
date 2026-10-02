import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/frontend/src"
views_dir = os.path.join(base_dir, "views")

app_tsx = """import { useState } from 'react';
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
    switch (activeTab) {
      case 'assistant': return <AIAssistant />;
      case 'history': return <HistoryView />;
      case 'approvals': return <ApprovalsView />;
      case 'tools': return <ToolRegistryView />;
      case 'monitoring': return <MonitoringView />;
      case 'architecture': return <ArchitectureView />;
      case 'workflow': return <WorkflowView />;
      case 'deployment': return <DeploymentView />;
      case 'security': return <SecurityView />;
      default: return <AIAssistant />;
    }
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
"""

ai_assistant_tsx = """import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, Terminal, Loader2, Sparkles, CheckCircle2, AlertCircle, RefreshCw } from 'lucide-react';

export default function AIAssistant() {
    const [request, setRequest] = useState('');
    const [taskId, setTaskId] = useState<number | null>(null);
    const [executions, setExecutions] = useState<any[]>([]);
    const [loading, setLoading] = useState(false);
    const intervalRef = useRef<any>(null);

    const handleSubmit = async () => {
        if (!request) return;
        setLoading(true);
        setExecutions([]);
        try {
            const res = await axios.post('http://localhost:8080/api/agent/request', {
                request,
                userId: "1"
            });
            setTaskId(res.data.id);
            poll(res.data.id);
        } catch (e) {
            console.error(e);
            setLoading(false);
        }
    };

    const poll = (id: number) => {
        if (intervalRef.current) clearInterval(intervalRef.current);
        intervalRef.current = setInterval(async () => {
            try {
                const res = await axios.get(`http://localhost:8080/api/agent/tasks/${id}/executions`);
                setExecutions(res.data);
                const last = res.data[res.data.length - 1];
                if (last && (last.state === 'COMPLETED' || last.state === 'FAILED' || last.state === 'WAITING_FOR_AUTHORIZATION' || last.state === 'CANCELLED')) {
                    clearInterval(intervalRef.current);
                    setLoading(false);
                }
            } catch (e) {
                console.error(e);
            }
        }, 500);
    };

    useEffect(() => {
        return () => { if (intervalRef.current) clearInterval(intervalRef.current); };
    }, []);

    const getStateIcon = (state: string) => {
        switch (state) {
            case 'COMPLETED': return <CheckCircle2 size={16} className="text-green-400" />;
            case 'FAILED': return <AlertCircle size={16} className="text-red-400" />;
            case 'WAITING_FOR_AUTHORIZATION': return <AlertCircle size={16} className="text-yellow-400" />;
            default: return <RefreshCw size={16} className="text-brand-400 animate-spin" />;
        }
    };

    return (
        <div className="h-full flex flex-col gap-6">
            <div>
                <h2 className="text-4xl font-bold tracking-tight mb-2">AI Assistant</h2>
                <p className="text-slate-400">Interact with the autonomous agent to resolve IT requests.</p>
            </div>
            
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 flex-1 h-[calc(100%-6rem)]">
                {/* Chat Panel */}
                <div className="glass-panel rounded-2xl p-1 flex flex-col h-full gradient-border">
                    <div className="bg-surface/80 rounded-xl p-6 flex flex-col h-full border border-slate-700/50">
                        <div className="flex items-center gap-2 mb-6 border-b border-slate-700/50 pb-4">
                            <Sparkles className="text-brand-400" size={20} />
                            <h3 className="text-xl font-semibold">Interaction Console</h3>
                        </div>
                        
                        <div className="flex-1 overflow-auto space-y-6 mb-6">
                            <div className="space-y-3 bg-slate-900/50 border border-slate-800 p-4 rounded-xl">
                                <p className="text-xs font-semibold text-brand-400 uppercase tracking-widest">Suggested Prompts</p>
                                <div className="flex flex-wrap gap-2">
                                    {["My VPN is not working. Create a high priority ticket.", "Close ticket #1042.", "Show my open tickets."].map(prompt => (
                                        <button 
                                            key={prompt}
                                            onClick={() => setRequest(prompt)}
                                            className="text-xs text-left bg-slate-800 hover:bg-slate-700 hover:border-slate-500 px-4 py-2 rounded-lg border border-slate-700 transition-all duration-200 ease-out"
                                        >
                                            {prompt}
                                        </button>
                                    ))}
                                </div>
                            </div>
                            
                            {taskId && (
                                <div className="flex flex-col gap-2">
                                    <div className="self-end max-w-[80%] bg-gradient-to-br from-brand-600 to-brand-500 text-white p-4 rounded-2xl rounded-tr-sm shadow-lg shadow-brand-500/20 text-sm">
                                        {request}
                                    </div>
                                </div>
                            )}
                        </div>
                        
                        <div className="flex gap-3 relative group">
                            <input 
                                type="text" 
                                value={request}
                                onChange={(e) => setRequest(e.target.value)}
                                onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
                                placeholder="Describe your IT issue to the agent..." 
                                className="flex-1 bg-slate-900/80 rounded-xl px-5 py-4 text-slate-200 outline-none border border-slate-700 focus:border-brand-500 transition-all shadow-inner focus:shadow-[0_0_15px_rgba(20,184,166,0.15)] placeholder:text-slate-500 text-sm" 
                            />
                            <button 
                                onClick={handleSubmit}
                                disabled={loading || !request}
                                className="bg-gradient-to-r from-brand-500 to-blue-500 hover:from-brand-400 hover:to-blue-400 disabled:opacity-50 text-white px-6 rounded-xl font-medium transition-all shadow-lg flex items-center justify-center group-focus-within:shadow-[0_0_20px_rgba(20,184,166,0.3)]"
                            >
                                {loading ? <Loader2 className="animate-spin" size={20} /> : <Send size={20} className="transform group-hover:translate-x-1 transition-transform" />}
                            </button>
                        </div>
                    </div>
                </div>

                {/* Agent Workflow Panel */}
                <div className="glass-panel rounded-2xl p-1 flex flex-col h-full gradient-border">
                    <div className="bg-surface/80 rounded-xl p-6 flex flex-col h-full border border-slate-700/50">
                        <div className="flex items-center justify-between mb-6 border-b border-slate-700/50 pb-4">
                            <div className="flex items-center gap-2">
                                <Terminal className="text-blue-400" size={20} />
                                <h3 className="text-xl font-semibold">Agent State Machine</h3>
                            </div>
                            {loading && <span className="flex items-center gap-2 text-xs font-mono bg-blue-500/10 text-blue-400 px-3 py-1 rounded-full border border-blue-500/20"><span className="relative flex h-2 w-2"><span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span><span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span></span> Processing</span>}
                        </div>
                        
                        <div className="flex-1 overflow-auto custom-scrollbar">
                            {executions.length === 0 ? (
                                <div className="text-slate-500 flex flex-col items-center justify-center h-full opacity-50">
                                    <Bot size={48} className="mb-4 text-slate-600" />
                                    <p>Waiting for incoming tasks...</p>
                                </div>
                            ) : (
                                <div className="space-y-0">
                                    {executions.map((exec, idx) => (
                                        <div key={idx} className="flex gap-4 relative pb-6 animate-in slide-in-from-left-4 duration-300" style={{animationDelay: `${idx * 100}ms`}}>
                                            <div className="w-8 flex flex-col items-center relative z-10">
                                                <div className={`w-8 h-8 rounded-full flex items-center justify-center border-2 ${exec.state === 'COMPLETED' ? 'border-green-500/50 bg-green-500/10 text-green-400' : exec.state === 'FAILED' ? 'border-red-500/50 bg-red-500/10 text-red-400' : exec.state === 'WAITING_FOR_AUTHORIZATION' ? 'border-yellow-500/50 bg-yellow-500/10 text-yellow-400' : 'border-brand-500 bg-brand-500/20 text-brand-400 shadow-[0_0_10px_rgba(20,184,166,0.3)]'}`}>
                                                    {getStateIcon(exec.state)}
                                                </div>
                                                {idx < executions.length - 1 && <div className="absolute top-8 bottom-[-24px] w-0.5 bg-gradient-to-b from-brand-500/50 to-slate-700/50" />}
                                            </div>
                                            <div className="flex-1 pt-1">
                                                <div className="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50 shadow-sm hover:border-slate-600 transition-colors">
                                                    <div className="font-bold text-slate-200 tracking-wide">{exec.state}</div>
                                                    {exec.selectedTool && (
                                                        <div className="mt-3 flex items-center gap-2">
                                                            <span className="text-xs text-slate-500 uppercase font-bold tracking-wider">Tool</span>
                                                            <span className="text-xs font-mono bg-blue-500/10 text-blue-400 border border-blue-500/20 px-2 py-0.5 rounded shadow-sm flex items-center gap-1">
                                                                <Settings size={10} /> {exec.selectedTool}
                                                            </span>
                                                        </div>
                                                    )}
                                                    {exec.result && (
                                                        <div className="mt-3 bg-slate-950 p-3 rounded-lg border border-slate-800 text-sm text-slate-300 font-mono">
                                                            {exec.result}
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                    {loading && (
                                        <div className="flex gap-4 relative pb-6 animate-pulse">
                                            <div className="w-8 flex flex-col items-center relative z-10">
                                                <div className="w-8 h-8 rounded-full border-2 border-slate-700 bg-slate-800 flex items-center justify-center">
                                                    <div className="w-2 h-2 bg-slate-500 rounded-full" />
                                                </div>
                                                <div className="absolute top-[-24px] bottom-[32px] w-0.5 bg-gradient-to-b from-brand-500/50 to-slate-700/50" />
                                            </div>
                                            <div className="flex-1 pt-1">
                                                <div className="bg-slate-900/30 p-4 rounded-xl border border-slate-800 h-16 flex items-center">
                                                    <div className="h-4 bg-slate-700 rounded w-1/3" />
                                                </div>
                                            </div>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
"""

with open(os.path.join(base_dir, "App.tsx"), "w") as f:
    f.write(app_tsx)
    
with open(os.path.join(views_dir, "AIAssistant.tsx"), "w") as f:
    f.write(ai_assistant_tsx)

print("Premium UI generated.")

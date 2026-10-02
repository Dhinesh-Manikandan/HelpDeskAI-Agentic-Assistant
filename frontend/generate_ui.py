import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/frontend/src"
views_dir = os.path.join(base_dir, "views")
os.makedirs(views_dir, exist_ok=True)

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

  return (
    <div className="flex h-screen bg-background text-slate-200 font-sans">
      <aside className="w-64 bg-surface flex flex-col border-r border-slate-700">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-brand-500 tracking-tight">HelpDeskAI</h1>
          <p className="text-xs text-slate-400 mt-1">Agentic IT Support</p>
        </div>
        <nav className="flex-1 px-4 space-y-1 overflow-y-auto pb-4">
          <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2 mt-4 px-4">App</div>
          {['assistant', 'history', 'approvals', 'tools'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`w-full text-left px-4 py-2 rounded-lg transition-colors ${activeTab === tab ? 'bg-brand-900 text-brand-100' : 'hover:bg-slate-800'}`}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
          <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2 mt-6 px-4">Deliverables</div>
          {['architecture', 'workflow', 'deployment', 'security', 'monitoring'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`w-full text-left px-4 py-2 rounded-lg transition-colors ${activeTab === tab ? 'bg-brand-900 text-brand-100' : 'hover:bg-slate-800'}`}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
        </nav>
      </aside>
      <main className="flex-1 overflow-auto">
        {renderContent()}
      </main>
    </div>
  );
}
export default App;
"""

with open(os.path.join(base_dir, "App.tsx"), "w") as f:
    f.write(app_tsx)

print("App.tsx created.")

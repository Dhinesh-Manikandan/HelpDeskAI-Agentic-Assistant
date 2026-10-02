import { useState, useEffect } from 'react';
import axios from 'axios';

export default function ToolRegistryView() {
    const [tools, setTools] = useState<any[]>([]);
    
    useEffect(() => {
        axios.get('http://localhost:8080/api/data/tools').then(res => setTools(res.data));
    }, []);

    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-2">About</h2>
            <p className="text-slate-400 mb-8">These are the specific capabilities and tools that the Agentic AI can automatically handle on your behalf to resolve IT requests.</p>
            <div className="grid grid-cols-3 gap-6">
                {tools.map((t: any) => (
                    <div key={t.name} className="bg-surface p-6 rounded-xl border border-slate-700">
                        <h3 className="font-bold text-lg text-brand-400 mb-2">{t.name}</h3>
                        <p className="text-slate-400 text-sm mb-4">{t.description}</p>
                        <div className="flex gap-2 text-xs">
                            <span className="bg-slate-800 px-2 py-1 rounded">Role: {t.requiredRole}</span>
                            <span className={`px-2 py-1 rounded ${t.riskLevel === 'HIGH' ? 'bg-red-500/20 text-red-500' : 'bg-green-500/20 text-green-500'}`}>Risk: {t.riskLevel}</span>
                        </div>
                    </div>
                ))}
            </div>
            
            <div className="mt-12 bg-surface/50 p-6 rounded-xl border border-slate-700/50">
                <h3 className="text-xl font-semibold mb-4 text-slate-200">Example Prompts for the AI Agent</h3>
                <p className="text-sm text-slate-400 mb-6">You can copy and paste the following commands into the AI Assistant's Interaction Console to test the agent's capabilities:</p>
                <div className="space-y-3">
                    <div className="flex flex-col md:flex-row md:items-center gap-2 border-b border-slate-800 pb-3">
                        <span className="text-brand-400 font-mono text-xs w-40 shrink-0">search_knowledge</span>
                        <code className="text-slate-300 text-sm bg-slate-900 px-3 py-1.5 rounded-lg flex-1 select-all">How do I reset my password?</code>
                    </div>
                    <div className="flex flex-col md:flex-row md:items-center gap-2 border-b border-slate-800 pb-3">
                        <span className="text-brand-400 font-mono text-xs w-40 shrink-0">create_ticket</span>
                        <code className="text-slate-300 text-sm bg-slate-900 px-3 py-1.5 rounded-lg flex-1 select-all">My VPN is not working. Create a high priority ticket.</code>
                    </div>
                    <div className="flex flex-col md:flex-row md:items-center gap-2 border-b border-slate-800 pb-3">
                        <span className="text-brand-400 font-mono text-xs w-40 shrink-0">get_my_tickets</span>
                        <code className="text-slate-300 text-sm bg-slate-900 px-3 py-1.5 rounded-lg flex-1 select-all">Show my open tickets.</code>
                    </div>
                    <div className="flex flex-col md:flex-row md:items-center gap-2 border-b border-slate-800 pb-3">
                        <span className="text-brand-400 font-mono text-xs w-40 shrink-0">get_ticket_status</span>
                        <code className="text-slate-300 text-sm bg-slate-900 px-3 py-1.5 rounded-lg flex-1 select-all">What is the status of ticket #[your ticket number]?</code>
                    </div>
                    <div className="flex flex-col md:flex-row md:items-center gap-2">
                        <span className="text-brand-400 font-mono text-xs w-40 shrink-0">close_ticket</span>
                        <code className="text-slate-300 text-sm bg-slate-900 px-3 py-1.5 rounded-lg flex-1 select-all">Close ticket #[your ticket number].</code>
                    </div>
                </div>
            </div>
        </div>
    );
}

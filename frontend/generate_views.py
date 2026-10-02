import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/frontend/src/views"

views = {
    "AIAssistant.tsx": """import { useState, useEffect, useRef } from 'react';
import axios from 'axios';

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

    return (
        <div className="p-8 h-full flex flex-col">
            <h2 className="text-3xl font-bold mb-6">AI Assistant</h2>
            <div className="grid grid-cols-2 gap-8 flex-1">
                {/* Chat Panel */}
                <div className="bg-surface rounded-xl p-6 border border-slate-700 flex flex-col">
                    <h3 className="text-xl font-semibold mb-4 border-b border-slate-700 pb-2">User Request</h3>
                    <div className="flex-1 overflow-auto space-y-4 mb-4">
                        <div className="space-y-2">
                            <p className="text-sm text-slate-400">Try these demo prompts:</p>
                            <div className="flex flex-wrap gap-2">
                                {["My VPN is not working. Create a high priority ticket.", "Close ticket #1042.", "Show my open tickets."].map(prompt => (
                                    <button 
                                        key={prompt}
                                        onClick={() => setRequest(prompt)}
                                        className="text-xs bg-slate-800 hover:bg-slate-700 px-3 py-1 rounded-full border border-slate-600 transition-colors"
                                    >
                                        {prompt}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </div>
                    <div className="flex gap-2">
                        <input 
                            type="text" 
                            value={request}
                            onChange={(e) => setRequest(e.target.value)}
                            onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
                            placeholder="Describe your IT issue..." 
                            className="flex-1 bg-slate-800 rounded-lg px-4 py-3 text-slate-200 outline-none border border-slate-600 focus:border-brand-500 transition-colors" 
                        />
                        <button 
                            onClick={handleSubmit}
                            disabled={loading || !request}
                            className="bg-brand-500 hover:bg-brand-600 disabled:opacity-50 text-white px-6 rounded-lg font-medium transition-colors"
                        >
                            Send
                        </button>
                    </div>
                </div>

                {/* Agent Workflow Panel */}
                <div className="bg-surface rounded-xl p-6 border border-slate-700 flex flex-col">
                    <h3 className="text-xl font-semibold mb-4 border-b border-slate-700 pb-2">Agent Workflow</h3>
                    <div className="flex-1 overflow-auto">
                        {executions.length === 0 ? (
                            <div className="text-slate-500 flex items-center justify-center h-full">Waiting for request...</div>
                        ) : (
                            <div className="space-y-4">
                                {executions.map((exec, idx) => (
                                    <div key={idx} className="flex gap-4">
                                        <div className="w-8 flex flex-col items-center">
                                            <div className="w-3 h-3 rounded-full bg-brand-500 mt-1.5" />
                                            {idx < executions.length - 1 && <div className="w-px h-full bg-slate-700 my-1" />}
                                        </div>
                                        <div className="flex-1 bg-slate-800/50 p-3 rounded-lg border border-slate-700/50">
                                            <div className="font-semibold text-brand-400">{exec.state}</div>
                                            {exec.selectedTool && <div className="text-sm text-slate-300 mt-1">Tool: <span className="font-mono bg-slate-900 px-1 rounded">{exec.selectedTool}</span></div>}
                                            {exec.result && <div className="text-sm text-slate-400 mt-1">{exec.result}</div>}
                                        </div>
                                    </div>
                                ))}
                                {loading && (
                                    <div className="flex gap-4 animate-pulse">
                                        <div className="w-8 flex flex-col items-center">
                                            <div className="w-3 h-3 rounded-full bg-slate-500 mt-1.5" />
                                        </div>
                                        <div className="flex-1 bg-slate-800/20 p-3 rounded-lg border border-slate-700/30">
                                            <div className="h-4 bg-slate-700 rounded w-1/3" />
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
""",
    "ApprovalsView.tsx": """import { useState, useEffect } from 'react';
import axios from 'axios';

export default function ApprovalsView() {
    const [approvals, setApprovals] = useState<any[]>([]);

    const fetchApprovals = async () => {
        const res = await axios.get('http://localhost:8080/api/data/approvals');
        setApprovals(res.data);
    };

    useEffect(() => { fetchApprovals(); }, []);

    const handleResolve = async (id: number, approved: boolean) => {
        await axios.post(`http://localhost:8080/api/agent/approvals/${id}/resolve`, {
            approved, approverId: 3 // ADMIN
        });
        fetchApprovals();
    };

    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-6">Human Approvals</h2>
            <div className="bg-surface rounded-xl border border-slate-700 overflow-hidden">
                <table className="w-full text-left border-collapse">
                    <thead>
                        <tr className="bg-slate-800 text-slate-400 border-b border-slate-700">
                            <th className="p-4">ID</th>
                            <th className="p-4">Action</th>
                            <th className="p-4">Requester</th>
                            <th className="p-4">Status</th>
                            <th className="p-4">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {approvals.map((a: any) => (
                            <tr key={a.id} className="border-b border-slate-700/50">
                                <td className="p-4">{a.id}</td>
                                <td className="p-4 font-mono">{a.actionDetails}</td>
                                <td className="p-4">User {a.requester?.id}</td>
                                <td className="p-4">
                                    <span className={`px-2 py-1 rounded text-xs ${a.status === 'PENDING' ? 'bg-yellow-500/20 text-yellow-500' : a.status === 'APPROVED' ? 'bg-green-500/20 text-green-500' : 'bg-red-500/20 text-red-500'}`}>
                                        {a.status}
                                    </span>
                                </td>
                                <td className="p-4">
                                    {a.status === 'PENDING' && (
                                        <div className="flex gap-2">
                                            <button onClick={() => handleResolve(a.id, true)} className="bg-brand-500 hover:bg-brand-600 text-white px-3 py-1 rounded text-sm transition-colors">Approve</button>
                                            <button onClick={() => handleResolve(a.id, false)} className="bg-slate-700 hover:bg-slate-600 text-white px-3 py-1 rounded text-sm transition-colors">Reject</button>
                                        </div>
                                    )}
                                </td>
                            </tr>
                        ))}
                        {approvals.length === 0 && <tr><td colSpan={5} className="p-8 text-center text-slate-500">No approvals found.</td></tr>}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
"""
}

for name, content in views.items():
    with open(os.path.join(base_dir, name), "w") as f:
        f.write(content)

print("Main views created.")

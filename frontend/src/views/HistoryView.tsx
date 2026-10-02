import { useState, useEffect } from 'react';
import axios from 'axios';
import { ChevronDown, ChevronRight, Bot } from 'lucide-react';

export default function HistoryView() {
    const [tasks, setTasks] = useState<any[]>([]);
    const [expanded, setExpanded] = useState<number | null>(null);
    const [executionsMap, setExecutionsMap] = useState<Record<number, any[]>>({});

    const fetchTasks = async () => {
        const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:8080'}/api/agent/tasks`);
        setTasks(res.data);
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    const toggleExpand = async (taskId: number) => {
        if (expanded === taskId) {
            setExpanded(null);
            return;
        }
        setExpanded(taskId);
        if (!executionsMap[taskId]) {
            const res = await axios.get(`${import.meta.env.VITE_API_URL || 'http://localhost:8080'}/api/agent/tasks/${taskId}/executions`);
            setExecutionsMap(prev => ({ ...prev, [taskId]: res.data }));
        }
    };

    return (
        <div className="h-full flex flex-col gap-6 max-w-5xl mx-auto w-full">
            <div>
                <h2 className="text-3xl font-bold mb-2">Execution History</h2>
                <p className="text-slate-400">View past interactions and agent workflows.</p>
            </div>
            <div className="glass-panel rounded-2xl flex-1 flex flex-col overflow-hidden p-1 gradient-border">
                <div className="bg-surface/80 rounded-xl flex-1 overflow-auto custom-scrollbar border border-slate-700/50 flex flex-col p-2 gap-2">
                    {tasks.length === 0 && <div className="text-center text-slate-500 p-8">No history found.</div>}
                    {tasks.slice().reverse().map((t: any) => (
                        <div key={t.id} className="shrink-0 bg-slate-900/50 border border-slate-700/50 rounded-xl overflow-hidden transition-all duration-300">
                            <div 
                                className="p-4 cursor-pointer hover:bg-slate-800/50 flex items-center gap-4 transition-colors"
                                onClick={() => toggleExpand(t.id)}
                            >
                                <div className="text-brand-400">
                                    {expanded === t.id ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
                                </div>
                                <div className="flex-1">
                                    <div className="font-medium text-slate-200">{t.userRequest}</div>
                                    <div className="text-xs text-slate-500 flex items-center gap-2 mt-1">
                                        <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">Task #{t.id}</span>
                                        <span className={`px-2 py-0.5 rounded font-mono ${t.status === 'COMPLETED' ? 'text-green-400 bg-green-400/10' : t.status === 'FAILED' ? 'text-red-400 bg-red-400/10' : 'text-yellow-400 bg-yellow-400/10'}`}>{t.status}</span>
                                    </div>
                                </div>
                            </div>
                            
                            {expanded === t.id && (
                                <div className="p-4 pt-0 border-t border-slate-700/30 bg-slate-950/30 animate-in slide-in-from-top-2">
                                    {!executionsMap[t.id] ? (
                                        <div className="text-slate-500 text-sm p-4 text-center">Loading response...</div>
                                    ) : (
                                        <div className="mt-4 flex gap-3">
                                            <div className="mt-1">
                                                <div className="w-8 h-8 rounded-full bg-brand-500/20 border border-brand-500 flex items-center justify-center">
                                                    <Bot size={16} className="text-brand-400" />
                                                </div>
                                            </div>
                                            <div className="flex-1 bg-slate-800/80 p-4 rounded-xl rounded-tl-sm border border-slate-700">
                                                <p className="text-sm text-slate-200 whitespace-pre-wrap">
                                                    {executionsMap[t.id][executionsMap[t.id].length - 1]?.result || "No final response."}
                                                </p>
                                            </div>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

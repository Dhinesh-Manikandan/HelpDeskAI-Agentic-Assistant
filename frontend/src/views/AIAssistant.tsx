import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { Send, Terminal, Loader2, Sparkles, CheckCircle2, AlertCircle, RefreshCw, Bot, Settings } from 'lucide-react';

export default function AIAssistant() {
    const [request, setRequest] = useState('');
    const [taskId, setTaskId] = useState<number | null>(null);
    const [executions, setExecutions] = useState<any[]>([]);
    const [loading, setLoading] = useState(false);
    const [chatHistory, setChatHistory] = useState<{request: string, response: string, loading: boolean, executions: any[]}[]>([]);
    const intervalRef = useRef<any>(null);
    const chatEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [chatHistory, executions]);

    const handleSubmit = async () => {
        if (!request) return;
        const currentReq = request;
        setRequest('');
        setChatHistory(prev => [...prev, {request: currentReq, response: '', loading: true, executions: []}]);
        setLoading(true);
        setExecutions([]);
        try {
            const res = await axios.post('http://localhost:8080/api/agent/request', {
                request: currentReq,
                userId: "1"
            });
            setTaskId(res.data.id);
            poll(res.data.id);
        } catch (e) {
            console.error(e);
            setLoading(false);
            setChatHistory(prev => {
                const next = [...prev];
                next[next.length - 1] = { ...next[next.length - 1], response: "Failed to connect to the agent server.", loading: false };
                return next;
            });
        }
    };

    const poll = (id: number) => {
        if (intervalRef.current) clearInterval(intervalRef.current);
        intervalRef.current = setInterval(async () => {
            try {
                const res = await axios.get(`http://localhost:8080/api/agent/tasks/${id}/executions`);
                setExecutions(res.data);
                const last = res.data[res.data.length - 1];
                
                if (last && (last.state === 'COMPLETED' || last.state === 'FAILED' || last.state === 'CANCELLED')) {
                    clearInterval(intervalRef.current);
                    setLoading(false);
                    
                    const finalResponse = last.result || "Task processing finished.";
                        
                    setChatHistory(prev => {
                        const next = [...prev];
                        next[next.length - 1] = { ...next[next.length - 1], response: finalResponse, loading: false, executions: res.data };
                        return next;
                    });
                } else if (last && last.state === 'WAITING_FOR_AUTHORIZATION') {
                    // Update the chat to show it's waiting for approval, but keep polling!
                    setChatHistory(prev => {
                        const next = [...prev];
                        if (next[next.length - 1].loading && !next[next.length - 1].response.includes("approval")) {
                            next[next.length - 1] = { ...next[next.length - 1], response: "This action requires administrator approval. Please review the Approvals tab. Waiting...", loading: true, executions: res.data };
                        } else {
                            next[next.length - 1].executions = res.data;
                        }
                        return next;
                    });
                } else {
                    setChatHistory(prev => {
                        const next = [...prev];
                        next[next.length - 1].executions = res.data;
                        return next;
                    });
                }
            } catch (e) {
                console.error(e);
            }
        }, 1000);
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
            
            <div className="flex-1 h-[calc(100%-6rem)]">
                {/* Chat Panel */}
                <div className="glass-panel rounded-2xl p-1 flex flex-col h-full gradient-border">
                    <div className="bg-surface/80 rounded-xl p-6 flex flex-col h-full border border-slate-700/50">
                        <div className="flex items-center gap-2 mb-6 border-b border-slate-700/50 pb-4">
                            <Sparkles className="text-brand-400" size={20} />
                            <h3 className="text-xl font-semibold">Interaction Console</h3>
                        </div>
                        
                        <div className="flex-1 overflow-auto space-y-6 mb-6 custom-scrollbar pr-2">
                            {chatHistory.length === 0 && (
                                <div className="space-y-3 bg-slate-900/50 border border-slate-800 p-4 rounded-xl mb-4">
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
                            )}
                            
                            {chatHistory.map((chat, idx) => (
                                <div key={idx} className="flex flex-col gap-4 animate-in fade-in slide-in-from-bottom-2">
                                    <div className="self-end max-w-[80%] bg-gradient-to-br from-brand-600 to-brand-500 text-white p-4 rounded-2xl rounded-tr-sm shadow-lg shadow-brand-500/20 text-sm">
                                        {chat.request}
                                    </div>
                                    
                                    <div className="self-start max-w-[80%] bg-slate-800 border border-slate-700 text-slate-200 p-4 rounded-2xl rounded-tl-sm shadow-lg text-sm flex gap-3">
                                        <div className="mt-0.5">
                                            <Bot size={18} className="text-brand-400" />
                                        </div>
                                        <div>
                                            {chat.executions && chat.executions.length > 0 && (
                                                <div className="mb-3 space-y-2 border-l-2 border-slate-700 pl-3">
                                                    {chat.executions.map((exec, eIdx) => (
                                                        <div key={eIdx} className="flex items-center gap-2 text-xs">
                                                            {getStateIcon(exec.state)}
                                                            <span className="text-slate-400 font-mono">
                                                                {exec.state}
                                                            </span>
                                                            <span className="text-slate-500 truncate max-w-sm">
                                                                - {exec.result || "Working..."}
                                                            </span>
                                                        </div>
                                                    ))}
                                                </div>
                                            )}
                                            {chat.loading && !chat.response ? (
                                                <div className="flex items-center gap-2 text-slate-400">
                                                    <Loader2 size={14} className="animate-spin" /> Analyzing and executing task...
                                                </div>
                                            ) : (
                                                <div className="space-y-2 mt-3 pt-3 border-t border-slate-700/50">
                                                    <p className="whitespace-pre-wrap">{chat.response}</p>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            ))}
                            <div ref={chatEndRef} />
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
            </div>
        </div>
    );
}

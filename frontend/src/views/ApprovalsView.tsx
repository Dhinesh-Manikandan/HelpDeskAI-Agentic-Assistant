import { useState, useEffect } from 'react';
import axios from 'axios';

export default function ApprovalsView({ onResolve }: { onResolve?: () => void }) {
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
        if (onResolve) onResolve();
    };

    return (
        <div className="h-full flex flex-col gap-6 max-w-5xl mx-auto w-full">
            <div>
                <h2 className="text-3xl font-bold mb-2">Human Approvals</h2>
                <p className="text-slate-400">Review and manage required authorizations.</p>
            </div>
            <div className="glass-panel rounded-2xl flex-1 flex flex-col overflow-hidden p-1 gradient-border">
                <div className="bg-surface/80 rounded-xl flex-1 overflow-auto custom-scrollbar border border-slate-700/50">
                    <table className="w-full text-left border-collapse min-w-[600px]">
                        <thead className="sticky top-0 bg-slate-800/90 backdrop-blur z-10 shadow-sm border-b border-slate-700/50">
                            <tr className="text-slate-400 text-sm">
                                <th className="p-4 font-semibold rounded-tl-xl">ID</th>
                                <th className="p-4 font-semibold">Action</th>
                                <th className="p-4 font-semibold">Requester</th>
                                <th className="p-4 font-semibold">Status</th>
                                <th className="p-4 font-semibold rounded-tr-xl">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {approvals.map((a: any) => (
                                <tr key={a.id} className="border-b border-slate-700/30 hover:bg-slate-800/30 transition-colors">
                                    <td className="p-4">{a.id}</td>
                                    <td className="p-4 font-mono text-sm">{a.actionDetails}</td>
                                    <td className="p-4">User {a.requester?.id}</td>
                                    <td className="p-4">
                                        <span className={`px-2 py-1 rounded text-xs border ${a.status === 'PENDING' ? 'bg-yellow-500/10 text-yellow-500 border-yellow-500/20' : a.status === 'APPROVED' ? 'bg-green-500/10 text-green-500 border-green-500/20' : 'bg-red-500/10 text-red-500 border-red-500/20'}`}>
                                            {a.status}
                                        </span>
                                    </td>
                                    <td className="p-4">
                                        {a.status === 'PENDING' && (
                                            <div className="flex gap-2">
                                                <button onClick={() => handleResolve(a.id, true)} className="bg-brand-500 hover:bg-brand-600 text-white px-3 py-1 rounded text-sm transition-colors border border-brand-400/50 shadow-sm shadow-brand-500/20">Approve</button>
                                                <button onClick={() => handleResolve(a.id, false)} className="bg-slate-800 hover:bg-slate-700 text-white px-3 py-1 rounded text-sm transition-colors border border-slate-600 shadow-sm">Reject</button>
                                            </div>
                                        )}
                                    </td>
                                </tr>
                            ))}
                            {approvals.length === 0 && (
                                <tr>
                                    <td colSpan={5} className="p-8 text-center text-slate-500">
                                        No approvals found.
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}

import { useState, useEffect } from 'react';
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

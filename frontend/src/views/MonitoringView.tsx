export default function MonitoringView() {
    return (
        <div className="p-8">
            <h2 className="text-3xl font-bold mb-6">Monitoring Dashboard</h2>
            <div className="grid grid-cols-4 gap-6 mb-6">
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">System Status</div>
                    <div className="text-2xl font-bold text-green-400">HEALTHY</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">Total Tasks</div>
                    <div className="text-2xl font-bold text-brand-400">14</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">Pending Approvals</div>
                    <div className="text-2xl font-bold text-yellow-400">1</div>
                </div>
                <div className="bg-surface p-6 rounded-xl border border-slate-700">
                    <div className="text-slate-400 text-sm">AI Mode</div>
                    <div className="text-2xl font-bold text-blue-400">DEMO (Rule-Based)</div>
                </div>
            </div>
        </div>
    );
}

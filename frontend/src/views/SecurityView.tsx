export default function SecurityView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Security Model</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700 space-y-4">
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">1. Role-Based Access Control</h3>
                    <p className="text-sm text-slate-400 mt-1">Users have USER, SUPPORT_AGENT, or ADMIN roles. Tools are restricted by role.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">2. Human-in-the-Loop</h3>
                    <p className="text-sm text-slate-400 mt-1">High-risk tools (like close_ticket) pause execution and require explicit ADMIN approval.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">3. Indirect Database Access</h3>
                    <p className="text-sm text-slate-400 mt-1">The agent cannot execute arbitrary SQL. It only has access to predefined tools in the Tool Registry.</p>
                </div>
                <div className="bg-slate-800 p-4 rounded-lg">
                    <h3 className="font-bold text-brand-400">4. Audit Logging</h3>
                    <p className="text-sm text-slate-400 mt-1">All agent actions and tool executions are persistently logged for compliance.</p>
                </div>
            </div>
        </div>
    );
}

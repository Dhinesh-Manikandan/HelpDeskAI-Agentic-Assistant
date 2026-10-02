export default function ArchitectureView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Architecture Diagram</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700 space-y-6">
                <div className="flex flex-col items-center gap-4 text-center">
                    <div className="bg-brand-900/50 border border-brand-500/50 p-4 rounded-lg w-64">
                        <h3 className="font-bold text-brand-400">React Frontend</h3>
                        <p className="text-xs text-slate-400 mt-1">User Interface & Chat</p>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-64">
                        <h3 className="font-bold">Spring Boot API</h3>
                        <p className="text-xs text-slate-400 mt-1">REST Controllers</p>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="flex gap-4">
                        <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-48">
                            <h3 className="font-bold">Agent Service</h3>
                            <p className="text-xs text-slate-400 mt-1">State Machine & Logic</p>
                        </div>
                        <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-48">
                            <h3 className="font-bold">Tool Registry</h3>
                            <p className="text-xs text-slate-400 mt-1">Controlled Actions</p>
                        </div>
                    </div>
                    <div className="h-8 w-px bg-slate-600"></div>
                    <div className="bg-slate-800 border border-slate-600 p-4 rounded-lg w-64">
                        <h3 className="font-bold">SQLite Database</h3>
                        <p className="text-xs text-slate-400 mt-1">State, Logs, Tickets</p>
                    </div>
                </div>
            </div>
        </div>
    );
}

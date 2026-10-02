export default function WorkflowView() {
    return (
        <div className="p-8 max-w-4xl">
            <h2 className="text-3xl font-bold mb-6">Agent Workflow</h2>
            <div className="bg-surface p-8 rounded-xl border border-slate-700">
                <ul className="space-y-4 font-mono text-sm">
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">RECEIVED &rarr; Request received from user</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">ANALYZING &rarr; Determine intent</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-slate-500">PLANNING &rarr; Select tool</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-yellow-500">WAITING_FOR_AUTHORIZATION &rarr; (If HIGH risk)</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-brand-500">EXECUTING &rarr; Run tool via registry</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-brand-500">VALIDATING &rarr; Check output</li>
                    <li className="bg-slate-800 p-3 rounded border-l-4 border-green-500">COMPLETED &rarr; Return to user</li>
                </ul>
            </div>
        </div>
    );
}
